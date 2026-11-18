# LT-System v2: A Dimensional System for Near-Realistic Simulations

**Mass as the Field Parameter (M = μ), Electrical Sector and Bernoulli’s Law**  
**Date:** November 2026  
**Author:** Vitali Colesnicenco  
**Independent Researcher, London, England, United Kingdom**  
**Email:** vitalydecoder@gmail.com  
**Based on:** The Inverse 3/2 Law, a geometric interpretation of Kepler's third law (BaseReal-OS Framework)  
https://vitalydecoder.github.io/BaseReal-OS/  
**Previous version:** v1, *Geometrization of Physical Quantities: A Modification of Bartini’s LT-System Based on the Inverse 3/2 Law*, Zenodo, June 2026, https://zenodo.org/records/20788306  
**Status:** An engineering unit system for virtual simulations; not a claim to describe real physics

## Abstract

An updated LT-table is proposed. All quantities are expressed through length L and time T, and each body is set by two numbers: its radius R and the orbital period T at its surface. Version 1 defined mass as pure geometry, M = 4π²R³ (dimension L³). This version returns time to mass: the mass of a body is its field parameter, M = μ = 4π²R³/T² (dimension L³T⁻²), and μ replaces mass in every formula. Three things follow. The gravitational coupling becomes G = 1 (dimensionless), so Newton’s law reads F = M₁M₂/r² with no constant. Density becomes ρ = 3π/T², a function of the body’s own time alone. Real mass ratios and mean densities are reproduced, which a purely geometric mass cannot do. Energy is separated from μ and has dimension L⁵T⁻⁴. The electrical sector is closed under Coulomb’s law without constants and places charge in the same cell as mass. Bernoulli’s law is shown to be written in the table cells as a consequence of classical energy balance. The resulting table coincides with LT-systems in which G is dimensionless (Brown, Bartini); the contribution of this version is the engine-oriented form. The paper lists what is confirmed, what is a convention and what remains open.

## 1. Purpose and Scope

- This is a system of conventions for a simulation engine, not a replacement for SI and not a theory of physics.
- The success criterion is engineering: dimensional consistency, cheap computation, behaviour close to the real world.
- For every statement a status is indicated: **definition** (adopted in the system), **derived** (follows from the definitions and classical mechanics), **convention** (depends on the choice of unit system), **hypothesis** (not proven).

## 2. Core Conventions

- Base quantities: length L, time T.
- **Mass** (definition): M = μ = 4π²R³/T² = ω²R³, dimension L³T⁻². T is the orbital period at the surface of the given body, individual for each body. The mass of a body and its field parameter are one quantity.
- **Gravitational coupling** (consequence of the definition): G = μ/M = 1, dimensionless and universal. Newton’s law is F = M₁M₂/r². The acceleration produced by a body is a = M/r².
- **Density** (derived): ρ = M/V = (4π²R³/T²) / (4/3·πR³) = 3π/T², dimension T⁻². The mean density of a body depends only on its surface period: the body’s time is its density. The classical relation T = √(3π/(Gρ)) becomes the definition of density in the table.
- **Orbits** (derived): P = 2π√(a³/M) = T·(a/R)^{3/2}, the 3/2 law. The field of every body is fully set by R and T.
- **Kilograms** (convention): M[kg] = μ / G_SI, where G_SI = 6.674·10⁻¹¹ m³kg⁻¹s⁻². In this system G_SI is a unit conversion factor, like k_B for temperature. The engine itself never needs kilograms.
- All other quantities are defined by standard formulae (F = M·a, A = F·L, etc.).
- μ is **not** energy. Energy (work) F·L = M·v² has dimension L⁵T⁻⁴.
- **Relation to Brown and Bartini.** When G is dimensionless, the mechanical table is fixed uniquely, and it coincides with the LT-tables of Brown (1941) and Bartini (1965), where mass is L³T⁻². Version 1 modified Bartini’s system by taking T out of mass; this version puts it back. What remains specific to this system is the description of each body by its own R and T, density through T, and the 3/2 law as the working rule of the engine.

