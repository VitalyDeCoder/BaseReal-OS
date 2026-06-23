# The Geometric Inverse 3/2 Law

**Author:** Vitali Colesnicenco  
**Affiliation:** Independent Researcher, London, England, United Kingdom  
**Date:** April 26, 2026

---

## Introduction

The geometric inverse 3/2 law is proposed as a fundamental framework for the construction of virtual digital universes. The inverse 3/2 law is derived from Kepler's Third Law.

The modeling of gravitational systems and digital universes is based on only two geometric parameters: the **radius** and the **system time**.

This approach is particularly advantageous for educational and gaming simulators, such as *Kerbal Space Program*, where the precise configuration of orbits and planetary behavior requires simple, physically meaningful input parameters.

---

## Construction

- A vertical axis is drawn upwards from a central point.
- Arcs expand from this axis with radii increasing in integer steps: $r,\ 2r,\ 3r,\ \ldots$
- The arc's opening angle decreases as the distance from the central point increases.
- The first arc with radius $r$ unfolds completely to form a circle.

The second arc ($n = 2$) opens to an angle:

$$\alpha = \frac{2\pi}{2^{3/2}}$$

Any other arc with radius $nr$ opens to an angle:

$$\alpha_n = \frac{2\pi}{n^{3/2}}$$

> The arcs can be extended to infinity, which indicates that phenomena built upon the foundation of this law are capable of interacting across infinite distances.

---

## Inertial Parameter (Geometrical Mass)

Even at the stage of a static 2D drawing, it can be observed that the square of any arc multiplied by its radius yields the same value:

$$L_n^2 \cdot r_n = \left(\frac{2\pi \cdot nr}{n^{3/2}}\right)^2 \cdot (nr) = \left(\frac{4\pi^2 r^2}{n}\right) \cdot (nr) = 4\pi^2 r^3 = \text{const}$$

This constant can be associated with **mass** — it is an **inertial parameter**.

- The symbol of resistance to external influence is the gyroscope.
- A torus exhibits a gyroscopic effect.
- **Geometrical Mass** is defined as an inertial parameter where **1 m³** of torus sector volume corresponds to **585 kg** of physical mass.

To visualize this constant, the volume of a torus with a tube radius equal to half of the torus radius is used: $r = 0.5R$. The 3D visualization consists of equal-volume torus sectors.

🔗 [BaseReal-OS — 3D visualization](https://vitalydecoder.github.io/BaseReal-OS/)

---

## Dynamics. Adding the Period

Once system time $T$ is added, each arc shows the path a body travels at its current distance from the center during one system period. This results in a velocity distribution scheme:

| Parameter | Formula | Description |
|---|---|---|
| Angular velocity | $\omega = \dfrac{2\pi}{T}$ | Angular velocity |
| Orbital velocity | $\upsilon = \dfrac{2\pi R}{T}$ | Linear orbital velocity |

After assigning the time period $T$, a second constant emerges. The square of the angular velocity of the arc's opening multiplied by the cube of the arc's radius equals a constant — this is the **$\mu$ — gravitational parameter** of the field:

$$\mu = \omega^2 r^3 = \frac{4\pi^2}{T^2} r^3 = \frac{4\pi^2 r^3}{T^2} = \text{const}$$

Or in terms of orbital velocity:

$$\mu = \upsilon^2 r = \frac{4\pi^2 r^2}{T^2} \cdot r = \frac{4\pi^2 r^3}{T^2} = \text{const}$$

🔗 [BaseReal-OS — dynamics](https://vitalydecoder.github.io/BaseReal-OS/speed.html)

---

## Mass and the Gravitational Parameter

The intensity of $\mu$ manifests as centripetal acceleration, which decreases with the square of the distance from the center of the field. Thus, when the period is added, the inverse 3/2 law generates dynamics, and the **inverse square law** naturally follows from it.

In this model, the mass of a body is determined **purely geometrically**:

$$M = 4\pi^2 R^3$$

> It is noteworthy that the Earth's mass value calculated in this manner is very close to the result obtained by Cavendish when determining the mean density of the Earth.

**A key feature of this model** is that the gravitational parameter and mass do not maintain a direct linear proportionality; rather, each object is characterized by its own fundamental period $T$.

---

## Fundamental Periods

The minimum astronomical unit used is the **kilosecond (1000 s)**.

For Earth, Mars, and the Sun, the following fundamental periods are used within the framework of the model:

| Body | Period $T$ |
|---|---|
| **Earth** | 5000 s (5 ks), anomaly +60 s |
| **Mars** | 6000 s (6 ks) |
| **Sun** | 10,000 s (10 ks) |

The Earth anomaly of +60 s is explained by a 50 km radius increase, consistent with the Theia impact hypothesis, while the gravitational field remains unchanged.

In this model, mass follows the calculated field, keeping the gravitational parameter ($\mu$) and the inertial parameter ($M$) entirely decoupled. This provides a natural gain of several percent for small bodies during barycenter calculations.

---

## Mutual Attraction and Newton's Third Law

In the proposed geometric model, each body simultaneously serves as:

- the **source** of its own gravitational field: $\mu = \dfrac{4\pi^2 R^3}{T^2}$
- an **inertial object**: $M = 4\pi^2 R^3$

The dominant body's field indicates the direction and magnitude of acceleration to both masses (the "hammer and feather" principle is preserved). This acceleration is divided between the bodies **in inverse proportion to their masses** — automatically yielding perfect compliance with Newton's third law. The forces are equal and opposite.

---

## Example: Mutual Orbital Perturbation — Earth–Venus

**Given:**

- $\mu_\text{Earth} = 4 \times 10^{14}\ \text{m}^3/\text{s}^2$
- $R = 4.2 \times 10^{10}\ \text{m}$ — average Earth–Venus distance at opposition / inferior conjunction

**Calculation:**

$$R^2 = (4.2 \times 10^{10})^2 = 1.764 \times 10^{21}\ \text{m}^2$$

$$a = \frac{\mu_\text{Earth}}{R^2} = \frac{4 \times 10^{14}}{1.764 \times 10^{21}} = 2.27 \times 10^{-7}\ \text{m/s}^2$$

The barycentre shows what percentage of acceleration is assigned to each body:

| Body | Share | Force ($F$) |
|---|---|---|
| Venus | 54% | $F_1 = 0.54 \times a \times 4\pi^2 r_\text{Venus}^3 \approx 1.072 \times 10^{15}\ \text{m}^4/\text{s}^2$ |
| Earth | 46% | $F_2 = 0.46 \times a \times 4\pi^2 r_\text{Earth}^3 \approx 1.065 \times 10^{15}\ \text{m}^4/\text{s}^2$ |

With a more accurate calculation of the Earth–Venus system barycentre, the values of $F_1$ and $F_2$ become equal.

**Radii used:**
- $r_\text{Venus} = 6.052 \times 10^6\ \text{m}$
- $r_\text{Earth} = 6.371 \times 10^6\ \text{m}$

---

## Conclusion

In this geometric model, gravity works as a simple algorithm for distributing a single acceleration. Instead of calculating forces for each object separately, the system finds the total field strength at a specific point and divides it between bodies in inverse proportion to their mass via the barycentre.

This creates a perfect illusion of "opposing forces," although in reality it is merely an optimized way of updating coordinates. **Newton's third law** is not the result of a struggle between two objects, but the basic code maintaining the integrity of the simulation grid.

This geometric model is ideal for virtual universes where complex matter properties are reserved for future updates. By eliminating the need for density calculations or particle distribution, it allows users to participate in world-building — creating stars and planets with physically accurate mechanics through a streamlined, efficient framework.
