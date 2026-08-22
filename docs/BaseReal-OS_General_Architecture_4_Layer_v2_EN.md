# General Architecture of the BaseReal-OS Hybrid Four-Layer Computational Model

## The State Controller as an Architectural Condition for Evolution in Systems with Frozen Computational Cores

**BaseReal-OS Technical Preprint Series · Part 1: General Architecture**

---

**Author:** Vitali Colesnicenco
**Affiliation:** Independent Research Project BaseReal-OS · London, United Kingdom
**Date:** August 2026
**Category:** Computer Science / Hardware Architecture / Systems Design
**Status:** Falsifiable Engineering Hypothesis — general architecture (layer content not yet specified)
**License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

---

## Abstract

Modern artificial intelligence architectures and neuromorphic computing systems increasingly rely on fixed weights (frozen layers) for stability and execution speed. However, a frozen computational boundary imposes a fundamental architectural constraint: a system with static weights cannot, on its own, from within itself, change its own way of distinguishing categories — this requires an external input. This paper proposes a general architectural model for BaseReal-OS: a hybrid four-layer system in which three layers (geometric invariants, variety generation, consistency filter) remain fully frozen, while the fourth layer holds a dynamic, path-dependent state. The present work fixes only the general architecture and the status of the hypothesis; the specific mathematical and physical content of each layer is the subject of subsequent papers in the series.

---

## 1. Introduction and Problem Statement

Scaling parameters within a closed, statically weighted computational loop does not yield autonomous evolution of the system's behavior over time. Once weights are fixed, the system operates strictly within the boundaries of the mapping established during training or design — it can produce a varied output within that mapping, but it cannot change the *rules* by which it distinguishes objects, categories, and the relations between them.

This problem is not a new observation. It is structurally related to at least two long-known difficulties:

- **The regress problem of justification** in epistemology: any grounds for a judgment themselves require grounding, and the chain either runs to infinity or comes to rest on an unverifiable postulate.
- **Karl Friston's self-prediction paradox** within the free energy principle: a system that predicts its environment cannot fully predict itself as part of that environment, and is therefore forced to obtain its target priors externally [Friston, 2010].

Formally: a computational system defined by a static mapping *f: X → Y* with parameters Θ_frozen cannot dynamically alter its own basis for distinction. Any attempt to derive new categorical distinctions from within one and the same fixed projection space collapses into a combinatorial enumeration of already-existing invariants — variety of form, but not evolution of rules.

This gives rise to the paper's central question: what is the minimal architectural addition to a purely frozen system that is necessary and sufficient to obtain path-dependent — that is, genuinely evolving rather than merely combinatorially varied — dynamics?

---

## 2. Relation to Existing Approaches

Before formulating the architecture, it is important to state explicitly what in the proposed model is not new and what constitutes an original contribution — otherwise the work cannot be considered a good-faith engineering publication.

**Reservoir Computing.** The idea of a "fixed substrate + a trainable/dynamic layer on top of it" was formalized as early as the early 2000s in the Echo State Network architecture [Jaeger, 2001] and the Liquid State Machine architecture [Maass, Natschläger & Markram, 2002]: a large reservoir of random, non-frozen weights remains unchanged, while only a lightweight readout layer on top of it is trained. The BaseReal-OS architecture is structurally related to this pattern, with two differences. First, the "reservoir" here is not random but consists of several specialized, deterministic functional layers (geometry, variety, consistency), rather than a single undifferentiated pool. Second, the emphasis is placed on the physical realization of the frozen substrate directly in analog silicon, rather than on a software emulation of the reservoir.

**Free Energy Principle.** Friston's formulation of the need for external priors for a system's goal-setting directly motivates Section 4 (architectural hypothesis): the 4th layer in the proposed model performs a function analogous to the place occupied by priors in Friston's model — it remains structurally outside the frozen mapping, and is therefore able to modify it.

**Analog Compute-in-Memory Hardware.** The idea of physically "freezing" computational weights directly into the conductance of a material is not hypothetical but an already practically realized technology (see Section 7).

The original contribution of this work lies not in inventing the state-space scheme as such (it is well known), but in (a) explicitly formulating the architectural constraint as a *falsifiable engineering hypothesis* with a clear refutation criterion, and (b) directly mapping each functional layer onto a specific class of existing or prospective hardware.

---

## 3. General Architecture: Four Functional Layers

Below is a description of the general functional role of each layer. This work deliberately does not fix specific formulas, specific physical laws, or specific algorithms within each layer — that is the subject of separate subsequent papers in the series (see Section 9). Only the architectural contract between the layers is fixed here: what each layer must do, and what it must not.

### 3.1. Layer 1 — Geometric and Spatial Invariants

Functional role: maintaining the basic spatial and structural constraints that any generated frame or object must obey (consistency of form, relations, and scale). The layer is fully frozen: it is not trained and does not change during system operation.

### 3.2. Layer 2 — Variety Generation

Functional role: producing variability from a noise or seed space without repeating previously generated output. The layer is frozen; all the variety it produces is combinatorial variety within the bounds of one and the same fixed mapping, not an evolution of that mapping.