**Why time returns to mass.** With the geometric mass of version 1, M = 4π²R³, density is ρ = 4π²R³ / (4/3·πR³) = 3π for every body: all bodies have one and the same density. Calibrated on the Earth, every body receives the Earth’s mean density of 5513 kg/m³. Mars then comes out heavier by 5513/3934 = 1.40, the Sun by 5513/1410 = 3.9, and the Earth/Moon mass ratio from radii is 49.3 instead of the measured 81.3. With M = μ the same 3π is divided by the body’s own T².

## 3. Quantity Table

| Quantity                                 | Formula              | LT     | Status                    |
| ---------------------------------------- | -------------------- | ------ | ------------------------- |
| Length, radius                           | R                    | L¹     | base                      |
| Period                                   | T                    | T¹     | base                      |
| Mass = field parameter μ                 | 4π²R³/T² = ω²R³      | L³T⁻²  | definition                |
| Gravitational coupling G                 | μ/M = 1              | L⁰T⁰   | consequence of definition |
| Velocity                                 | 2πR/T                | L¹T⁻¹  | derived                   |
| Acceleration                             | M/R² = 4π²R/T²       | L¹T⁻²  | derived                   |
| Density                                  | M/V = 3π/T²          | T⁻²    | derived                   |
| Momentum                                 | M·v                  | L⁴T⁻³  | derived                   |
| Force                                    | M·a ; M₁M₂/r²        | L⁴T⁻⁴  | derived                   |
| Angular momentum, action                 | r·M·v ; E·T          | L⁵T⁻³  | derived                   |
| Energy, work, moment of force            | F·L = M·v²           | L⁵T⁻⁴  | derived                   |
| Power                                    | E/T                  | L⁵T⁻⁵  | derived                   |
| Pressure, stress, energy density         | F/A = E/V            | L²T⁻⁴  | derived                   |
| Dynamic viscosity, pressure×time         | p·T = ρ·ν            | L²T⁻³  | derived                   |
| Kinematic viscosity                      | ν                    | L²T⁻¹  | derived                   |
| Specific angular momentum                | r×v                  | L²T⁻¹  | derived                   |
| Specific energy, gravitational potential | ½v², M/r, p/ρ        | L²T⁻²  | derived                   |
| Volume flow rate                         | A·v ~ R³/T           | L³T⁻¹  | derived                   |
| Mass flow rate                           | ρ·A·v                | L³T⁻³  | derived                   |

### Matrix

|         | L⁻¹        | L⁰            | L¹                    | L²                                     | L³                 | L⁴       | L⁵                       |
| ------- | ---------- | ------------- | --------------------- | -------------------------------------- | ------------------ | -------- | ------------------------ |
| **T²**  | inductance |               |                       |                                        |                    |          |                          |
| **T¹**  | resistance | period        |                       |                                        |                    |          |                          |
| **T⁰**  |            | dimensionless | length, capacitance   | area                                   | volume             |          |                          |
| **T⁻¹** |            | frequency     | velocity              | r×v, kinematic viscosity, flux linkage | volume flow rate   |          |                          |
| **T⁻²** |            | density, ω²   | acceleration, E-field | v², specific energy, M/r, voltage      | mass = μ, charge   |          |                          |
| **T⁻³** |            |               |                       | dynamic viscosity                      | current, mass flow | momentum | angular momentum, action |
| **T⁻⁴** |            |               |                       | pressure, energy density               |                    | force    | energy, moment of force  |
| **T⁻⁵** |            |               |                       |                                        |                    |          | power                    |

Every quantity that contains mass once inherits its factor T⁻². Quantities in which mass cancels (specific energy, r×v, resistance, capacitance, inductance) contain no time from mass.

### Changes Relative to Version 1

| Quantity                                    | Version 1                                 | Version 2                                                           |
| ------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------- |
| Mass                                        | 4π²R³ (L³)                                | μ = 4π²R³/T² (L³T⁻²)                                                |
| Field parameter μ                           | shared the L³T⁻² cell with energy         | the mass itself                                                     |
| Energy                                      | L³T⁻² (the cell of μ)                     | L⁵T⁻⁴                                                               |
| Power                                       | L³T⁻³                                     | L⁵T⁻⁵                                                               |
| Energy density                              | T⁻²                                       | L²T⁻⁴                                                               |
| Density (follows from mass)                 | 3π (L⁰), the same for all bodies          | 3π/T² (T⁻²), individual                                             |
| Gravitational constant                      | a constant                                | G = 1, dimensionless; kilogram conversion factor                    |
| Momentum, force, action, pressure           | built on M = L³                           | gain the factor T⁻²: L⁴T⁻³, L⁴T⁻⁴, L⁵T⁻³, L²T⁻⁴                     |
| Core fission                                | ΔM = 4π²(R³ − r₁³ − r₂³), read as energy  | ΔM = μ − μ₁ − μ₂ is mass; ΔE = ΔM·w² (L⁵T⁻⁴), w a characteristic speed |
| Electricity                                 | open question                             | closed under Coulomb’s law without constants (§4)                   |
| Bernoulli’s law                             | —                                         | written in the table cells (§6)                                     |

