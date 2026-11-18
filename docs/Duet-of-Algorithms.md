<!-- kicker: BaseReal-OS · Preprint · Version 2.0 -->
<!-- formulas: A — restoring attractor | B — latent stock | $P = \alpha A + (1-\alpha) B$ | $\hat\alpha = 1 - \hat\rho_1$ -->
<!-- running: Duet of Algorithms · v2.0 · V. Colesnicenco · 2026 -->
<!-- watermark: A ⇄ B -->
<!-- keeptables: 8 -->
# Duet of Algorithms: A Two-Process Architecture of Threshold Transitions, from Dissipative Systems to Topological and Measurement-Induced Phases, and the Role of Conditional Intent as a Directing Operator

**Version 2.0** (November 2026)

**Author:** Vitali Colesnicenco

**Independent Researcher, London, England, United Kingdom** <vitalydecoder@gmail.com>

Platform: BaseReal-OS — <https://vitalydecoder.github.io/BaseReal-OS/>

> **What changed from v1.** (1) Algorithm B is redefined as a *latent stock variable* that must be measured separately from the visible calm produced by Algorithm A. (2) The Postulate of Discreteness is restated in terms of a discrete *phase label*, which covers first-order, continuous (symmetry-breaking) and topological transitions. (3) A new Section 5 sets the architecture against topological phase transitions (Berry curvature and the Chern number), the Kibble–Zurek mechanism, Landau–Zener transitions and measurement-induced entanglement transitions, each with explicit limits. (4) The VIX test of v1 is audited and re-run ex ante on every VIX spike from 1990 to 2026 against a surrogate null. The v1 result does not survive. (5) Section 9 states falsifiable predictions and records one domain (seismology) where a close relative of the model's central prediction has already failed. (6) The historical examples and references have been corrected.

## Abstract

This paper proposes a two-process description of threshold transitions in physical, biological, economic and cognitive systems. **Algorithm A** is a restoring, structure-preserving process (an attractor). **Algorithm B** is a process that accumulates deviation potential while A holds the structure. A transition occurs when the cost of holding the structure exceeds the cost of reorganising it. The architecture has well-known ancestors: catastrophe theory, synergetics, self-organised criticality, Minsky's financial-instability hypothesis, and the early-warning-signals programme. The paper does not claim a new physical mechanism. It claims a shared *architecture* that can be stated operationally and tested.

Version 2 makes three contributions:

1. **B as a latent stock.** Following evidence that prolonged low volatility predicts banking crises through credit build-up [Danielsson et al. 2018], B is treated as a stock that is *not* visible in the noise A suppresses. Measuring calm is not measuring B.
2. **A wider transition class.** The architecture is set against topological transitions (where an integer invariant can change only when a gap closes), the Kibble–Zurek mechanism (where the rate of passage through a critical point sets the residue left behind), Landau–Zener transitions, and measurement-induced entanglement transitions in monitored quantum circuits. In the last of these, a structure-destroying process (unitary scrambling) and a structure-imposing process (measurement) compete, and a sharp transition occurs at a critical measurement rate. Every analogy is bounded explicitly. None of them bears on hidden variables or on any effect of human intention on physical systems.
3. **An honest empirical audit.** The v1 test on the CBOE VIX index reported a significant asymmetry between "endogenous" and "exogenous" events (p ≈ 0.029, n = 4 + 4). Re-analysis shows that this result depends on mixing two definitions of calm and on the volatility regime of each era. Under a regime-relative definition, p ≈ 0.89. An ex-ante, classification-free test on all 40 VIX spikes from 1990 to 2026 finds no relation between the length of the preceding calm and the size of the spike (for relative spike size, Spearman ρ from −0.02 to +0.12 across three definitions of calm; every correlation, including one mechanical artefact, falls inside a surrogate null band). This is read as evidence that VIX measures A's output, not B's stock.

The conditional-intent operator (IF→THEN) is retained as a cognitive-level hypothesis, consistent with meta-analytic evidence on implementation intentions [Gollwitzer & Sheeran 2006]. It is not offered as a physical mechanism.

## 1. Introduction

Threshold transitions are described in many fields with different mathematics:

- avalanche breakdown in semiconductors [McKay 1954];
- the neuronal action potential [Hodgkin & Huxley 1952];
- catastrophe theory [Thom 1972] and synergetics [Haken 1977];
- dissipative structures [Prigogine & Stengers 1984];
- self-organised criticality (SOC) [Bak, Tang & Wiesenfeld 1987];
- spin glasses [Parisi 1983];
- early warning signals of critical transitions [Scheffer et al. 2009];
- endogenous versus exogenous crashes in finance [Johansen & Sornette 2010];
- "stability is destabilising" in macro-finance [Minsky 1986; Danielsson et al. 2018];
- topological phase transitions [Kosterlitz & Thouless 1973; Thouless et al. 1982], recognised by the 2016 Nobel Prize in Physics.

This paper proposes a common vocabulary: two coupled processes and one control coefficient. The aim is modest. A shared architecture is useful only if it

- (a) can be stated so that it could be wrong,
- (b) says which observable measures which process, and
- (c) predicts something its predecessors do not.

Version 1 did not meet (b) or (c). Version 2 tries to.

Two prior programmes deserve special mention because v1 understated them.

