# Duet of Algorithms: A Universal Mechanism for Nonlinear Transitions in Dynamical Systems and the Role of Conditional Intent as a Directing Operator

**Author:** Vitaly Kolesnichenko

**Independent Researcher, London, England, United Kingdom** <vitalydecoder@gmail.com>

Platform: BaseReal-OS — <https://vitalydecoder.github.io/BaseReal-OS/>

## Abstract

This paper proposes a unified two-algorithm model of nonlinear dynamics applicable to physical, biological, economic, and cognitive systems. The model postulates the interaction of two competing processes — Algorithm A (a deterministic attractor, a stability vector) and Algorithm B (a stochastic generator, a deviation impulse) — as a sufficient mechanism to explain the threshold avalanche transitions observed across a broad class of phenomena: from avalanche breakdown in semiconductors and the neuronal action potential to the collapse of supernovae, from self-organized criticality to evolutionary leaps — that is, across scales from nanometers to light-years. The central contribution of the paper is the introduction of the concept of **conditional intent** (the IF→THEN operator) as the mechanism by which an observer supplies the controlling system with a directing vector for the avalanche — specifying not merely a goal, but a complete map of the cascade's unfolding. It is shown that this model is consistent with a number of Nobel-winning discoveries in non-equilibrium thermodynamics and the physics of complex systems, and that it also connects substantively with the independently developed program of early-warning signals for critical transitions in ecology and climatology.

The two-algorithm model developed here received empirical testing against historical data of the CBOE VIX volatility index for the period 1990–2026. Statistical analysis confirmed the existence of a pronounced asymmetry between endogenous avalanches (preceded by an anomalously prolonged latent stagnation of the system, averaging 82 days) and exogenous shocks (occurring with zero preceding calm). The differences found are statistically significant at the $p < 0.05$ level (exact Mann-Whitney test, $p \approx 0.029$), which supports the plausibility of the proposed two-algorithm model using real macroeconomic processes as an example; the authors explicitly note the limitations of the sample and the associated ceiling on the test's power (Section 8.3), and invite independent replication on larger datasets.

## 1. Introduction

Modern science describes nonlinear threshold transitions — avalanches, phase transitions, evolutionary bifurcations, neuronal firing — as disparate phenomena within disciplinarily isolated models. Semiconductor physicists, neurophysiologists, non-equilibrium thermodynamicists, climatologists, and economists each use different mathematical apparatus to describe phenomena that, as will be shown, share a single architectural nature.

In 1954, McKay experimentally established the mechanism of avalanche breakdown in silicon — impact ionization of charge carriers in a strong electric field [1]. In 1952, Hodgkin and Huxley formalized the threshold mechanism generating the neuronal action potential [2]. Independently of one another, Thom laid the mathematical foundations of catastrophe theory in 1972 [3], and Haken formulated the principles of synergetics in 1977 [4] — both programs pursued the same unification of discontinuous transitions in dynamical systems that this paper pursues, and the present model owes much to their legacy. In work throughout the 1970s, Prigogine formalized non-equilibrium dissipative structures [5]. In 1987, Bak, Tang, and Wiesenfeld introduced the concept of self-organized criticality (SOC) [6]. In a series of papers on spin glasses and complex systems, Parisi described the statistical mechanics of states near the critical point [7]. Special mention is owed to the program of early-warning signals for critical transitions developed by Scheffer and co-authors [8]: it arrived, independently and empirically, at closely related conclusions in ecology, climatology, and physiology, establishing that the approach to a bifurcation point is accompanied by rising variance and autocorrelation in the signal (critical slowing down). The present paper offers a mechanistic account of the regularities that this program established statistically, and is methodologically indebted to it.

Each of these discoveries describes a local aspect of a phenomenon that this paper proposes to regard as a manifestation of a single two-algorithm mechanism.

We propose a model in which the absence of unification is explained not by the complexity of nature but by the absence of a meta-level of description at which determinism and stochasticity are treated not as opposing ontological positions but as two coupled algorithms of one and the same system.

## 2. The Two-Algorithm Model

### 2.1 Algorithm A — the deterministic attractor

Algorithm A performs the function of minimizing the system's energy expenditure and maintaining structural integrity. In various systems it manifests as:

- the crystal lattice in solid-state physics;
- homeostasis in biological systems;
- institutional inertia in social systems;
- habit and routinization in cognitive systems;
- orbital stability in mechanics.

Formally, Algorithm A is described as an attractor of the system's phase space: the state $S$ tends toward a minimum of the potential function $V(S)$, resisting deviations.

### 2.2 Algorithm B — the stochastic generator

Algorithm B generates fluctuations that grow in proportion to the time the system spends in the stability state maintained by Algorithm A. Its nature in different systems:

- thermal fluctuations in physics;
- accumulation of kinetic energy by charge carriers in a strong electric field;
- random mutations in biology;
- market volatility in economics;
- creative deviation in cognitive processes;
- quantum uncertainty in microphysics (see the caveat on the limits of this analogy in Section 9).

