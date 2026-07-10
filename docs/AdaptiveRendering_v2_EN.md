# Adaptive Perception and Lazy Rendering: Dynamic Thresholds for Computationally Efficient Rendering

### A hierarchy of relative-change thresholds for resource savings, arbitrary focus, and virtual scientific instruments

**Vitaly Colesnicenco** — Independent Researcher, London, United Kingdom
Version 2, July 2026 — technical revision

*Status: preprint, not peer-reviewed.*

## Abstract

This paper extends the concept of adaptive perceptual resolution introduced in the companion publication to computer rendering. It proposes a hierarchical scale of relative signal-change thresholds (1/4 → 1/8 → 1/16 → 1/32 → 1/64 and beyond) as a basis for attention-driven rendering. The approach relates to existing techniques — level-of-detail (LOD) rendering and foveated rendering — and proposes a single parameterizable mechanism unifying both. Integration of virtual scientific instruments (telescope, microscope, audio amplifier) is discussed as a special case of threshold shifting.

---

## 1. Introduction

When observing a complex scene, a person does not perceive everything with equal clarity: the object in the focus of attention becomes highly detailed, the periphery remains coarser; during rapid motion the whole scene simplifies to preserve smoothness. This is a well-known effect underlying foveated rendering in modern VR systems (Illahi et al., 2020, 2021).

This paper describes how a hierarchical scale of relative signal-change thresholds can serve as a unified mechanism for lazily computed rendering, deliberate focus control, and virtual measurement instruments.

---

## 2. Theoretical Basis

The system responds not to absolute signal values but to relative change compared with the previous state (see the companion paper on the perceptual scale and the Weber-Fechner law).

The proposed discrete threshold scale:

| Threshold | Mode               | Application                        |
| --------- | ------------------ | ---------------------------------- |
| 1/4       | Very coarse        | Fast motion, resource savings      |
| 1/8       | Base working level | Changes below 12.5% are ignored    |
| 1/16      | Medium detail      | Standard observation               |
| 1/32      | High sensitivity   | Detects changes of ~3%             |
| 1/64+     | Maximum detail     | Deep analysis, virtual instruments |

The geometric progression (halving) is computationally convenient and corresponds to long-established LOD approaches in computer graphics.

---

## 3. Lazy Rendering and Automatic Detail Adjustment

Lazy (progressive) rendering means the system does not render the entire scene at maximum quality at all times, but only as needed — the same principle underlying chunk-based streaming in open-world games (e.g., chunk loading in Minecraft) and standard LOD.

- Fast motion / large changes → coarse thresholds (1/4–1/8) → reduced detail
- Slow approach / calm observation → fine thresholds (1/16 → 1/32 → 1/64+) → detail increases automatically

---

## 4. Arbitrary Focus and Virtual Scientific Instruments

When a user focuses on a particular signal, the system shifts the threshold for that signal to finer values — a direct analogue of foveated rendering, where the gaze focus area (via eye-tracking) is rendered at maximum quality while the periphery is coarser (Illahi et al., 2021; Kämäräinen & Siekkinen, 2023).

The same mechanism can serve as the basis for virtual instruments:

- **Telescope** — shift the threshold to 1/64 or 1/128 for distant objects
- **Microscope** — shift to ultra-fine thresholds for small details
- **Audio amplifier** — lower the threshold for audio signals
- **X-ray / radar** — temporarily change the type of signal processed and its sensitivity

Threshold shifting under focus of attention is not merely an engineering metaphor: an analogous effect is well documented in the psychophysiology of auditory attention. The classic "cocktail party effect" (Cherry, 1953) shows that a person can isolate one stream of speech from a noisy mixture by focusing attention on it. Later EEG studies showed that selective attention amplifies the brain's early sensory response (the N1 component, ~100 ms after stimulus onset) for the attended channel — before the signal is fully analyzed for meaning (Hillyard et al., 1973) — meaning the brain physically alters signal gain at the input stage rather than merely selecting from an already-complete result. Studies using direct recordings from auditory cortex confirmed that the neural representation of an attended voice is amplified relative to the rest of the mixture (Mesgarani & Chang, 2012). This can be seen as a biological analogue of the focus-driven threshold shift described above — with the caveat that transferring a finding from auditory neuroscience to a rendering architecture remains a metaphor, not a proven equivalence of mechanisms.