- **Johansen and Sornette.** They classified large drawdowns in world markets as endogenous (preceded by log-periodic power-law bubble signatures) or exogenous (attributable to a news shock). Over the markets they analysed, they identified 49 outliers: 25 endogenous, 22 exogenous and 2 associated with the Japanese anti-bubble [Johansen & Sornette 2010]. The endogenous/exogenous distinction used in v1 is therefore theirs, and on a far larger sample.
- **Danielsson, Valenzuela and Zer.** With a database spanning up to 211 years and 60 countries, they showed that prolonged low volatility predicts banking crises in and out of sample, while the level of volatility does not [Danielsson et al. 2018]. Section 8 shows why this distinction (calm as a cause of build-up, not as its measure) matters for the present model.

## 2. The two-process model

### 2.1 Algorithm A — the restoring process

Algorithm A minimises the cost of maintaining a configuration and resists deviations from it. Examples:

- the crystal lattice;
- ion pumps holding a resting membrane potential;
- homeostasis;
- institutional inertia;
- habit.

Formally, A is an attractor: the state $S$ relaxes toward a minimum of a potential $V(S)$ at a recovery rate $\lambda > 0$.

### 2.2 Algorithm B — the accumulating process (revised)

In v1, B was "a stochastic generator whose signal grows with the duration of stagnation". Version 2 separates two things that v1 conflated:

- **Fluctuations** — the noise around the attractor, which A suppresses and which observers see.
- **Stock** — a latent quantity $B(t)$ that accumulates while A holds the configuration and that shifts the location of the threshold. Examples: leverage and credit in a financial system, inert core mass in a star, kinetic energy of carriers between collisions, depolarising charge on a membrane.

The revised postulate is:

> **B is a stock, not a noise level.** Its growth may be fed by the very calm that A produces (as with leverage under low volatility), so the visible calm of a system is at best an *input* to B and never a *measurement* of it.

This makes a testable distinction. A model that measures B by the duration of calm (as v1 did) predicts that calm duration predicts the transition. A model that treats B as a separate stock predicts that calm duration predicts the transition only through the stock. When the stock is not observed, calm may have little or no predictive value. Section 8 finds the latter for daily VIX.

### 2.3 The control coefficient $\alpha$ (operationalised)

The state is summarised as

$$P(t) = \alpha \cdot A(S) + (1-\alpha) \cdot B(t), \qquad \alpha \in [\varepsilon,\ 1-\varepsilon],\ \varepsilon = 10^{-5}.$$

In v1, $\alpha$ had no operational definition and the bifurcation was placed at $\alpha \approx 0.5$ without justification. Version 2 proposes a definition through critical slowing down. Near a fold bifurcation, the recovery rate $\lambda$ tends to zero and the lag-1 autocorrelation of fluctuations $\rho_1 = e^{-\lambda \Delta t}$ tends to one [Scheffer et al. 2009; Dakos et al. 2008]. Hence

$$\hat\alpha(t) = \operatorname{clip}\big(1 - \hat\rho_1(t),\ \varepsilon,\ 1 - \varepsilon\big),$$

with $\hat\rho_1$ estimated in a rolling window.

- A strongly restoring system has $\hat\alpha$ near its maximum.
- A system approaching a fold has $\hat\alpha$ falling toward a critical value $\alpha_c$.

$\alpha_c$ is system-specific and must be estimated, not assumed. The value 0.5 is withdrawn.

Two cautions from the early-warning literature apply directly:

- Some transitions give no warning at all, in particular noise-induced transitions between basins [Ditlevsen & Johnsen 2010; Boettiger & Hastings 2012a].
- Selecting systems because they are already known to have transitioned produces false positives: the prosecutor's fallacy [Boettiger & Hastings 2012b].

### 2.4 The Postulate of Discreteness (restated)

Version 1 claimed that the state $S$ always jumps with "no stable intermediate configuration". That claim fails for continuous (second-order) transitions. The laser threshold, for example, is formally analogous to a second-order phase transition: the order parameter (the coherent field amplitude) grows continuously from zero above threshold [DeGiorgio & Scully 1970; Haken 1975]. Version 2 restates the postulate in terms of a **phase label** $L$, a discrete characterisation of which phase the system is in:

| Transition type | What is continuous | What is discrete | Example |
|---|---|---|---|
| First-order | control parameter | order parameter jumps; phase label | boiling, fold catastrophes, all-or-none spike |
| Continuous (second-order) | control parameter and order parameter | symmetry of the state (broken / unbroken) | laser threshold, ferromagnet at $T_c$ |
| Topological | control parameter, local curvature | an integer invariant (e.g. Chern number $C$) | quantum Hall plateaus, Chern insulators |

> **Postulate of Discreteness (v2).** A smooth change in the control parameter produces a discrete change in the phase label $L$ at a critical point. Between labels, no stable intermediate *label* exists, even when some continuous quantity passes through intermediate values.

The original postulate survives intact for first-order and catastrophe-type transitions. For the other two classes, discreteness is a property of the label, not of every observable.

## 3. "Randomness" relocated, not annulled

Version 1 claimed to "annul randomness as an explanatory principle". This is too strong. The model does not remove stochasticity. It assigns stochasticity to the *timing* of the trigger while treating the *accumulation* that makes a trigger effective as structured.

SOC already provides a mechanistic account of why driven threshold systems produce avalanches of all sizes. In the classic SOC models, however, the size of the next avalanche carries little memory of the waiting time. The architecture proposed here differs precisely there: it asserts memory in the stock $B$. Section 9 turns this into a prediction.

## 4. Classical examples (corrected)

**Avalanche breakdown.**
- Carriers gain energy between collisions with the lattice (B); the lattice holds (A).
- Above a critical field, impact ionisation creates new carriers, which are themselves accelerated: an exponential cascade [McKay 1954].