Key property: **the signal of Algorithm B grows monotonically with the duration of local stagnation and the intensity of iterations.** This distinguishes the proposed model from a simple superposition of random noise on a deterministic trajectory.

- **Potential accumulation:** The strength and mass of Algorithm B grow nonlinearly. It is directly proportional to two factors: the duration of stagnation (the time the structure is held by Algorithm A) and the **density of uniform iterations**.
  
- **Time-compression effect:** Within the proposed model, system time is not a linear external scale but is determined by the intensity of internal processes. An increase in the frequency of endogenous events, extreme thermodynamic loading, or a high density of digital computation leads to an accelerated, nonlinear buildup of the critical mass of Algorithm B's potential. As a result, the physical interval before the onset of the phase transition sharply contracts, transforming the expected timescale of the macro-event from long-term to sub-second.
  

### 2.3 Interaction dynamics and the balance coefficient

The state of the system is described by a continuous control coefficient $\alpha$. The absolute values 0 and 1 are inadmissible for this parameter: they generate singularities (terms of the equation vanishing or diverging to infinity, a physically unrealizable instantaneous or infinitely slow accumulation). An epsilon regularizer $\varepsilon = 10^{-5}$ is therefore introduced, setting physically attainable bounds:

$$\alpha \in [\alpha_{min},\ \alpha_{max}], \qquad \alpha_{min} = \varepsilon, \qquad \alpha_{max} = 1 - \varepsilon$$

$$P(t) = \alpha \cdot A(S) + (1-\alpha) \cdot B(t)$$

where $A(S)$ is the deterministic component and $B(t)$ is the accumulated stochastic potential.

- As $\alpha \to \alpha_{max}$ (the system approaches $1-\varepsilon$, never reaching exact unity): the stagnation phase. Algorithm B accumulates potential while held by Algorithm A.
- At $\alpha \approx 0.5$: the bifurcation point. Tension is maximal.
- As $\alpha \to \alpha_{min}$ (the system approaches $\varepsilon$, never reaching exact zero): the avalanche-transition phase. Rapid structural reorganization.

After the avalanche the system settles into a new attractor, $\alpha$ returns to the neighborhood of $\alpha_{max}$ — the cycle restarts.

### 2.4 The Postulate of Discreteness of the Transition

Here it is important to separate two distinct objects that are easily conflated on a first reading of Section 2.3. The coefficient $\alpha$ is a continuous control parameter: it never reaches the exact bounds 0 or 1 and always remains strictly inside $[\varepsilon,\ 1-\varepsilon]$ — in this sense the system is never absolutely static nor absolutely chaotic.

The system state $S$ — the configuration in which Algorithm A currently sits (the crystal lattice, the neuron's membrane potential, an asset's price, the phase of matter) — behaves in a fundamentally different way: it undergoes a discrete jump at the moment $\alpha$ crosses the critical bifurcation threshold ($\alpha \approx 0.5$). Between the "before" state and the "after" state there is no stable intermediate configuration — this is precisely what "avalanche" means throughout the paper (Sections 3, 4.1, 4.2, 4.6, 5.2).

**Postulate of Discreteness of the Transition:** a smooth change in the continuous control parameter $\alpha$ produces a discontinuous (discrete) jump in the state variable $S$ at the moment the critical threshold is crossed. This is not an internal contradiction of the model but the standard architecture of catastrophe theory [3]: a smooth control parameter and a non-smooth, discontinuous state variable coexist within one system. Epsilon regularization pertains to the former ($\alpha$); discreteness pertains to the latter ($S$); the present work holds both statements simultaneously, since they describe different variables of one and the same dynamics.

## 3. Annulling "Randomness" as an Explanatory Principle

Classical physics uses the notion of a "random fluctuation" to explain the triggering mechanisms of avalanche transitions. This explanation is circular: the avalanche occurred because a fluctuation occurred; the fluctuation occurred because the system was unstable.

The two-algorithm model removes this circularity for classical dissipative systems. Avalanche breakdown is not a random caprice of the material. It is a deterministic consequence of the accumulation of Algorithm B's potential up to the threshold at which the cost of maintaining the structure via Algorithm A exceeds the cost of a full recalculation. The transition is discrete (instantaneous) because the system has no intermediate states with sufficient computational stability: it is either one configuration or the other. (On the special status of quantum systems in this argument, see the caveat in Section 9.)

This is consistent with the observation of Bak and co-authors [6] that in SOC systems avalanches of all scales are statistically inevitable — however, the proposed model provides a mechanistic explanation for **why accumulation inevitably leads to an avalanche, rather than merely recording this fact statistically**.

## 4. Examples of Threshold Transitions: From Avalanche Breakdown to Nobel-Winning Discoveries

### 4.1 Avalanche breakdown in semiconductors — McKay (1954)

A free charge carrier (an electron), accelerated by a strong electric field, gains kinetic energy between collisions with the crystal lattice [1]. This is literally the accumulation of potential with each collision iteration — a direct physical realization of Algorithm B. As long as the carrier's energy remains below the ionization threshold, nothing happens: Algorithm A holds the structure, and only a negligible leakage current flows across the junction.

