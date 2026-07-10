# Adaptive Perceptual Resolution: A Relative Information Scale for Living Systems

**Vitaly Colesnicenco**
*Independent Researcher, London, United Kingdom*
Version 2 (July 2026) — technical revision, metaphysical content removed

*Status: preprint, not peer-reviewed.*

---

## Abstract

This paper proposes a hierarchical scale of perceptual resolution for living systems, based on relative comparison with a previous signal state rather than absolute measurement. The scale spans a range from binary detection to perception of fractional ratios. The work draws on the well-established Weber-Fechner psychophysical law and Stevens' theory of scales of measurement, proposing a generalization of both as a multi-level discrete model applicable to both biological perception and engineered signal-processing systems.

---

## 1. The Problem of Absolute Measurement

Classical information theory (Shannon, 1948) describes static channels with fixed resolution. Biological perception works differently:

- The eye responds to contrast rather than absolute brightness — the retina encodes signal through lateral inhibition (see work on ganglion cells, e.g. Rodieck et al., 1985).
- The ear perceives loudness on a logarithmic scale — the decibel itself is a relative unit of measurement.
- Skin responds primarily to a change in stimulus rather than to its constant presence (sensory adaptation).

This is consistent with the Weber-Fechner law (Weber, 1834; Fechner, 1860): the just-noticeable difference (JND) in a stimulus is proportional to the stimulus's baseline magnitude, rather than being a fixed absolute quantity.

---

## 2. A Relative Information Scale

| Level | Name | Comparison | Theoretical capacity | Noise robustness |
| --- | --- | --- | --- | --- |
| 1   | Binary | Present / Absent | 1 bit | Maximum |
| 2   | Directional | Greater / Less / Equal | log₂(3) ≈ 1.58 bits | High |
| 3   | Proportional | Twice as strong, one-third as weak, etc. | Variable, grows with number of distinguishable gradations | Medium |

**Caveat:** the capacity values in this table are a theoretical combinatorial ceiling (log₂ of the number of distinguishable outcomes), not an empirically measured throughput of any particular sensory system. Real channel capacity is constrained by noise, integration time, and receptor physiology, and is typically lower than the theoretical limit.

The scale relates to Stevens' classification of measurement scales (Stevens, 1946: nominal, ordinal, interval, ratio) — levels 1–3 above correspond roughly to the ordinal and interval scales in that classification.

### Level 1 — Binary

The simplest level: a pulse is either present or not.

### Level 2 — Directional

Comparison with the previous state: better / worse / unchanged.

### Level 3 — Proportional

Perception of relative magnitudes (twice as much, one-third as much, etc.).

---

## 3. Key Implications

- Robustness to external perturbation is higher than in systems using absolute measurement, since noise that does not exceed the current discrimination threshold is filtered out automatically.
- The system can adaptively shift its operating level: under load or stress, it can shift to coarser levels (faster, less precise); under calm conditions, to finer levels.

---

## 4. Relationship to Delta Encoding

To be candid: the mechanism described above is essentially equivalent to delta encoding in computer science — encoding via the difference from a previous state, widely used in video compression, file versioning, and network protocols. The difference lies not in the underlying principle but in the context of application: in living systems this is not an engineered solution designed to save bandwidth, but a property of receptor physiology. In other words, it is the same mathematical technique, implemented biologically rather than designed.

---

## 5. Conclusion

Living systems track change relative to a previous state rather than measuring absolute quantities. The proposed scale formalizes this observation as a set of discrete levels that can serve as a starting point for engineered systems (see the companion paper on adaptive rendering). Empirical validation — comparison against actual psychophysical experiments — has not yet been carried out and remains a subject for future work.

---

## References

- Weber, E.H. (1834). *De Pulsu, Resorptione, Auditu et Tactu*.
- Fechner, G.T. (1860). *Elemente der Psychophysik*.
- Stevens, S.S. (1946). On the theory of scales of measurement. *Science*, 103(2684), 677–680.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.
- Rodieck, R.W., Binmoeller, K.F., Dineen, J. (1985). Parasol and midget ganglion cells of the human retina. *Journal of Comparative Neurology*, 233(1), 115–132.

---

*An open concept for further research. Preprint, not peer-reviewed.*