**Action potential.**
- Synaptic input depolarises the membrane (B); leak and pumps hold the resting potential (A).
- At threshold, voltage-gated sodium channels open regeneratively [Hodgkin & Huxley 1952].
- "All-or-none" is an approximation. Threshold behaviour differs between classes of excitability, but the spike is a robust first-order-like event.

**Laser threshold.** Pumping accumulates population inversion (B). Above threshold, stimulated emission dominates. As noted in Section 2.4, this is a continuous transition in the order parameter with a discrete change of label (incoherent → coherent). The maser/laser work of Basov and Prokhorov (Nobel Prize 1964) is the historical anchor.

**Dissipative structures.** Far from equilibrium, open systems form ordered structures through bifurcations; the Belousov–Zhabotinsky reaction is the standard example [Prigogine & Stengers 1984].

**Stellar core collapse.**
- Shell burning deposits inert iron mass in the core (B, literally a stock); electron-degeneracy pressure holds it (A).
- Near the Chandrasekhar mass the core collapses [Chandrasekhar 1931].
- The revival of the stalled shock into an explosion remains an active research problem; neutrino heating is the leading hypothesis [Bethe & Wilson 1985]. The example supports accumulation-and-threshold, not a solved cascade.

**Punctuated equilibrium.** Long stasis and rapid speciation [Eldredge & Gould 1972]. Here the identification of B (neutral variation plus environmental pressure) is loose and should be read as illustrative.

**Insight.**
- Insight solutions are preceded by a burst of gamma-band EEG activity over the right anterior temporal lobe beginning about 0.3 s before the response.
- They are also preceded by an earlier increase in alpha activity over right posterior cortex, interpreted as gating of visual input [Jung-Beeman et al. 2004; Kounios & Beeman 2014].
- This replaces the v1 citation, which concerned artists and non-artists rather than insight.
- The alpha-then-gamma sequence is a natural "hold, then release" signature, but it is correlational.

## 5. Topological and quantum transitions: where the architecture holds and where it stops

This section is new. Its purpose is to test the two-process architecture against transitions whose physics is understood exactly, not to borrow prestige from them. Each subsection ends with an explicit limit.

### 5.1 Berry curvature and the Chern number

In a two-dimensional band insulator, each filled band carries a Berry curvature $\Omega_{xy}(\mathbf k)$ over the Brillouin zone [Berry 1984]. Its integral over the whole torus is an integer, the Chern number:

$$C = \frac{1}{2\pi}\int_{\mathrm{BZ}} \Omega_{xy}(\mathbf k)\, d^2k \in \mathbb Z,$$

which fixes the quantised Hall conductance $\sigma_{xy} = C\, e^2/h$ [Thouless et al. 1982; Haldane 1988; Hasan & Kane 2010]. The parameters of the Hamiltonian can be changed continuously, but $C$ can change only when the energy gap closes.

| Feature | Chern / Berry | Duet of Algorithms |
|---|---|---|
| Structure that holds | the energy gap | the attractor maintained by A |
| What accumulates under it | local Berry curvature (geometric phase) | the stock B |
| Local vs global | curvature is local; $C$ is a global integral | B accumulates locally; the threshold is a system-wide property |
| Smooth control, discrete label | continuous parameters, integer $C$ | continuous $\alpha$, discrete label $L$ |
| How the label changes | only through gap closing (a singular point) | only through the critical point $\alpha_c$ |
| After the change | a new stable phase with a different $C$ | a new attractor; the cycle restarts |

**Limits.**
- (i) Berry curvature is a geometric property of wavefunctions, not a stock that grows *in time*. The analogy concerns the *architecture of protection* (a label that cannot change smoothly), not accumulation dynamics.
- (ii) The Chern number is a rigorous invariant; the present model is phenomenological.
- (iii) Identifying Berry curvature with "potential B" would be a category error.

The defensible statement is narrow: *both systems display a discrete label that is protected against smooth deformation and can change only through a singular point.*

### 5.2 A classical topological transition: Kosterlitz–Thouless

The Berezinskii–Kosterlitz–Thouless transition in two-dimensional systems shows that topological transitions need not be quantum [Kosterlitz & Thouless 1973]:

- Below $T_{KT}$, vortices and antivortices exist only as bound pairs.
- Above it, the entropy gain of free vortices exceeds their energy cost, and pairs unbind.

The architecture applies more literally here than in 5.1:

- Thermal excitation populates pairs (B).
- Binding energy holds them (A).
- The transition occurs when the free-energy balance reverses, which is the v1 criterion of "cost of holding > cost of reorganising".

This example matters because it carries the topological framing into the classical domain, where the model's claims are made.

### 5.3 Rate matters: the Kibble–Zurek mechanism

As a system approaches a continuous transition, its relaxation time diverges (critical slowing down). If the control parameter is swept at a finite rate:

- the system cannot follow and "freezes out" at some distance from the critical point;
- it is left with a density of defects that scales as a power of the sweep rate [Kibble 1976; Zurek 1985];
- faster sweeps leave more defects.

The quantum version has been verified on a programmable Rydberg-atom simulator by measuring the growth of spatial correlations while crossing an Ising-type quantum phase transition at variable speeds [Keesling et al. 2019].

Relevance: v1's "time-compression effect" claimed that the density of internal events accelerates the approach to transition. Kibble–Zurek supplies the rigorous version of a related idea. **The rate at which a system is driven through its critical region determines what it carries into the new phase.** This links the early-warning programme (critical slowing down) to the residue of a transition, which v1 did not address.