Once the carrier's energy exceeds the lattice's ionization energy, impact ionization occurs: a new electron-hole pair is born, each of which is itself accelerated by the field and generates further carriers — an exponential cascade known in semiconductor theory precisely as *avalanche breakdown*. The phenomenon underlies the physics of semiconductor devices, for which Bardeen, Brattain, and Shockley were awarded the Nobel Prize in 1956 [9]. The transition is sharp rather than gradual: below the critical field — leakage current; above it — exponential multiplication of carriers, with no stable intermediate regime, directly illustrating the principle set out in Section 3.

### 4.2 The neuronal action potential — Hodgkin and Huxley (Nobel Prize 1963)

Synaptic inputs sum on the neuron's membrane, gradually shifting its potential away from resting level — this is Algorithm B, accumulating the contribution of individual impulses. Ion-leak mechanisms and the action of ion pumps hold the resting potential — Algorithm A [2]. As long as cumulative depolarization does not cross the threshold (around −55 mV), nothing happens.

At the moment the threshold is crossed, voltage-gated sodium channels open: an avalanche-like, self-amplifying current arises, producing a full spike — on an all-or-none principle. No intermediate, "half-fired" action potentials exist as a stable configuration — again a direct illustration of Section 3. This mechanism directly links the physical level of the model to the cognitive example of insight discussed in Section 5.4.

### 4.3 Laser pumping — Basov and Prokhorov (Nobel Prize 1964)

The operating principle of the laser is based on population inversion: a system of atoms is pumped to a state in which there are more excited atoms than atoms in the ground state — after which avalanche-like stimulated emission occurs [10].

Here, Algorithm A is the ground state of the atomic system, the potential minimum. Algorithm B is the external pumping, growing monotonically toward population inversion. The inversion point is the bifurcation point. The avalanche emission is the system's transition to a new attractor.

### 4.4 Dissipative structures — Prigogine (Nobel Prize 1977)

Prigogine showed that open thermodynamic systems far from equilibrium are capable of spontaneously forming ordered structures [5]. The Belousov–Zhabotinsky reaction is a classic example: the system oscillates between two states, periodically passing through bifurcation points.

In terms of the proposed model, this is a direct realization of the cyclical interaction of Algorithms A and B: order accumulates tension, bifurcation produces a new structure, which itself becomes the new attractor of Algorithm A.

### 4.5 The physics of complex systems — Parisi (Nobel Prize 2021)

Parisi developed a mathematical apparatus for describing systems with multiple metastable states — spin glasses, bird flocks, climate modes [7]. His key contribution: the understanding that the behavior of complex systems near the critical point obeys universal statistical laws regardless of the specific nature of the system.

The proposed work extends this result: the universality of critical behavior is explained not merely statistically but mechanistically — through a single two-algorithm engine manifesting itself in different substrates.

### 4.6 The collapse and explosion of a supernova — Chandrasekhar (Nobel Prize 1983)

A massive star fuses elements shell by shell up to iron, whose fusion no longer releases energy. Each fusion cycle silently deposits another portion of inert mass in the core — a direct, literal realization of Algorithm B: accumulation without any change in the visible structure. Degenerate-electron pressure holds the core in hydrostatic equilibrium — Algorithm A. As long as the core's mass remains below the Chandrasekhar limit (≈1.4 solar masses), the system remains stable indefinitely [11].

Once the core's mass approaches this limit, degeneracy pressure can no longer compensate for gravity: collapse occurs within a fraction of a second, with no stable intermediate state between "star" and "collapsing core" — the same discreteness of transition seen in Sections 4.1–4.2. The bounce and subsequent ejection of the envelope produce the observed supernova. Type Ia supernovae display the same architecture with even more direct accumulation: a white dwarf literally accumulates matter flowing from a companion star until the mass crosses that same Chandrasekhar threshold — after which an explosive thermonuclear runaway completely disrupts the star [11]. The calculation of this threshold earned Chandrasekhar the 1983 Nobel Prize in Physics, shared with Fowler for work on stellar nucleosynthesis [12].

**A caveat on the status of this example.** Unlike avalanche breakdown and the neuronal action potential, where the entire chain "accumulation → threshold → avalanche" has been traced experimentally in full, in the case of supernovae it is the trigger moment itself (the Chandrasekhar limit) that is firmly established, whereas the precise mechanism by which the stalled post-collapse shock "revives" into an observed explosion remains an area of active research in theoretical astrophysics — the leading hypothesis today, neutrino-driven reheating, was proposed by Bethe and Wilson [13], but full three-dimensional explosion modeling is not yet complete. This example should therefore be read as solid confirmation of the accumulation-and-threshold mechanism (Sections 2–3), not as a claim that the physics of the post-collapse cascade is fully solved.

### 4.7 Comparative table