## 4. Electrical Sector

**Convention.** Coulomb’s law is written as F = q²/r² without additional constants (a CGS-type system). The dimension of charge is fixed by this choice; in SI the ampere is independent, therefore this is a convention, not a derivation from nature.

| Quantity        | Obtained from | LT     | Status                        |
| --------------- | ------------- | ------ | ----------------------------- |
| Charge q        | q² = F·r²     | L³T⁻²  | convention                    |
| Current I       | q/T           | L³T⁻³  | derived under this convention |
| Voltage U       | E/q = q/r     | L²T⁻²  | same                          |
| Resistance Rₑ   | U/I           | L⁻¹T¹  | same                          |
| Capacitance C   | q/U           | L¹     | same                          |
| Inductance      | U·T/I         | L⁻¹T²  | same                          |
| Flux linkage Φ  | L·I = U·T     | L²T⁻¹  | same                          |
| Electric field  | F/q           | L¹T⁻²  | same                          |

- Ohm’s law U = I·Rₑ closes dimensionally. Resistance is **not** dimensionless. Resistance, capacitance and inductance contain no mass, so the choice M = μ does not affect them.
- Power U·I has dimension L⁵T⁻⁵, the same as mechanical E/T.
- Energies ½L·I² and ½C·U² occupy the same cell (L⁵T⁻⁴) as mechanical energy: in an LC circuit energy is exchanged inside a single cell.
- **Charge and mass share one cell** (L³T⁻²): F = q₁q₂/r² and F = M₁M₂/r² have the same form. This follows from two conventions taken together (G = 1 and Coulomb’s law without a constant) and does not mean that charge is mass.
- Further coincidences: current and mass flow rate (L³T⁻³); voltage and gravitational potential M/r (L²T⁻²); electric field and acceleration (L¹T⁻²), since in both sectors the field is force per unit source.
- **What is not derived.** Ohm’s law and LC resonance agree dimensionally, but the numerical coefficients (in particular the relation of LC frequency to geometry) are not obtained from the 3/2 law.

## 5. Coinciding Cells and Exchange Pairs

Dimensional coincidence does not mean identity of the quantities; these are places for checks.

- **L²T⁻²:** v², specific energy, gravitational potential M/r, p/ρ, voltage. A circular orbit satisfies v² = M/r; Bernoulli’s law is written as ½v² + p/ρ = const; the potential of a charge is q/r. Three balances live inside one cell.
- **L³T⁻²:** mass (= μ) and charge.
- **L³T⁻³:** current and mass flow rate.
- **L¹T⁻²:** acceleration and electric field.
- **L²T⁻¹:** kinematic viscosity, specific angular momentum r×v, flux linkage.
- **L⁵T⁻⁴:** energy, moment of force, pressure work pV, ½L·I², ½C·U².
- **T⁻²:** density and ω².

| System                   | What is exchanged     | Invariant                     | Cell   |
| ------------------------ | --------------------- | ----------------------------- | ------ |
| Ellipse                  | r ↔ v                 | r×v (r_p·v_p = r_a·v_a)       | L²T⁻¹  |
| Superconducting loop     | L ↔ I                 | flux linkage Φ = L·I          | L²T⁻¹  |
| Pipe                     | R ↔ v                 | flow rate A·v                 | L³T⁻¹  |
| Junction (pipe, circuit) | inflow ↔ outflow      | Σ ρ·A·v = 0 ; Σ I = 0         | L³T⁻³  |
| Pipe, energy             | v ↔ p                 | ½v² + p/ρ                     | L²T⁻²  |
| Circuit, conductor       | U and I grow together | Rₑ = U/I                      | L⁻¹T¹  |
| Transformer              | U ↔ I                 | U·I (power)                   | L⁵T⁻⁵  |