**Limit.** Kibble–Zurek concerns continuous transitions and defect formation. It does not show that faster internal iteration brings a transition *sooner*.

### 5.4 Adiabatic versus diabatic passage: Landau–Zener

When two energy levels with coupling $\Delta$ are swept through an avoided crossing at rate $v = |d(E_1 - E_2)/dt|$, the probability of a diabatic jump (failing to follow the instantaneous ground state) is

$$P_{\mathrm{jump}} = \exp\!\left(-\frac{2\pi \Delta^2}{\hbar\, v}\right)$$

[Landau 1932; Zener 1932].

This is the simplest exact model of the paper's central control question: whether a structure is carried through a change of conditions or abandoned depends on the ratio of the restoring scale ($\Delta$, the "strength of A") to the rate of change.

**Limit.** Landau–Zener describes a two-level quantum system. Its use here is as an exactly solvable template, not as evidence about markets or minds.

### 5.5 Measurement versus scrambling: measurement-induced entanglement transitions

The closest quantum analogue of the duet is found in monitored quantum circuits. Two processes compete:

- Unitary interactions spread entanglement through a many-qubit system. This is the chaotic, structure-dissolving process.
- Local measurements remove entanglement. This is the structure-imposing process.

As the measurement rate $p$ is varied continuously, the steady state switches sharply at a critical rate $p_c$ between a volume-law (entangling) phase and an area-law (disentangling) phase [Li, Chen & Fisher 2018; Skinner, Ruhman & Nahum 2019]. At the extreme of very frequent measurement, the dynamics freezes, a many-body cousin of the quantum Zeno effect [Misra & Sudarshan 1977].

The transition has now been observed experimentally:

- on trapped ions [Noel et al. 2022];
- on superconducting qubits with mid-circuit readout, where data collapse of the entanglement entropy demonstrated critical behaviour [Koh et al. 2023];
- on up to 70 superconducting qubits using a space-time duality mapping [Google Quantum AI and Collaborators 2023].

| Duet element | Monitored circuit |
|---|---|
| Algorithm B (deviation, mixing) | unitary scrambling, entanglement growth |
| Algorithm A (restoring, ordering) | local projective measurement |
| Control coefficient $\alpha$ | measurement rate $p$ |
| Critical value $\alpha_c$ | critical rate $p_c$ |
| Discrete label | volume-law vs area-law phase |

**Limits.**
- (i) The transition lives in the entanglement structure of individual measurement trajectories. Detecting it requires either exponentially costly post-selection or decoding against classical simulation [Google Quantum AI and Collaborators 2023]. It is not visible in ordinary averaged observables.
- (ii) "Measurement" here means a physical interaction with an apparatus. It is not an observer's attention or intention. Nothing in this literature supports any claim that conscious intent acts on physical systems, and this paper makes no such claim.
- (iii) The result says nothing about hidden variables.

### 5.6 What Section 5 does and does not establish

It establishes that the two-process architecture (a holding process, a dissolving or accumulating process, a continuous control, a discrete label, a critical point) appears in transitions whose physics is exact:

- topological transitions in both quantum (Chern) and classical (Kosterlitz–Thouless) systems;
- rate-dependent passage (Kibble–Zurek, Landau–Zener);
- measurement-induced entanglement transitions.

It does *not* establish that the same mechanism operates in markets, organisms or minds. It also does not extend the determinism/indeterminism synthesis of Section 10 to the quantum domain.

## 6. Controlling the critical point (corrected)

| Strategy | Mechanism in the model | Example |
|---|---|---|
| Raise the threshold | strengthen A; reduce sensitivity to triggers | dynamite; antibiotics |
| Forced pause | interrupt the run-up to let information re-equilibrate | market-wide circuit breakers |
| Balance near criticality | continuous feedback on $\alpha$, made possible by a slow channel | nuclear reactor control |

**Dynamite and the fuse (corrected).**
- Nobel stabilised nitroglycerin in kieselguhr, patenting dynamite in 1867, which raised the trigger threshold by orders of magnitude.
- The reliable initiating element was his blasting cap (mid-1860s).
- The slow-burning *safety fuse*, whose delay is literally measured in length, was invented earlier, by William Bickford in 1831.

Version 1 attributed the fuse to Nobel and conflated the safety fuse with detonating cord; both errors are corrected here. The pairing still illustrates the strategy: a stabilised charge plus a channel that delivers the trigger along a predetermined path and timetable.

**Antibiotics.** Penicillin inhibits bacterial cell-wall synthesis, suppressing the exponential growth process directly rather than only strengthening the host's restoring response.

**Circuit breakers (corrected).**
- In March 2020 the US market-wide circuit breaker was triggered four times (9, 12, 16 and 18 March), each time at Level 1 (a 7% decline) with a 15-minute pause. Level 2 (13%) was never reached.
- The industry working group that reviewed these events concluded that the halts worked as intended and appear to have calmed volatility without causing harm [MWCB Working Group 2021].
- China's circuit breaker, introduced on 4 January 2016, was triggered on 4 and 7 January. On 7 January trading lasted under half an hour, and the regulator suspended the mechanism after four days [CSRC announcement, 7 January 2016].
- Theory predicts both outcomes. Halts can help a market absorb large volume shocks [Greenwald & Stein 1991]. They can also produce a "magnet effect": as the price approaches the trigger, volatility rises and the probability of triggering accelerates [Subrahmanyam 1994; Chen, Petukhov, Wang & Xing 2024].