| **Parameter** | **Classical and Nobel-winning discoveries** | **Two-algorithm model** |
| --- | --- | --- |
| Scale of description | Disciplinarily isolated | Cross-level, unified |
| Object of description | Symptoms and statistics of avalanches | The mechanism and engine of avalanches |
| Role of the observer | Passive or undefined | Active, via conditional intent |
| Determinism vs. chaos | Opposition | Coupled algorithms of one system |
| Explanation of the threshold | Phenomenological | Mechanistic (accumulation of B up to threshold A) |

## 5. Empirical Illustrations

### 5.1 The sandpile model (Bak–Tang–Wiesenfeld)

The classic SOC experiment [6]: grains of sand are added one at a time. Most of the time the system is stable (Algorithm A). Algorithm B's potential grows with each added grain. Upon reaching the critical angle of repose, one additional grain triggers an avalanche of arbitrary scale. The distribution of avalanche sizes follows a power law.

The two-algorithm model reproduces this behavior: the cost of maintaining the angle via Algorithm A becomes higher than the cost of collapse, and the system undergoes a transition. Importantly, the avalanche is not "random" — it is **inevitable** after sufficient accumulation; only the exact moment of the trigger is random.

### 5.2 Phase transitions

Water, when heated, accumulates thermal energy (Algorithm B grows). The crystalline or molecular structure resists (Algorithm A). At 100°C, the cost of maintaining the liquid structure exceeds the cost of transitioning to the gas phase — an avalanche transition. The sharpness of the first-order phase-transition boundary is explained by the same principle: no intermediate stable states exist.

### 5.3 Evolutionary leaps (punctuated equilibrium)

The model of Eldredge and Gould [14] describes evolution as an alternation of long periods of stasis and short periods of rapid speciation. Algorithm A is stabilizing selection, maintaining the adapted phenotype. Algorithm B is the accumulation of neutral mutations and environmental pressure. Once the threshold of the adaptive landscape is exceeded, a rapid cascade of changes follows.

### 5.4 A cognitive example: mastery and insight

Prolonged training (Algorithm A: repetition, structure, error minimization) accumulates neural potential. Insight — the sudden solving of a problem — corresponds to an avalanche transition of Algorithm B, structurally identical to the threshold mechanism generating the action potential described in Section 4.2 [2]. Neurobiologically, this correlates with gamma bursts in the EEG: a sharp, synchronous excitation of neuronal ensembles following a period of latent processing [15].

The Japanese concept of *mushin* (no-mind, an "empty mind" in the martial arts) describes a state of perfect criticality: maximally accumulated training order combined with zero resistance to the avalanche-like action.

## 6. Controlling the Bifurcation Point: Historical Examples

If an avalanche is inevitable given sufficient accumulation of Algorithm B's potential, a practical question arises: can the moment, conditions, and direction of the avalanche be controlled without eliminating it altogether? The history of science and economics offers several answers. As a summary of the theoretical and applied aspects of managing critical states, the table below systematizes the basic strategies for influencing a system near a bifurcation point.

| **Control strategy** | **Physical / technical analogue** | **Mechanism** |
| --- | --- | --- |
| **Raising the stability threshold** | Stabilization of nitroglycerin using A. Nobel's method (the creation of dynamite) | Artificially holding the parameter $\alpha$ at a high level to prevent premature detonation from noise. |
| **Forced technological window** | The mechanism of stock-market "circuit breakers" | Forced halting of Algorithm A's iterations once a critical density of events is exceeded, in order to dissipate stochastic potential. |
| **Dynamic damping / balancing** | Absorbing rods in a nuclear reactor core | Introduction of a controlled counter-signal, proportional to the rate of growth of local stagnation, to prevent a cascading transition. |

### 6.1 Dynamite — Alfred Nobel (1867)

Nitroglycerin is a classic example of a system with an extremely low bifurcation threshold: Algorithm A (the molecular structure) maintains equilibrium, while Algorithm B (mechanical or thermal impact) accumulates potential instantly under minimal external influence. The result is an uncontrolled avalanche-like detonation from a random jolt.

Nobel did not eliminate the avalanche. He **raised the triggering threshold** by mixing nitroglycerin with kieselguhr (diatomaceous earth): the molecular structure was stabilized by a porous carrier, which increased the required trigger impulse by orders of magnitude. Accidental detonation became practically impossible; directed, on-command explosion became reproducible.

In terms of the model: Nobel increased the system's $\alpha$ — making Algorithm A dominant under conditions of ordinary handling — while preserving the full potential of Algorithm B for controlled release. The detonating fuse became the physical embodiment of conditional intent: the time to triggering was literally measured in meters of cord, and the cascade was transmitted strictly along a predetermined path.

### 6.2 Antibiotics and control of a biological avalanche — Fleming, Florey, Chain (Nobel Prize 1945)

A bacterial infection represents an avalanche process: the exponential growth of a pathogen (Algorithm B) versus the organism's immune response (Algorithm A). Before the discovery of penicillin, the only strategy was to strengthen Algorithm A (immune support). Fleming discovered, and Florey and Chain developed, a mechanism for the direct suppression of Algorithm B: penicillin blocks the synthesis of the bacterial cell wall, preventing the very accumulation of avalanche potential. This is the first example of **preventive control of Algorithm B** in a biological system.