### 3.3. Layer 3 — Consistency and Invariant-Conservation Filter

Functional role: the layer acts as a sieve, checking every frame generated by Layers 1–2 for compliance with a set of fundamental system constraints (conservation laws, consistency, permissible parameter bounds) and rejecting or correcting any violations. It is important to stress: this work deliberately **does not fix** what specific principles make up this set of constraints — it could be a single law, a family of laws, or a hierarchy of rules at different levels. The specific content of Layer 3 (including any named formal laws) is the subject of a separate subsequent paper in the series, where it will be introduced and justified independently of this work. Within the scope of this paper, Layer 3, like Layers 1–2, is fixed as a **fully frozen, deterministic component**.

### 3.4. Layer 4 — State Controller (Stateful Layer)

Functional role: the only layer in the architecture that is not frozen. It holds a dynamic state that accumulates over time, and on each cycle feeds this state as a conditioning input to Layers 1–3, without modifying their weights. It is this layer that provides path-dependence — the fact that the system's previous states influence its subsequent ones — that is, evolution in the strict sense, rather than mere generation of variety.

**Architectural contract between layers** (general schema, without specifying particular functions):

- Layers 1–3 are deterministic, static, and do not change during system operation under any circumstances.
- Layer 4 changes on every cycle but never directly modifies the weights of Layers 1–3.
- The only channel through which Layer 4 influences Layers 1–3 is the input conditioning vector supplied on each computational cycle.
- The only channel through which Layers 1–3 influence Layer 4 is the output of the current cycle's computation, which feeds into the state update.

This schema is deliberately left at the level of a general contract: it fixes a *separation of responsibilities*, not a specific algorithm. The concrete implementation of the state-update function and of the conditioning mechanism is the subject of subsequent papers in the series.

---

## 4. Architectural Hypothesis

> **Working hypothesis (not a postulate).** A computational system with fixed weights is structurally incapable of autonomously changing its own internal logic for distinguishing objects and categories. Changing this logic requires an external conditioning input that is structurally independent of the frozen weights.

The formulation is deliberately given the status of a hypothesis rather than an axiom — it can be refuted (see Section 5), and this is the principled point distinguishing an engineering hypothesis from a metaphysical postulate.

---

## 5. Falsifiability Criteria

The hypothesis is considered refuted if an autonomous, path-dependent evolving system is demonstrated — that is, a system capable of non-trivial re-differentiation of its own categories over time — built on a strictly frozen weight architecture (Θ_fixed), without an external persistent state registry (S_t) and without online retraining of parameters.

Such a criterion makes the hypothesis testable in principle: it specifies a concrete type of counterexample that would refute it, rather than leaving the hypothesis shielded from any possible observation.

---

## 6. Proposed Experimental Validation Program

At the time of publication of this work, no corresponding experiments have been carried out; what follows is not a result but a proposed validation protocol, open for implementation by any party, in the spirit of this publication's open license.

**Minimal test case.** Compare two systems built on the same frozen generative foundation (Layers 1–3 in any specific implementation):

1. **Control group** — a purely frozen system without Layer 4, running for many cycles on a stream of new inputs.
2. **Experimental group** — the same frozen foundation, augmented with Layer 4 in accordance with the architectural contract of Section 3.4.

**Measured quantity.** The system's ability for non-trivial re-differentiation of categories over a long horizon — operationally, this can be measured, for example, via novelty and trajectory-divergence metrics relative to the initial distribution (in the spirit of novelty search methods in evolutionary computation), via the shift of the system's *effective* classification decision boundary at the output — that is, the observed decision rule that arises as a function of the current conditioning input S_t while the weights Θ_frozen remain unchanged — or via tasks that require changing the classification criterion as experience accumulates, without retraining the weights.

**Expected result under the hypothesis.** The control group should show a saturation of variety without structural drift of categories; the experimental group should show cumulative, path-dependent drift. If the control group exhibits the same behavior without Layer 4, the hypothesis is refuted per Section 5.

A detailed protocol, metrics, and open-source code for reproduction are the subject of a separate publication in the series or an open repository, a link to which will be added once available.

---

## 7. Implications for Hardware Implementation

The separation into frozen and dynamic layers maps directly onto an existing and evolving class of hardware solutions, making the architecture not merely theoretical but physically realizable on today's device technology.

**Frozen layers (1–3).** These can be implemented as analog compute-in-memory, where weights are physically encoded in the conductance of non-volatile elements, and multiply-accumulate operations are carried out directly via Ohm's and Kirchhoff's laws, without shuttling data between memory and processor. This removes the primary source of energy loss in digital architectures: according to the now-classic analysis by Horowitz (2014), accessing external DRAM consumes 100–1000 times more energy than the computational operation itself of the same magnitude — and it is precisely this gap that is eliminated when weights are moved directly into the memory where computation occurs. Demonstrated figures for this approach:

- IBM's analog phase-change-memory chip (Ambrogio et al., 2023) — up to 12.4 TOPS/W at sustained performance, more than 14 times more energy-efficient than a comparable digital solution.
- Independently, a 64-core analog IBM phase-change-memory chip for inference of convolutional and recurrent networks (Le Gallo et al., 2023) demonstrates the same architectural principle on a different class of tasks — eliminating memory traffic through fully on-chip integrated computation.
- A ReRAM chip with fully parallel MAC computation — 78.4 TOPS/W [International Solid-State Circuits Conference (ISSCC), 2020].
- The commercial EnCharge AI product — 200 trillion operations per second at 8.25 W (≈24 TOPS/W), claimed as a 20-fold improvement over comparable solutions [Moore, S. K., *EnCharge's Analog AI Chip Promises Low-Power and Precision*, IEEE Spectrum, 2025].

**Layer 4.** By definition must remain on rewritable memory (SRAM/DRAM) — freezing this layer into silicon would deprive the system of the very source of path-dependence for which it was introduced.

For a baseline reference point on digital architecture without in-memory compute: the systolic array of the first Tensor Processing Unit delivered peak performance of 92 TOPS in a fully digital, non-analog implementation [Jouppi et al., *In-Datacenter Performance Analysis of a Tensor Processing Unit*, ISCA, 2017] — the comparison illustrates the scale of the gain that an analog in-memory implementation of the frozen layers provides.

---

## 8. Limitations and Open Questions

This work is deliberately limited in the scope of what it claims. It does **not** assert:

- that the proposed architecture solves the problem of consciousness or constitutes a theory of general intelligence;
- that the state-space formalism between layers is an original invention (see Section 2);
- the specific mathematical or physical content of Layer 3 — this is deliberately left open for subsequent work in the series;
- that the experiments in Section 6 have been carried out — they are proposed as a protocol, not reported as a result.

Open questions left for subsequent papers in the series: a formal definition of the set of invariants for Layer 3; the concrete state-update function U(S_t, I_t, O_t) of Layer 4; empirical testing of the protocol proposed in Section 6; a quantitative comparison with classical reservoir computing architectures on common benchmarks.

---

## 9. Roadmap for the Publication Series

This work fixes only the general architecture and the status of the hypothesis. Planned subsequent papers in the BaseReal-OS series:

- **Part 2.** Formal content of Layer 1 (geometric and spatial invariants).
- **Part 3.** Formal content of Layer 2 (variety-generation mechanism).
- **Part 4.** Formal content of Layer 3 (set of consistency and conservation invariants).
- **Part 5.** Formal state-update function of Layer 4 and empirical results of the protocol in Section 6.

---

## Acknowledgments and Authorship Statement

This work was carried out by a single author as part of the independent research project BaseReal-OS. This publication fixes the date and authorship of the general architectural idea through the DOI assigned by the Zenodo repository.

---

## How to Cite This Work

> Colesnicenco, V. (2026). *General Architecture of the BaseReal-OS Hybrid Four-Layer Computational Model: The State Controller as an Architectural Condition for Evolution in Systems with Frozen Computational Cores*. BaseReal-OS Technical Preprint Series, Part 1. Zenodo. DOI: [to be assigned upon publication].

---

## License

This work is distributed under the terms of the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license.

Full license text: https://creativecommons.org/licenses/by-sa/4.0/

This means:

- **Free use.** Anyone may copy, adapt, distribute, and use this work — including for commercial purposes — without needing to ask permission.
- **Attribution.** Any use must credit the author and this publication.
- **ShareAlike.** This is the key property that makes the license "infect" any use with openness: any derivative work — a modification, an extension, a translation, use of this architecture in another project — must be distributed under the same CC BY-SA 4.0 terms. A derivative work cannot be closed off under a proprietary license: openness is legally inherited by every subsequent generation of derivative works, exactly as it works, for example, for Wikipedia.

---

## References

1. Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.
2. Jaeger, H. (2001). *The echo state approach to analysing and training recurrent neural networks*. GMD Report 148, German National Research Center for Information Technology.
3. Maass, W., Natschläger, T., & Markram, H. (2002). Real-time computing without stable states: A new framework for neural computation based on perturbations. *Neural Computation*, 14(11), 2531–2560.
4. Ambrogio, S., Narayanan, P., Okazaki, A., et al. (2023). An analog-AI chip for energy-efficient speech recognition and transcription. *Nature*, 620(7975), 768–775.
5. Le Gallo, M., Khaddam-Aljameh, R., Stanisavljevic, M., et al. (2023). A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference. *Nature Electronics*, 6, 680–693.
6. International Solid-State Circuits Conference (ISSCC) (2020). A fully integrated analog ReRAM based 78.4 TOPS/W compute-in-memory chip with fully parallel MAC computing. *Proceedings of ISSCC 2020*, 500–502.
7. Moore, S. K. (2025). EnCharge's Analog AI Chip Promises Low-Power and Precision. *IEEE Spectrum*.
8. Jouppi, N. P. et al. (2017). In-Datacenter Performance Analysis of a Tensor Processing Unit. *Proceedings of the 44th Annual International Symposium on Computer Architecture (ISCA)*.
9. Horowitz, M. (2014). 1.1 Computing's energy problem (and what we can do about it). *IEEE International Solid-State Circuits Conference (ISSCC) Digest of Technical Papers*, 10–14.