In model terms, a pause raises $\alpha$ temporarily, but a *visible* threshold can itself feed B.

**Reactors (sharpened).** A reactor can be balanced near criticality because a small fraction of fission neutrons (about 0.65% for U-235) is emitted with delays of seconds rather than microseconds. These delayed neutrons stretch the system's time constant into a range where control rods can act [Hetrick 1993]. The general lesson for the model: **control near criticality requires a slow component in the dynamics.** Without one, balancing degenerates into either suppression or runaway.

## 7. Conditional intent as a directing operator (cognitive level)

### 7.1 Two levels of goal-setting

1. **Unconditional intent** holds focus on a goal. In model terms it reinforces A during the holding phase and is blind to the transition.
2. **Conditional intent** has the form "IF trigger X occurs → THEN do Y". It specifies in advance what to do when the transition comes and so pre-structures the channels along which the released potential will flow.

The structure is borrowed from implementation intentions [Gollwitzer 1999]. A meta-analysis of 94 independent tests found a medium-to-large effect on goal attainment (d ≈ 0.65) [Gollwitzer & Sheeran 2006]. The mechanism proposed there is delegation of control to situational cues, so that no fresh act of will is needed at the moment of action.

### 7.2 The IF→THEN chain as a cascade map

A chain "IF A → THEN B → which opens C → …" gives a controller a route with checkpoints rather than a destination. The fuse of Section 6 is its physical template: the channel is laid before ignition.

### 7.3 Status of the claim

The evidence for conditional intent concerns human action planning. Priming lowers thresholds for subsequent activation in memory systems [Tulving & Schacter 1990]. That makes a cognitive version of "pre-laid channels" plausible, but it does not demonstrate that conditional intent directs avalanches in any system other than the person forming it. The parallels with *kavvanah*, *niyyah* and Buddhist notions of intention are cultural and metaphorical. They are kept because they motivate the question, not as evidence.

## 8. Empirical re-analysis: what the VIX data do and do not show

### 8.1 Audit of the v1 test

Version 1 compared four "endogenous" events with four "exogenous" ones using "the number of consecutive days with VIX below 15 within the 90-day window preceding the event". Re-computing the reported values from the daily CBOE VIX closing series (1990-01-02 to 2026-09-22, 9,278 observations) shows that they were produced by **two different definitions**:

- 136 days (February 2007) and 115 days (February 2018) are unbounded streaks ending at the event. They cannot occur inside a 90-day window.
- 23 days (August 2015) and 55 days (August 2024) are the longest streaks *inside* the 90-day window.
- The March 2026 event, recorded as 0, has an 11-day streak inside its window.
- The event labelled "2007 Global Financial Crisis" is in fact 27 February 2007 (the Shanghai sell-off and early subprime stress). The September 2008 spike was preceded by a year of elevated volatility, not calm.

Applying each definition consistently to all eight events:

| Definition of calm | Endogenous (2007, 2018, 2015, 2024) | Exogenous (1998, 2001, 2010, 2026) | Exact Mann–Whitney p |
|---|---|---|---|
| Unbounded streak below 15 ending at event | 136, 115, 10, 0 | 0, 0, 0, 0 | 0.114 |
| Longest streak below 15 in 90-day window | 90, 90, 23, 55 | 0, 0, 0, 11 | 0.029 |
| Regime-relative: share of 90 days below own trailing-year 25th percentile | 0.82, 0.56, 0.20, 0.48 | 0.32, 0.26, 0.82, 0.24 | 0.886 |

The result is significant under one definition only, and it disappears entirely when calm is measured relative to each era's own volatility regime. The cause is visible in the data. Before the 1998, 2001 and 2010 events the VIX stood at about 34, 32 and 25, so a fixed threshold of 15 was unreachable regardless of how calm those markets were by their own standards. The fixed threshold measures the regime, not the trigger. Because the eight events were chosen after the fact from known crises, the comparison is also exposed to the prosecutor's fallacy [Boettiger & Hastings 2012b].

### 8.2 Ex-ante test on all spikes

To remove selection, every VIX spike from 1990 to 2026 was identified by a fixed rule:

- the closing value reaches at least 1.6 times its minimum over the previous 20 trading days;
- onsets are at least 63 trading days apart.

This yields 40 spikes, including 1998, 2001, September 2008, 2010, August 2011, February 2018, February 2020, August 2024, April 2025 and March 2026.

For each spike, calm was measured in the 90 trading days ending 20 days before onset (to exclude the run-up) in three ways:

- (a) days below 15;
- (b) the longest run below the trailing-year 25th percentile;
- (c) low variance of daily log changes.

Spike size was measured as log(peak/base) and as peak − base.

**Surrogate null.** A heterogeneous autoregressive (HAR) model of log VIX [Corsi 2009] was fitted, and 300 synthetic series were generated with block-bootstrapped residuals. The identical pipeline was run on each. The null captures purely mechanical relations, for example that a low base allows a large ratio. Under it, an effect of "accumulated B" has no reason to exist.

| Calm measure | Size measure | Observed ρ | Surrogate 95% band | One-sided p |
|---|---|---|---|---|
| Regime-relative streak | log(peak/base) | −0.02 | [−0.27, +0.30] | 0.59 |
| Days below 15 | log(peak/base) | +0.12 | [−0.27, +0.28] | 0.26 |
| Low variance | log(peak/base) | +0.05 | [−0.28, +0.25] | 0.33 |
| Days below 15 | peak − base | −0.39 | [−0.65, −0.16] | 0.37 |