### 6.3 Stock-market circuit breakers — financial regulators (since 1988)

After the U.S. stock market crash of October 19, 1987 (Black Monday, -22.6% in a single day), the Brady Commission recommended implementing a circuit-breaker mechanism — an automatic halt of trading upon reaching threshold levels of decline [16, 17].

The mechanism directly reproduces control of the bifurcation point: when the S&P 500 index falls by 7%, trading is halted for 15 minutes. At 13%, a repeated pause follows. At 20%, trading closes for the day. In March 2020, during the crash associated with the COVID-19 pandemic, circuit breakers were triggered four times within two weeks; in three of the four cases, the pause stabilized the decline at the trigger level [16].

In terms of the model: a circuit breaker artificially raises $\alpha$ at the moment an avalanche is building — it introduces a forced period of Algorithm A activity (informational realignment), giving participants time to rationally reassess their positions. However, China's experience in 2016 showed the opposite effect: circuit breakers lasted only four days before being suspended, since the very fact of approaching the threshold provoked panic selling [17]. This confirms the non-trivial nature of bifurcation control: an incorrectly chosen threshold can **accelerate** an avalanche rather than contain it.

### 6.4 Nuclear reactors — a controlled chain reaction

Nuclear fission represents an avalanche process in its purest form: each decaying atom emits neutrons that trigger the decay of the next (Algorithm B in exponential mode). In an atomic bomb, the avalanche unfolds uncontrollably. In a nuclear reactor, control rods made of neutron-absorbing materials (cadmium, boron) act as regulators of $\alpha$: they continuously balance the system near criticality, allowing Algorithm B neither to die out (subcritical mode) nor to explode (supercritical mode).

This is the most precise physical realization of the concept of a controlled dance between the two algorithms: the system is deliberately held at $\alpha \approx 0.5$ for maximum energy output under full control of the avalanche [18].

### 6.5 The general principle of bifurcation control

Analysis of the examples above allows three strategies for controlling the bifurcation point to be identified:

| **Strategy** | **Mechanism** | **Example** |
| --- | --- | --- |
| Raising the threshold | Strengthening Algorithm A, reducing sensitivity to the trigger | Dynamite, antibiotics |
| Forced pause | Temporarily braking Algorithm B at the moment of buildup | Stock-market circuit breakers |
| Balancing near criticality | Continuous adjustment of $\alpha$ to maintain a controlled avalanche | Nuclear reactor |

None of these three strategies eliminates the avalanche as such — they control its **moment, scale, and direction**. This confirms the central thesis: an avalanche is inevitable once Algorithm B's potential has accumulated; the task of control is not to prevent it but to direct it.

## 7. Conditional Intent as a Directing Operator

### 7.1 Two levels of goal-setting

To accurately understand the mechanisms of subject-driven control, a strict distinction must be drawn between two qualitatively different levels of goal-setting:

1. **Intent (unconditional):** This is the classical, ordered, vectorial form of motion. It consists of consistently holding focus on a specific goal and attempting a linear development of the system. In terms of the model, this functions as a stabilizer of Algorithm A during the stagnation phase. However, unconditional intent is completely blind to phase transitions: at the moment stability sharply collapses ($\alpha \to \alpha_{min}$), the chaotic outburst of Algorithm B simply sweeps this vector away, rendering the holding of focus useless.
  
2. **Conditional intent:** This is meta-control constructed with full knowledge of the inevitability of the coming avalanche. Instead of trying to hold on to the old vector, it functions as a conditional operator ("IF/WHEN trigger X occurs $\to$ THEN scenario Y is launched"). Conditional intent does not fear chaos; it uses it: by mapping out the desired cascade scenario in advance, the subject creates informational "channels" in the landscape of the system. When the avalanche breaks loose, the energy released by Algorithm B does not destroy the goal but flows in a directed way along these channels, instantly unfolding the required outcome.
  

It is worth acknowledging the predecessor of this idea in experimental psychology: Gollwitzer [19] showed that the structure "IF situation X occurs → THEN I do Y" (implementation intentions) sharply raises the probability that an intention will be realized, compared with simply setting a goal, because it delegates the decision in advance to a situational trigger rather than requiring a renewed act of will at the moment of action. The present work borrows this same logical structure and carries it over from the plane of individual action planning to the plane of controlling a system's avalanche transitions.

### 7.2 The IF→THEN operator as a map of the cascade

Conditional intent of the form:

**"If [condition A] → then [action B] → which opens up [condition C] → ..."**

provides the system with a complete map of the cascade's unfolding. Each link in the chain is simultaneously the collapse point of the superposition of the previous level and the trigger for the next.

Example: *"If revenue grows several-fold → then we lease the adjacent premises → we open a second production line → we hire a manager → we scale the model to another city."*

The controlling system receives not a destination but a **marked-out route with intermediate verification points**. This differs fundamentally from simple goal-setting.

### 7.3 The analogy with the detonating fuse