## 5. Algorithm (Pseudocode)

The first version of this algorithm did not account for flickering at the threshold boundary: if a signal oscillates near the `effective_step` value, detail would keep switching back and forth. Below is a corrected version with hysteresis (asymmetric thresholds for raising vs. lowering detail):

```
base_step = user_selected_step  // e.g. 1/16
UP_MARGIN = 1.5   // require a stronger signal to raise detail
DOWN_MARGIN = 0.5 // and a noticeably weaker one to lower it (hysteresis)
EPSILON = 1e-6    // keeps the denominator from hitting zero at absolute darkness/silence

for each signal in the scene:
    delta = abs(current_signal - previous_signal) / max(previous_signal, EPSILON)

    if signal is in user focus or under an instrument:
        effective_step = base_step / 8
    else:
        effective_step = base_step * 2

    if current_detail(signal) == low and delta > effective_step * UP_MARGIN:
        raise_detail(signal)
    else if current_detail(signal) == high and delta < effective_step * DOWN_MARGIN:
        lower_detail(signal)
    // otherwise — leave unchanged, do not switch
```

One detail worth flagging: `EPSILON` in the denominator exists because a relative delta is undefined when `previous_signal == 0` (absolute darkness, absolute silence) — division by zero. The reference value in the denominator must therefore never be allowed to reach true zero; `max(previous_signal, EPSILON)` is the simplest way to enforce that.

What sounds lofty in fundamental physics or philosophy as *'Absolutes are unattainable'* becomes a strict *'Absolutes are impermissible'* in real program code for purely mathematical and computational reasons. The system must always have a minimum reference threshold. 

The proposed algorithm is still a simplification: a real implementation would additionally need to address multi-observer consistency for a shared scene and network latency compensation — neither is addressed here.

## 6. Advantages

1. Resource savings in large-scale simulations
2. Smoother, less abrupt detail transitions when hysteresis is properly tuned
3. Deliberate control over the distribution of computational power via focus
4. Simple integration of virtual measurement instruments
5. Robustness to noise that does not exceed the current threshold

---

## 7. Limitations and Open Questions

- The algorithm has not been implemented or tested; the pseudocode above is a conceptual sketch, not a production-ready specification.
- The numerical threshold values (1/4, 1/8, ...) were chosen for computational convenience (powers of two), not calibrated against data on human perception.
- Not addressed: consistency across multiple observers, network latency, popping artifacts during LOD switches.

---

## 8. Conclusion

A dynamic threshold scale of 1/4 → 1/8 → 1/16 → 1/32, combined with arbitrary focus and hysteresis, can serve as the basis for a unified mechanism connecting lazy rendering, foveated rendering, and virtual measurement instruments within a single parameterizable system.

**Future plans:**

- Browser-based prototype
- Performance and subjective-perception testing across different threshold and hysteresis parameters
- Application in VR/AR and large-scale simulations (open worlds, scientific visualization)

---

## References

- Weber, E.H. (1834). *De Pulsu, Resorptione, Auditu et Tactu*.
- Fechner, G.T. (1860). *Elemente der Psychophysik*.
- Cherry, E.C. (1953). Some experiments on the recognition of speech, with one and with two ears. *Journal of the Acoustical Society of America*, 25(5), 975–979.
- Hillyard, S.A., Hink, R.F., Schwent, V.L., Picton, T.W. (1973). Electrical signs of selective attention in the human brain. *Science*, 182(4108), 177–180.
- Mesgarani, N., Chang, E.F. (2012). Selective cortical representation of attended speaker in multi-talker speech perception. *Nature*, 485(7397), 233–236.
- Illahi, G.K., Van Gemert, T., Siekkinen, M., Masala, E., Oulasvirta, A., Ylä-Jääski, A. (2020). Cloud Gaming with Foveated Video Encoding. *ACM Transactions on Multimedia Computing, Communications, and Applications*, 16(1).
- Illahi, G.K., Siekkinen, M., Kämäräinen, T., Ylä-Jääski, A. (2021). Foveated streaming of real-time graphics. *Proceedings of the 12th ACM Multimedia Systems Conference (MMSys '21)*.
- Kämäräinen, T., Siekkinen, M. (2023). Foveated Spatial Compression for Remote Rendered Virtual Reality. *Proceedings of MetaSys '23*.

*Preprint, not peer-reviewed.*