For the ellipse, the pipe and the junction the invariants are physically confirmed (angular momentum, continuity, conservation of mass and of charge, Kirchhoff’s first law). The flux through a closed superconducting loop is also conserved: if L changes, I adjusts so that L·I stays constant. This invariant falls into the same cell as r×v of the ellipse, which makes it a candidate for the circuit analogue of angular momentum. Caution: in the standard mechanical–electrical analogy (L ↔ M, I ↔ v) flux linkage corresponds to momentum, not to angular momentum. Status: observation.

## 6. Bernoulli’s Law in the LT Cells

Status: **derived** from classical mechanics in LT notation.

1. **Continuity.** Density ρ = M/V has dimension T⁻² and is constant (incompressible fluid); volume flow rate A·v is constant (L³T⁻¹), and so is mass flow rate ρ·A·v (L³T⁻³). Fluid velocity is determined by the cross-section and need not coincide with the orbital 2πR/T.
2. **Pressure work.** Pressure p (L²T⁻⁴) acting on volume V (L³) yields pV, an energy of dimension L⁵T⁻⁴.
3. **Energy.** Kinetic energy of a fluid element ½ρVv² plus pressure work remain constant along a streamline. Division by V gives ½ρv² + p = const (cell L²T⁻⁴). Division by ρ gives ½v² + p/ρ = const (cell L²T⁻², the same as v² and M/r of an orbit).
4. **Weight.** In an inclined pipe the term ρgh is added, with ρ = T⁻², g = L¹T⁻², h = L¹: ½ρv² + ρgh + p = const; all terms lie in the cell L²T⁻⁴.

Conditions: ideal fluid, steady flow, incompressibility, no viscosity. Limitations: viscosity, flow separation, cavitation, compressibility.

Numerical example (v₀ = 1, ρ = 1 in conventional units, circular pipe): when the radius is halved the velocity increases by a factor of 4 and the pressure drops by 7.5 conventional units.

For scale: water (1000 kg/m³) has LT density ρ = 6.67·10⁻⁸ s⁻². A ball of water of any size would have the surface period T = √(3π/ρ) ≈ 11 900 s.

No new predictions beyond classical hydrodynamics are obtained; the result is that the law is written in the table cells without additional engine rules.

## 7. Checks

- **Dimensions** of the mechanical and electrical sectors close (verified by counting powers of R and T, including U = I·Rₑ, U·I = E/T, ½L·I² = ½C·U² = pV = E, ρgh = p).
- **Surface periods**, T = 2π√(R³/M) from measured R and μ: Earth ≈ 5061 s, Mars ≈ 5991 s, Sun ≈ 10 008 s (mean radii 6371, 3389.5 and 695 700 km). T is taken from measured R and μ, not predicted.
- **Density** ρ = 3π/T² carries the individual density of each body, which a purely geometric mass cannot carry. The agreement with measured densities holds by construction, since T is computed from the same R and μ.

| Body    | T, s   | ρ = 3π/T², s⁻² | ρ / G_SI, kg/m³ | Geometric mass M = 4π²R³ (v1), kg/m³ |
| ------- | ------ | -------------- | --------------- | ------------------------------------ |
| Earth   | 5 061  | 3.680·10⁻⁷     | 5513            | 5513                                 |
| Moon    | 6 498  | 2.232·10⁻⁷     | 3344            | 5513                                 |
| Mars    | 5 991  | 2.626·10⁻⁷     | 3934            | 5513                                 |
| Jupiter | 10 319 | 8.851·10⁻⁸     | 1326            | 5513                                 |
| Sun     | 10 008 | 9.409·10⁻⁸     | 1410            | 5513                                 |

