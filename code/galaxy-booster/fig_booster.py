# Figure 2 of Galaxy Booster v2 (the mechanic) as a plain SVG, no dependencies.
#   python fig_booster.py booster_v2_fig2.svg
import math, sys

TAU = 2 * math.pi
L, R0, C, RMAX = 120.0, 0.022, 0.28, 1.04
K = math.log((RMAX + C) / (R0 + C)) / L
OMS = TAU / 210

W, H = 960, 430
F = 'font-family="Segoe UI, Arial, sans-serif"'
o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">', f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
def text(x, y, s, col='#223', size=12.5, anchor='start', weight='400'):
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{col}" text-anchor="{anchor}" {F}>{s}</text>')

# (a) one arm for three booster spins, face-on
cx, cy, R = 300, 200, 150
text(40, 28, '(a) One arm for three booster spins (face-on)', '#112', 14, weight='600')
o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#c9d2de" stroke-dasharray="4 5"/>')
o.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="#112"/>')
for sp, col, lab in ((35, '#7b3fbf', '35 s · 2.9 turns'), (55, '#1b84c4', '55 s · 1.6 turns (default)'), (90, '#e08a1e', '90 s · 0.8 turns')):
    w = TAU / sp - OMS
    pts = []
    for i in range(0, 401):
        a = L * i / 400
        r = (R0 + C) * math.exp(K * a) - C
        th = -w * a
        pts.append(f'{cx + R * r * math.cos(th):.1f},{cy - R * r * math.sin(th):.1f}')
    o.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="{3 if sp == 55 else 2}"/>')
for k, (col, lab) in enumerate((('#7b3fbf', 'spin 35 s · 2.9 turns'), ('#1b84c4', 'spin 55 s · 1.6 turns (default)'), ('#e08a1e', 'spin 90 s · 0.8 turns'))):
    o.append(f'<line x1="40" y1="{405 - 18 * (2 - k):.0f}" x2="62" y2="{405 - 18 * (2 - k):.0f}" stroke="{col}" stroke-width="3"/>')
    text(68, 409 - 18 * (2 - k), lab)
text(cx + R + 4, cy - 4, 'rim')

# (b) surface density of released stars
x0, y0, w, h = 560, 50, 360, 300
text(x0, 28, '(b) Stars per area across the disk', '#112', 14, weight='600')
sig = lambda r: 1 / (r * (r + C))
rd = 0.351
exp_ = lambda r: sig(0.3) * math.exp(-(r - 0.3) / rd)
ylo, yhi = 0.3, 300.0
fx = lambda r: x0 + w * r / 1.0
fy = lambda v: y0 + h - h * (math.log10(v) - math.log10(ylo)) / (math.log10(yhi) - math.log10(ylo))
o.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="none" stroke="#9aa6b8"/>')
for t in (0, 0.2, 0.4, 0.6, 0.8, 1.0):
    o.append(f'<line x1="{fx(t):.1f}" y1="{y0}" x2="{fx(t):.1f}" y2="{y0 + h}" stroke="#eef1f5"/>'); text(fx(t), y0 + h + 17, f'{t:g}', '#445', 12, 'middle')
for t in (1, 10, 100):
    o.append(f'<line x1="{x0}" y1="{fy(t):.1f}" x2="{x0 + w}" y2="{fy(t):.1f}" stroke="#eef1f5"/>'); text(x0 - 7, fy(t) + 4, f'{t:g}', '#445', 12, 'end')
text(x0 + w / 2, y0 + h + 36, 'radius, in units of the galaxy radius', '#223', 13, 'middle')
o.append(f'<text transform="translate({x0 - 38},{y0 + h / 2}) rotate(-90)" text-anchor="middle" font-size="13" fill="#223" {F}>relative surface density</text>')
pts = ' '.join(f'{fx(r):.1f},{fy(sig(r)):.1f}' for r in [0.03 + 0.97 * i / 200 for i in range(201)] if ylo < sig(r) < yhi)
o.append(f'<polyline points="{pts}" fill="none" stroke="#1b84c4" stroke-width="3"/>')
pts = ' '.join(f'{fx(r):.1f},{fy(exp_(r)):.1f}' for r in [0.03 + 0.97 * i / 200 for i in range(201)] if ylo < exp_(r) < yhi)
o.append(f'<polyline points="{pts}" fill="none" stroke="#e08a1e" stroke-width="2" stroke-dasharray="7 5"/>')
text(fx(0.40), fy(sig(0.40)) - 14, 'booster: Σ ∝ 1 / [r (r + C)]', '#13679b')
text(fx(0.08), fy(exp_(0.75)) + 52, 'dashed: exponential disk, scale 0.35', '#b86a0a')
o.append('</svg>')
open(sys.argv[1] if len(sys.argv) > 1 else 'booster_v2_fig2.svg', 'w', encoding='utf-8').write('\n'.join(o))