Alfred Nobel, in creating a safe detonator, was solving the same problem: how to ensure the directed transmission of explosive energy along a set path while ruling out accidental detonation. The Bickford fuse is the physical analogue of conditional intent: the time to triggering is measured in meters of cord, and the cascade is transmitted strictly along the set path.

Conditional intent is the informational equivalent of the detonating fuse: it does not prevent the avalanche (which is inevitable given the accumulated potential of Algorithm B), but it **determines its direction and the sequence of its unfolding**.

### 7.4 Volitional focus as an accumulation mechanism

Sustained holding of attention on a conditional chain functions as an amplification of Algorithm A's signal in a given direction. This creates an anisotropy in the potential landscape: upon reaching bifurcation, the avalanche is more likely to develop along the route "paved" in advance.

This is consistent with neurobiological data on directed priming: prior activation of neural pathways lowers the threshold for their subsequent firing [20].

### 7.5 Historical and philosophical parallels, and the cyclicity of states

In metaphysical and spiritual traditions, the concept of subject-driven intent has historically served as a fundamental regulator of the dynamics of states, intuitively reflecting the phases of the two-algorithm cycle described here. Categories such as *intention* in Buddhist psychology, *kavvanah* (directedness of the heart) in Jewish mysticism, and *niyyah* (conscious will) in Islamic ethics have traditionally described the first phase — the holding of volitional focus, which is metaphysically equivalent to the fixation of Algorithm A's attractor and the accumulation of latent potential.

However, the proposed model extends this historical basis by closing it into a full cycle that includes the system's inevitable collapse into a critical state. In this paradigm, classical linear intent is not replaced but complemented by the conditional-intent operator (`IF→THEN`). Whereas traditional practices focused on the static phase of holding a goal, the introduction of the conditional operator enables subject-driven control during the dynamic phase of the avalanche transition. Thus the subject achieves control not in spite of chaos but through it, mapping out informational channels for the energy released by Algorithm B, which ensures a continuous and controlled cyclicity of the system's transitions from one stable state to another.

**Methodological caveat.** Section 7.5 describes historical and philosophical parallels at the level of analogy, not physical mechanism: the connection between spiritual practices of holding intent and the parameter $\alpha$ is metaphorical rather than measurable. Unlike Sections 4–6, where Algorithm B is operationalized through physically measurable quantities (charge-carrier energy, membrane potential, trading volume), empirical testing of the claims in Section 7 remains an open task.

## 8. Empirical Verification of the Model on Financial-Market Data (the CBOE VIX Index)

### 8.1 Methodology and operationalization of parameters

To test empirically the hypothesis of the accumulation of latent avalanche potential during the stagnation phase (Algorithm A) and its subsequent discharge (Algorithm B), daily historical data of the CBOE volatility index were used, covering a 36-year period (1990–2026) [21]. The VIX index serves as an ideal proxy indicator of the state of systemic chaos: its low values reflect a stable, ordered state (stagnation), while sharp upward spikes (volatility explosions) mark moments of panic and phase transitions. The "latent stagnation" parameter was operationalized as the number of consecutive days during which the VIX remained continuously below 15 points within the 90-day window preceding a critical event.

This operationalization connects substantively with the critical-slowing-down indicators from Scheffer and co-authors' early-warning-signals program [8] — rising variance and autocorrelation in the signal ahead of a critical transition. The present work uses a coarser proxy (duration below a fixed threshold), and subsequent replication would benefit from a direct calculation of VIX variance and autocorrelation in a rolling window instead of a threshold criterion.

### 8.2 Analysis results: the asymmetry of endogenous and exogenous avalanches

All recorded large-scale volatility spikes were divided into two groups based on the nature of the trigger. The first group — *endogenous avalanches* — matured within the market's own structure: the 2007 Global Financial Crisis (preceded by an anomalous latent stagnation of a record 136 consecutive days), the "Volmageddon" incident of February 2018 (115 days of continuous calm amid an aggressive, creeping rise in the indices), the 2015 Chinese yuan devaluation (23 days of calm), and the August 2024 yen carry-trade crisis (55 days). The average duration of latent stagnation for this group was 82 days. The second group — *exogenous avalanches (external shocks)* — was caused by events outside the perimeter of the financial system: the September 11, 2001 terrorist attacks, the collapse of LTCM following Russia's 1998 default, the 2010 technical Flash Crash, and the March 2026 geopolitical oil shock, with a VIX peak of 35 points. For all exogenous events, the duration of preceding calm was 0 days, since the system had been operating in a regime of ordinary noise immediately before the shock.

Applying the exact two-sided Mann–Whitney test gives a statistic of $U = 16$ (complete separation of the groups: every endogenous observation exceeds every exogenous observation) and a value of $p \approx 0.029$. For a sample of $n_1 = n_2 = 4$, this is in fact the smallest value the exact test can attain: $p_{min} = 2 / C(8,4) = 2/70 \approx 0.029$ — the test cannot go below this floor for any outcome, regardless of the true effect size. The result is significant at the conventional $p < 0.05$ level, but does not reach the stricter $p < 0.01$ threshold; claiming $p < 0.01$ at this sample size would be mathematically incorrect (see Section 8.3).