**No calm measure predicts spike size beyond what the surrogate null produces.** The one nominally significant correlation (days below 15 versus absolute jump, ρ = −0.39) is mechanical: the null produces it on average. Varying the spike threshold (1.5×, 1.8×, 2.0×) does not change the conclusion. For the largest spikes only (2.0×, n = 16), ρ = +0.30 with p = 0.26, a direction worth re-testing on other data, not a finding.

A hazard test asked whether a long regime-relative calm raises the probability of a spike within the next 63 trading days. The top tercile of calm had a spike rate 1.24 times that of the bottom tercile, against a surrogate mean of 1.18 (120 surrogates; 95% band 0.68–1.84; p = 0.35). No evidence either way.

### 8.3 Interpretation

The daily VIX record does not support the v1 claim that the duration of calm measures accumulated avalanche potential. Two readings remain:

1. **B is not accumulated at all** in this system at this time scale. Volatility spikes are better described by a memoryless or short-memory process.
2. **B accumulates in a stock that VIX does not observe.** Danielsson et al. find that the link from low volatility to crises runs through credit and leverage build-up over years, and that volatility itself does not predict crises [Danielsson et al. 2018]. Diks, Hommes and Wang find statistical evidence of critical slowing down before Black Monday 1987, but mixed or insignificant results for later crises [Diks, Hommes & Wang 2019].

Reading 2 is the one built into the revised Section 2.2. It is also the reason v2 no longer treats calm as a measurement of B. It makes a sharper prediction than v1: **the stock variable (credit-to-GDP gap, leverage, margin debt), not the calm, should predict the size and hazard of endogenous transitions, and calm should add nothing once the stock is controlled for.**

### 8.4 Protocol for the next test (fixed in advance)