- **Mass ratios.** Earth/Moon = μ⊕/μ☾ = 81.30, the measured value (geometric mass gives 49.3 from radii). Mars: μ/G_SI = 6.42·10²³ kg (geometric mass calibrated on the Earth: 9.0·10²³ kg); Sun: 1.99·10³⁰ kg (geometric: 7.8·10³⁰ kg). M = μ is the quantity that astronomy measures directly: GM of the Sun and the Earth are known to about 10⁻¹⁰ and 10⁻⁹, while G alone is known only to about 2·10⁻⁵. The LT mass is therefore the best-measured form of mass.
- **Round periods** (integer number of kiloseconds) for 16 solid bodies with well-measured GM and radius did not show a pattern: only Mars lies within 0.01 ks, mean deviation 0.245 ks versus a random expectation of 0.25. Any T is admissible for a simulation.
- **Pair rule** (engine application), exact: each body accelerates towards the other with a₁ = M₂/d², a₂ = M₁/d²; the mutual approach acceleration is (M₁ + M₂)/d²; the forces are equal, F = M₁M₂/d²; momentum is conserved. No “dominant body” approximation is needed. The two-body period is P = 2π√(a³/(M₁ + M₂)).

Demonstrations (HTML, MIT licence): a constricting pipe (velocity from continuity, pressure from energy balance) and an orbital scene of the Solar System with mass = μ, an elliptical comet and an r×v counter.

## 8. Known Limitations

1. **Kilograms.** Conversion to SI needs G_SI, known only to about 2·10⁻⁵; the simulation itself does not need kilograms.
2. **Mean density only.** ρ = 3π/T² is the mean density; internal structure (core, mantle, atmosphere) is not described by one T.
3. **Small scales.** For nuclei and atoms the surface period is a formal number (gravity is negligible there), and M = 4π²R³/T² is only a rewriting of mass through density. Nuclei have nearly constant density, hence nearly constant T, hence M ∝ R³, which agrees with R ∝ A^{1/3}.
4. **Electricity** closes only under the chosen convention for Coulomb’s law. The shared cell of charge and mass is a consequence of two conventions, not a physical identity.
5. **Temperature:** working hypothesis L⁵T⁻⁴ (in energy units, k_B = 1) or L²T⁻² per unit mass; not derived.
6. **Circuit analogue of angular momentum:** flux linkage is a candidate (§5), not established.
7. **Coefficients** of Ohm’s and LC laws are not derived from the 3/2 law.
8. **Dimensions are not new.** The table coincides with LT-systems with dimensionless G (Brown, Bartini). The contribution is the engine-oriented form: R and T per body, density as 3π/T², the 3/2 law.

Resolved relative to version 1: the single density of all bodies and the resulting errors in mass (Mars, Sun, Earth/Moon); the dimension of energy; the electrical sector (under the stated convention).

## 9. What Is Not Claimed

- that the system describes real physics better than SI;
- that the gravitational constant does not exist (G = 1 is a choice of units; G_SI is the conversion factor to kilograms);
- that charge is mass, or that current is mass flow (shared cells are places for checks, not identities);
- that Ohm’s, LC or Bernoulli’s laws are derived from the 3/2 law (Bernoulli is derived from classical mechanics inside the LT cells; Ohm and LC are only dimensionally consistent);
- that the dimension table is original (it coincides with Brown and Bartini);
- that body periods are integer numbers of kiloseconds.

## References

1. Colesnicenco, V. (2026). *Inverse 3/2 Law (Geometric Interpretation of Kepler's Third Law)*. Zenodo. https://doi.org/10.5281/zenodo.19799606
2. Colesnicenco, V. (2026). *General Architecture of the BaseReal-OS Hybrid Four-Layer Computational Model.* BaseReal-OS Technical Preprint Series, Part 1. Zenodo. https://doi.org/10.5281/zenodo.22060039
3. Colesnicenco, V. (2026). *Geometrization of Physical Quantities: A Modification of Bartini’s LT-System Based on the Inverse 3/2 Law* (v1). Zenodo. https://zenodo.org/records/20788306
4. Landau, L. D., & Lifshitz, E. M. *Fluid Mechanics* (Course of Theoretical Physics, Vol. VI).
5. Brown, G. Burniston (1941). A new treatment of the theory of dimensions. *Proceedings of the Physical Society*, 53(4), 418–432. https://doi.org/10.1088/0959-5309/53/4/307
6. Bartini, R. L. (1965). Some relations between physical constants. *Doklady Akademii Nauk SSSR*, 163(4), 861–864.  
   (English translation: Bartini, R. O. (1966). Some relations between physical constants. *Soviet Physics Doklady*, 10(8), 732–735).