### 8.3 Limitations of the empirical base

Despite significance at the $p < 0.05$ level, this test carries a number of built-in limitations. At $n_1 = n_2 = 4$, the exact Mann–Whitney test physically cannot produce a value below $p \approx 0.029$ for any outcome — this is a property of the test's power at this sample size, not an assessment of effect size; stricter significance levels ($p < 0.01$) are unattainable without expanding the sample, regardless of how pronounced the true asymmetry may be. The overall sample of landmark historical macro-crises over the stated period is limited (8 key precedents), and the procedure for classifying events as endogenous or exogenous relies partly on qualitative expert judgment of context, made post hoc by the author himself, which creates a risk of confirmatory selection (events were chosen as already-known examples rather than as an exhaustive list of all major VIX spikes over the period). At such a small $n$, the choice of threshold (15 points) and window width (90 days) could also have materially affected the resulting $p$-value. Final verification of the model requires independent replication on denser datasets with a methodology of classification and thresholds fixed in advance (ex ante) — for example, on an exhaustive list of all VIX spikes over the period without selection, on the microstructural parameters of distributed ledgers, the order-book depth of high-frequency trading (HFT), or the bioelectrical signals of mycelial networks under simulated stress conditions.

## 9. Resolving the Dispute Between Determinism and Indeterminism

Throughout the 20th century, physics was marked by a fundamental conflict between the deterministic worldview (Newton, Einstein: "God does not play dice") and the probabilistic interpretation of quantum mechanics (Bohr, Heisenberg: fundamental randomness).

The two-algorithm model proposes a synthesis for the class of macroscopic classical dissipative systems:

**Within this class, the world is simultaneously deterministic and stochastic — not in contradiction, but in coupling.**

- Algorithm A realizes determinism: within the current stable configuration, the system's evolution is predictable.
- Algorithm B realizes stochasticity: the accumulation of potential and the moment of the avalanche's trigger obey probabilistic laws.
- The interaction of the two algorithms produces the observed picture: predictability within periods of stability, and unpredictability of the moment (but not the fact) of the avalanche.

For avalanche breakdown, the neuronal action potential, phase transitions, and market avalanches, Einstein was right within Algorithm A: the holding of structure is deterministic. Bohr was right within Algorithm B: the moment of the trigger obeys probabilistic laws. Within the classical domain, the dispute turns out to be a meta-level misunderstanding: both were describing different components of one and the same mechanism.

**An important caveat on the limits of this synthesis.** The present synthesis is formulated for macroscopic classical systems — semiconductors, neurons, financial markets, ecosystems — where Algorithm B describes the accumulation of energy or tension through a sequence of classical interactions. It is not a claim to resolve the hidden-variables problem in quantum mechanics. Experimental violations of Bell's inequalities [22, 23] empirically rule out a broad class of local deterministic models of quantum phenomena: it has been shown that no theory with local hidden variables can reproduce the full set of quantum correlations. The mention of quantum uncertainty and the quantum jump in Sections 2.2 and 3 should be understood as a structural analogy of threshold behavior at the level of the curve's shape, not as a claim about the physical mechanism of wavefunction collapse. Whether the two-algorithm framework applies at the quantum level, and in what form — for instance, to non-local models not forbidden by Bell's theorem — remains an open question requiring separate, considerably more rigorous treatment beyond the scope of the present paper.

## 10. Limitations and Open Questions

The proposed model is conceptual in nature and requires further formalization:

1. **Quantitative specification of Algorithm B:** the potential-growth function $B(t)$ is postulated to be monotonically increasing, but its specific form for different classes of systems requires empirical refinement — in particular, comparison against critical-slowing-down indicators [8].
  
2. **Measuring the coefficient $\alpha$:** an operational definition of $\alpha$ for systems of different natures (physical, biological, social) remains an open question.
  
3. **The mechanism of avalanche directionality:** exactly how conditional intent creates anisotropy in the potential landscape is a question requiring experimental testing in cognitive neuroscience, beyond the metaphorical parallels of Section 7.5.
  
4. **Scope of applicability to quantum systems:** as noted in Section 9, the synthesis of determinism and indeterminism proposed in this paper is limited to classical macroscopic systems. Extending the model to the quantum level requires explicit reconciliation with the experimental violations of Bell's inequalities [22, 23] and cannot be postulated by analogy.
  
5. **The problem of system boundaries for exogenous shocks:** it is conceptually admissible that an event classified as exogenous relative to the financial market may itself be an endogenous avalanche within some broader system of which the market is a part (for example, market microstructure or the network of sovereign credit obligations). However, a rigorous test of this hypothesis requires first solving the problem of system individuation — defining, ex ante and independently of the observed outcome, the boundaries of the candidate super-system and the observable variable tracking its accumulated potential. This is feasible for systems with transparent, market-generated signals (e.g., credit spreads, HFT share), but not for systems characterized by strategic opacity and deliberate distortion of information by the parties involved — such as international geopolitics, where any retrospectively constructed "tension index" is inevitably distorted by the deliberate concealment and disinformation that define the very nature of that domain. This paper therefore does not extend the endogeneity/exogeneity test beyond financial markets and leaves this as an open methodological question rather than a claim.
  