- **Data.** Cross-country credit-to-GDP gaps and equity-market volatility (annual and quarterly); daily VIX and margin debt for the US.
- **Events.** All banking and stock-market crises in an existing chronology. No hand selection.
- **Hypotheses.**
  - H1: a stock measure predicts crisis size and hazard.
  - H2: calm adds no predictive value conditional on the stock.
  - H3 (v1's claim, expected to fail): calm predicts without the stock.
- **Null.** Surrogates with matched autocorrelation; out-of-sample evaluation.
- **Code.** The script used for Section 8 (data from the public CBOE series as mirrored by the `datasets/finance-vix` repository) will be published on the platform page.

## 9. Falsifiable predictions

**P1 — Memory in the stock.** Where B can be measured directly, the size or hazard of the next transition increases with the accumulated stock since the last transition. SOC-type models predict little such memory.

A cautionary precedent exists. In seismology, the time- and slip-predictable models encode exactly this kind of memory: elastic strain accumulates and is released. Tests on repeating earthquakes in California, Taiwan and Japan, and on laboratory stick-slip, found that these models predict event-to-event behaviour *worse* than models with fixed recurrence or fixed slip. The one exception is a correlation between slip and preceding recurrence time in some Parkfield sequences, not found elsewhere [Rubinstein et al. 2012]. The architecture must therefore specify, for each system, why its stock is not reset or redistributed by unobserved processes. Otherwise P1 will fail as the elastic-rebound version did.

**P2 — Rate dependence.** Driving a system faster through its critical region leaves more residual disorder after the transition (Kibble–Zurek). For cognitive or organisational systems this predicts that abrupt forced reorganisations leave more unresolved "defects" than gradual ones crossing the same threshold. This is testable in, for example, lab learning tasks with controlled pacing.

**P3 — Visible thresholds attract.** Announced thresholds raise volatility as they are approached (the magnet effect). Hidden or randomised thresholds should show weaker attraction.

**P4 — Conditional intent.** IF→THEN plans improve outcomes specifically when the trigger occurs, and should show little benefit when it does not. Insight should be preceded by alpha-band gating, then a gamma burst.

**P5 — Slow channel.** Systems with no slow component near criticality (no analogue of delayed neutrons) cannot be held at criticality by feedback. Attempts to do so should produce either suppression or runaway.

## 10. Determinism and indeterminism (limited synthesis)

For macroscopic classical dissipative systems the model offers a division of labour:

- A is predictable within a configuration.
- The *timing* of the trigger is probabilistic.
- The *fact* of the transition follows from accumulation, when B is a real stock.

In that restricted sense, Einstein's and Bohr's intuitions describe different components of one dynamics.

This synthesis does not extend to quantum mechanics. Bell-inequality violations [Bell 1964; Aspect, Dalibard & Roger 1982] have been confirmed in loophole-free tests [Hensen et al. 2015] and were recognised by the 2022 Nobel Prize in Physics. They rule out local hidden-variable models. The quantum systems of Section 5 instantiate the two-process *architecture* (Section 5.5 most directly) within standard quantum mechanics. They do not supply hidden determinism, and the paper claims none.

## 11. Limitations and open questions

1. **Operationalising B.** For each system class, which observable is the stock? Without an answer the model is not testable, as Section 8 shows.
2. **Estimating $\alpha_c$.** The AR(1)-based $\hat\alpha$ is one candidate. Its validity depends on the bifurcation type, and some transitions give no warning [Boettiger & Hastings 2012a].
3. **Novelty.** What the architecture adds beyond catastrophe theory, synergetics, SOC, Sornette's endogenous/exogenous taxonomy and the early-warning programme must be shown through P1–P5, not asserted.
4. **Directionality of conditional intent.** Evidence exists for individual action. Any extension to collective or physical systems is untested.
5. **System boundaries.** An "exogenous" shock to a market may be endogenous to a larger system. Testing this requires defining the larger system and its stock variable in advance (unchanged from v1).
6. **Quantum scope.** Measurement-induced transitions offer a rigorous two-process template. Whether anything beyond the architecture carries over to classical systems is open.

## 12. Conclusion

Version 2 keeps the core intuition of v1: stable structures can hide the build-up that ends them, and transitions can be steered without being prevented. It changes how the intuition is stated and tested:

1. B is a latent stock, distinct from the calm that A produces. Calm can feed B but does not measure it.
2. Discreteness belongs to the phase label. This brings continuous and topological transitions inside the architecture.
3. The architecture appears in exactly solvable or experimentally verified quantum and topological settings: Chern insulators, Kosterlitz–Thouless, Kibble–Zurek, Landau–Zener and, most closely, measurement-induced entanglement transitions. The limits are stated, and no claim is made about hidden variables or about intention acting on matter.
4. The v1 VIX result does not survive an ex-ante, regime-relative, surrogate-controlled re-analysis. The negative result is reported in full, and a pre-specified test on stock variables is proposed in its place.
5. The conditional-intent operator stands as a cognitive-level hypothesis with meta-analytic support for its human form.

The author invites replication and criticism, especially of P1, the prediction most likely to fail.

## Data and code

Daily CBOE VIX history (open, high, low, close), 1990-01-02 to 2026-09-22, 9,278 trading days, as mirrored in the public `datasets/finance-vix` repository from the CBOE series [CBOE]. Analysis code (Python: event audit, spike detection, HAR surrogate generation, hazard test) accompanies this version.

## References

- Aspect, A., Dalibard, J., & Roger, G. (1982). Experimental test of Bell's inequalities using time-varying analyzers. *Physical Review Letters*, 49(25), 1804–1807.
- Bak, P., Tang, C., & Wiesenfeld, K. (1987). Self-organized criticality: An explanation of the 1/f noise. *Physical Review Letters*, 59(4), 381–384.
- Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika*, 1(3), 195–200.
- Berry, M. V. (1984). Quantal phase factors accompanying adiabatic changes. *Proceedings of the Royal Society A*, 392, 45–57.
- Bethe, H. A., & Wilson, J. R. (1985). Revival of a stalled supernova shock by neutrino heating. *Astrophysical Journal*, 295, 14–23.
- Boettiger, C., & Hastings, A. (2012a). Quantifying limits to detection of early warning for critical transitions. *Journal of the Royal Society Interface*, 9(75), 2527–2539.
- Boettiger, C., & Hastings, A. (2012b). Early warning signals and the prosecutor's fallacy. *Proceedings of the Royal Society B*, 279, 4734–4739. https://doi.org/10.1098/rspb.2012.2085
- CBOE. *VIX Historical Data*. https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv
- Chandrasekhar, S. (1931). The maximum mass of ideal white dwarfs. *Astrophysical Journal*, 74, 81–82.
- Chen, H., Petukhov, A., Wang, J., & Xing, H. (2024). The dark side of circuit breakers. *Journal of Finance*, 79(2), 1405–1455. https://doi.org/10.1111/jofi.13310
- Corsi, F. (2009). A simple approximate long-memory model of realized volatility. *Journal of Financial Econometrics*, 7(2), 174–196.
- CSRC (China Securities Regulatory Commission) (2016). Announcement suspending the index circuit-breaker mechanism, 7 January 2016.
- Dakos, V., Scheffer, M., van Nes, E. H., Brovkin, V., Petoukhov, V., & Held, H. (2008). Slowing down as an early warning signal for abrupt climate change. *PNAS*, 105(38), 14308–14312.
- Danielsson, J., Valenzuela, M., & Zer, I. (2018). Learning from history: Volatility and financial crises. *Review of Financial Studies*, 31(7), 2774–2805. https://doi.org/10.1093/rfs/hhy049
- DeGiorgio, V., & Scully, M. O. (1970). Analogy between the laser threshold region and a second-order phase transition. *Physical Review A*, 2(4), 1170–1177.
- Diks, C., Hommes, C., & Wang, J. (2019). Critical slowing down as an early warning signal for financial crises? *Empirical Economics*, 57(4), 1201–1228. https://doi.org/10.1007/s00181-018-1527-3
- Ditlevsen, P. D., & Johnsen, S. J. (2010). Tipping points: Early warning and wishful thinking. *Geophysical Research Letters*, 37, L19703.
- Eldredge, N., & Gould, S. J. (1972). Punctuated equilibria: An alternative to phyletic gradualism. In T. J. M. Schopf (Ed.), *Models in Paleobiology* (pp. 82–115). Freeman Cooper.
- Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple plans. *American Psychologist*, 54(7), 493–503.
- Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis of effects and processes. *Advances in Experimental Social Psychology*, 38, 69–119.
- Google Quantum AI and Collaborators (2023). Measurement-induced entanglement and teleportation on a noisy quantum processor. *Nature*, 622, 481–486. https://doi.org/10.1038/s41586-023-06505-7
- Greenwald, B. C., & Stein, J. C. (1991). Transactional risk, market crashes, and the role of circuit breakers. *Journal of Business*, 64(4), 443–462.
- Haken, H. (1975). Cooperative phenomena in systems far from thermal equilibrium and in nonphysical systems. *Reviews of Modern Physics*, 47(1), 67–121.
- Haken, H. (1977). *Synergetics: An Introduction*. Springer.
- Haldane, F. D. M. (1988). Model for a quantum Hall effect without Landau levels. *Physical Review Letters*, 61(18), 2015–2018.
- Hasan, M. Z., & Kane, C. L. (2010). Colloquium: Topological insulators. *Reviews of Modern Physics*, 82(4), 3045–3067.
- Hensen, B., et al. (2015). Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. *Nature*, 526, 682–686.
- Hetrick, D. L. (1993). *Dynamics of Nuclear Reactors*. American Nuclear Society.
- Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500–544.
- Johansen, A., & Sornette, D. (2010). Shocks, crashes and bubbles in financial markets. *Brussels Economic Review*, 53(2), 201–253. (arXiv: cond-mat/0210509, "Endogenous versus exogenous crashes in financial markets".)
- Jung-Beeman, M., Bowden, E. M., Haberman, J., Frymiare, J. L., Arambel-Liu, S., Greenblatt, R., Reber, P. J., & Kounios, J. (2004). Neural activity when people solve verbal problems with insight. *PLoS Biology*, 2(4), e97. https://doi.org/10.1371/journal.pbio.0020097
- Keesling, A., et al. (2019). Quantum Kibble–Zurek mechanism and critical dynamics on a programmable Rydberg simulator. *Nature*, 568, 207–211. https://doi.org/10.1038/s41586-019-1070-1
- Kibble, T. W. B. (1976). Topology of cosmic domains and strings. *Journal of Physics A*, 9(8), 1387–1398.
- Koh, J. M., Sun, S.-N., Motta, M., & Minnich, A. J. (2023). Measurement-induced entanglement phase transition on a superconducting quantum processor with mid-circuit readout. *Nature Physics*, 19, 1314–1319.
- Kosterlitz, J. M., & Thouless, D. J. (1973). Ordering, metastability and phase transitions in two-dimensional systems. *Journal of Physics C*, 6(7), 1181–1203.
- Kounios, J., & Beeman, M. (2014). The cognitive neuroscience of insight. *Annual Review of Psychology*, 65, 71–93.
- Landau, L. D. (1932). Zur Theorie der Energieübertragung II. *Physikalische Zeitschrift der Sowjetunion*, 2, 46–51.
- Li, Y., Chen, X., & Fisher, M. P. A. (2018). Quantum Zeno effect and the many-body entanglement transition. *Physical Review B*, 98, 205136.
- McKay, K. G. (1954). Avalanche breakdown in silicon. *Physical Review*, 94(4), 877–884.
- Minsky, H. P. (1986). *Stabilizing an Unstable Economy*. Yale University Press.
- Misra, B., & Sudarshan, E. C. G. (1977). The Zeno's paradox in quantum theory. *Journal of Mathematical Physics*, 18(4), 756–763.
- MWCB Working Group (2021). *Report of the Market-Wide Circuit Breaker Working Group Regarding the March 2020 MWCB Events* (submitted 31 March 2021; filed with the SEC).
- Noel, C., et al. (2022). Measurement-induced quantum phases realized in a trapped-ion quantum computer. *Nature Physics*, 18, 760–764.
- Parisi, G. (1983). Order parameter for spin-glasses. *Physical Review Letters*, 50(24), 1946–1948.
- Prigogine, I., & Stengers, I. (1984). *Order Out of Chaos: Man's New Dialogue with Nature*. Bantam Books.
- Rubinstein, J. L., Ellsworth, W. L., Chen, K. H., & Uchida, N. (2012). Fixed recurrence and slip models better predict earthquake behavior than the time- and slip-predictable models: 1. Repeating earthquakes. *Journal of Geophysical Research*, 117, B02306. https://doi.org/10.1029/2011JB008724
- Scheffer, M., Bascompte, J., Brock, W. A., Brovkin, V., Carpenter, S. R., Dakos, V., Held, H., van Nes, E. H., Rietkerk, M., & Sugihara, G. (2009). Early-warning signals for critical transitions. *Nature*, 461, 53–59.
- Skinner, B., Ruhman, J., & Nahum, A. (2019). Measurement-induced phase transitions in the dynamics of entanglement. *Physical Review X*, 9, 031009.
- Subrahmanyam, A. (1994). Circuit breakers and market volatility: A theoretical perspective. *Journal of Finance*, 49(1), 237–254.
- Thom, R. (1972). *Structural Stability and Morphogenesis*. W. A. Benjamin.
- Thouless, D. J., Kohmoto, M., Nightingale, M. P., & den Nijs, M. (1982). Quantized Hall conductance in a two-dimensional periodic potential. *Physical Review Letters*, 49(6), 405–408.
- Tulving, E., & Schacter, D. L. (1990). Priming and human memory systems. *Science*, 247, 301–306.
- Zener, C. (1932). Non-adiabatic crossing of energy levels. *Proceedings of the Royal Society A*, 137, 696–702.
- Zurek, W. H. (1985). Cosmological experiments in superfluid helium? *Nature*, 317, 505–508.

*References removed from v1:* Greenwald, Stein & Stiglitz (1989) and Goldstein & Pauzner (2005), which did not support the claims attached to them; Bhattacharya & Petsche (2005), which concerns artists and non-artists rather than insight; Bardeen & Brattain (1948), Basov & Prokhorov (1954) and Burbidge et al. (1957), kept in v1 only as Nobel anchors and now mentioned in the text without bearing any claim.
