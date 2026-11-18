# Galaxy Booster v2: every number in the paper, from one script (no dependencies).
#   python booster_numbers.py
import math

TAU = 2 * math.pi
out = []
P = lambda k, v: out.append(f'{k:<58} {v}')

# ---------------- A. The game mechanic (defaults of demo/galaxy-booster.html) ----------------
L = 120.0                  # life of a star, s (at x1): from release to the rim
R0, C, RMAX = 0.022, 0.28, 1.04   # in units of the galaxy radius
K = math.log((RMAX + C) / (R0 + C)) / L
OMN = TAU / 55             # booster spin = pattern speed
OMS = TAU / 210            # star orbit
OMP = TAU / 170            # nozzle precession
EPS = math.radians(6)
MYR = 4                    # story clock: 1 s = 4 Myr

def pitch(r, omn=OMN):     # pitch angle of the arm at radius r, degrees
    return math.degrees(math.atan(K * (r + C) / ((omn - OMS) * r)))

def turns(omn=OMN):        # turns of one arm from release to the rim
    return (omn - OMS) * L / TAU

P('Drift rate K, 1/s', f'{K:.5f}')
P('Radial speed at r = 0.05 | 0.5 | 1.0 (radii per 100 s)', ' | '.join(f'{K * (r + C) * 100:.2f}' for r in (0.05, 0.5, 1.0)))
P('Turns of one arm (spin 55 s)', f'{turns():.2f}')
P('Pitch angle at r = 0.3 | 0.6 | 1.0, deg (spin 55 s)', ' | '.join(f'{pitch(r):.1f}' for r in (0.3, 0.6, 1.0)))
for sp in (35, 55, 90):
    P(f'Spin {sp} s: turns | pitch at r = 0.6, deg', f'{turns(TAU / sp):.2f} | {pitch(0.6, TAU / sp):.1f}')
sig = lambda r: 1 / (r * (r + C))     # surface density of released stars, steady state
P('Surface density ratio S(0.3)/S(1.0)', f'{sig(0.3) / sig(1.0):.1f}')
P('Equivalent exponential scale between 0.3 and 1.0 (radii)', f'{0.7 / math.log(sig(0.3) / sig(1.0)):.3f}')
P('Warp amplitude at the rim, 0.85 r sin(eps) (radii)', f'{0.85 * 1.0 * math.sin(EPS):.3f}')
P('... for a 15 kpc disk, kpc', f'{0.85 * 15 * math.sin(EPS):.2f}')
P('Precession waves along one life', f'{L / (TAU / OMP):.2f}')
P('Story clock: life | booster turn | star orbit, Myr', f'{L * MYR:.0f} | {55 * MYR:.0f} | {210 * MYR:.0f}')

# ---------------- B. Reality check: could a real black hole do this? ----------------
G, c, Msun, kpc, yr, Lsun = 6.674e-11, 2.998e8, 1.989e30, 3.0857e19, 3.156e7, 3.828e26
VC, RC, RD, RM, R_SUN = 230e3, 1.0, 2.6, 15.0, 8.2
MDISK, MBH, AGE = 5e10 * Msun, 4.1e6 * Msun, 10e9 * yr
v0 = lambda r: VC * math.sqrt(math.log(1 + (r / RC) ** 2))   # launch speed that stops a star at r (kpc), log potential
P('Centripetal acceleration at the Sun, m/s^2', f'{VC ** 2 / (R_SUN * kpc):.2e}')
P('Launch speed to reach 2 | 8.2 | 15 kpc, km/s', ' | '.join(f'{v0(r) / 1e3:.0f}' for r in (2, 8.2, 15)))
n = 200000
num = den = 0.0
for i in range(1, n):
    r = RM * i / n; w = r * math.exp(-r / RD); num += w * 0.5 * v0(r) ** 2; den += w
E = num / den * MDISK
LEDD = 1.26e31 * MBH / Msun
P('Launch energy of the disk, J | / (L_Edd x 10 Gyr)', f'{E:.2e} | {E / (LEDD * AGE):.1e}')
P('Launch energy / (M_BH c^2)', f'{E / (MBH * c * c):.1%}')
JMAX, JDISK = G * MBH ** 2 / c, MDISK * VC * 2 * RD * kpc
P('Disk angular momentum / max spin of Sgr A*', f'{JDISK / JMAX:.1e}')
P('Launch rate needed (stars/yr) | / observed HVS rate 1e-4', f'{5e10 / 10e9:.0f} | {5e10 / 10e9 / 1e-4:.0e}')
print('\n'.join(out))