## 11. Conclusion

This paper proposes a two-algorithm model of nonlinear dynamics that unifies a broad class of threshold avalanche transitions in physical, biological, economic, and cognitive systems. The model:

1. Removes "randomness" as an independent explanatory principle for classical dissipative systems, replacing it with the mechanism of Algorithm B's potential accumulation;
2. Is consistent with a number of Nobel-winning and classical discoveries — from avalanche breakdown in semiconductors and the neuronal action potential to non-equilibrium thermodynamics, the physics of complex systems, and the collapse of supernovae — as particular manifestations of a single mechanism operating across scales from the semiconductor junction to the star, and draws on prior unification programs: Thom's catastrophe theory, Haken's synergetics, and Scheffer and co-authors' early-warning signals for critical transitions;
3. Introduces the conditional-intent operator (IF→THEN) — a structure independently studied in experimental psychology as implementation intentions [19] — as an informational analogue of a detonating fuse: a mechanism for directing an inevitable avalanche along a set route;
4. Proposes a coupled, rather than opposed, synthesis of determinism and indeterminism — explicitly limited to classical macroscopic systems and making no claim to resolve the question of local hidden variables in quantum mechanics.

The author invites researchers to critically examine and empirically verify the concepts proposed here.

## References

[1] McKay, K. G. (1954). Avalanche Breakdown in Silicon. *Physical Review*, 94(4), 877–884.

[2] Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500–544.

[3] Thom, R. (1972). *Structural Stability and Morphogenesis*. W. A. Benjamin.

[4] Haken, H. (1977). *Synergetics: An Introduction*. Springer.

[5] Prigogine, I., & Stengers, I. (1984). *Order Out of Chaos: Man's New Dialogue with Nature*. Bantam Books.

[6] Bak, P., Tang, C., & Wiesenfeld, K. (1987). Self-organized criticality: An explanation of the 1/f noise. *Physical Review Letters*, 59(4), 381–384.

[7] Parisi, G. (1983). Order parameter for spin-glasses. *Physical Review Letters*, 50(24), 1946–1948.

[8] Scheffer, M., Bascompte, J., Brock, W. A., Brovkin, V., Carpenter, S. R., Dakos, V., Held, H., van Nes, E. H., Rietkerk, M., & Sugihara, G. (2009). Early-warning signals for critical transitions. *Nature*, 461(7260), 53–59.

[9] Bardeen, J., & Brattain, W. H. (1948). The transistor, a semi-conductor triode. *Physical Review*, 74(2), 230–231.

[10] Basov, N. G., & Prokhorov, A. M. (1954). Application of molecular beams to the radio spectroscopic study of the rotation spectra of molecules. *JETP*, 27, 431.

[11] Chandrasekhar, S. (1931). The Maximum Mass of Ideal White Dwarfs. *Astrophysical Journal*, 74, 81–82.

[12] Burbidge, E. M., Burbidge, G. R., Fowler, W. A., & Hoyle, F. (1957). Synthesis of the Elements in Stars. *Reviews of Modern Physics*, 29(4), 547–650.

[13] Bethe, H. A., & Wilson, J. R. (1985). Revival of a stalled supernova shock by neutrino heating. *Astrophysical Journal*, 295, 14–23.

[14] Eldredge, N., & Gould, S. J. (1972). Punctuated equilibria: An alternative to phyletic gradualism. In T. J. M. Schopf (Ed.), *Models in Paleobiology* (pp. 82–115). Freeman Cooper.

[15] Bhattacharya, J., & Petsche, H. (2005). Drawing on mind's canvas: Differences in cortical integration patterns between artists and non-artists. *Human Brain Mapping*, 26(1), 1–14.

[16] Greenwald, B., Stein, J., & Stiglitz, J. (1989). Financial Market Imperfections and Business Cycles. *Quarterly Journal of Economics*, 104(4), 651–660.

[17] Goldstein, I., & Pauzner, A. (2005). Demand-Deposit Contracts and the Probability of Bank Runs. *The Journal of Finance*, 60(3), 1293–1327.

[18] Hetrick, D. L. (1993). *Dynamics of Nuclear Reactors*. American Nuclear Society.

[19] Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple plans. *American Psychologist*, 54(7), 493–503.

[20] Tulving, E., & Schacter, D. L. (1990). Priming and human memory systems. *Science*, 247(4940), 301–306.

[21] Chicago Board Options Exchange (CBOE). *VIX Historical Data, 1990–2026*. Retrieved from <https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv>

[22] Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika*, 1(3), 195–200.

[23] Aspect, A., Dalibard, J., & Roger, G. (1982). Experimental test of Bell's inequalities using time-varying analyzers. *Physical Review Letters*, 49(25), 1804–1807.
