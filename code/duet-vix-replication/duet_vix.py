#!/usr/bin/env python3
"""
Replication code for Section 8 of
  Colesnicenco, V. (2026). Duet of Algorithms, v2.0.

Tests performed
  1. Audit of the eight hand-picked events of v1 under three definitions of "calm"
     (exact two-sided Mann-Whitney test).
  2. Ex-ante, classification-free test on ALL VIX spikes: does the preceding calm
     predict spike size? (Spearman correlations)
  3. Surrogate null: HAR model of log VIX with block-bootstrapped residuals; the
     identical pipeline is run on each surrogate series.
  4. Robustness of the size test to the spike threshold.
  5. Hazard test: does a long calm raise the probability of a spike within 63 days?

Usage
  python duet_vix.py                       # downloads data from the public mirror
  python duet_vix.py --data vix-daily.csv  # uses a local file
  python duet_vix.py --quick               # 30 surrogates, for a fast check

All tables are written to ./results/ . Seeds are fixed; with the default end date
(2026-09-22) the output reproduces the numbers reported in the paper.
"""
import argparse
import os
import sys
import urllib.request

import numpy as np
import pandas as pd
from scipy import stats

MIRROR_URL = "https://raw.githubusercontent.com/datasets/finance-vix/main/data/vix-daily.csv"

# ---- fixed design parameters (set before looking at results; see paper, Sec. 8.2) ----
RISE = 1.6      # spike: close >= RISE x min of previous PRE days
SEP = 63        # minimum trading days between spike onsets
PRE = 20        # run-up window, excluded from the calm window
WIN = 90        # calm window length (trading days)
LOOK = 252      # trailing window for regime-relative quantiles
Q = 0.25        # regime-relative quantile
HORIZON = 63    # hazard horizon (trading days)
BLOCK = 20      # block length for residual bootstrap
SEED_SIZE = 20261107
SEED_HAZARD = 7

EVENTS = [  # v1 events: (label, first date of event, v1 classification)
    ("Feb 2007 (Shanghai / subprime onset)", "2007-02-27", "endo"),
    ("Feb 2018 Volmageddon", "2018-02-02", "endo"),
    ("Aug 2015 yuan devaluation", "2015-08-11", "endo"),
    ("Aug 2024 yen carry unwind", "2024-08-01", "endo"),
    ("Aug 1998 Russia / LTCM", "1998-08-17", "exo"),
    ("Sep 2001 attacks", "2001-09-11", "exo"),
    ("May 2010 Flash Crash", "2010-05-06", "exo"),
    ("Mar 2026 oil shock", "2026-03-02", "exo"),
]


# ------------------------------------------------------------------ data
def load(path, end):
    if path is None:
        path = "vix-daily.csv"
        if not os.path.exists(path):
            print(f"Downloading {MIRROR_URL} ...")
            urllib.request.urlretrieve(MIRROR_URL, path)
    df = pd.read_csv(path)
    df.columns = [c.strip().upper() for c in df.columns]
    df["DATE"] = pd.to_datetime(df["DATE"])
    df = df.set_index("DATE").sort_index()
    if end:
        df = df.loc[:end]
    close = df["CLOSE"].astype(float).dropna()
    return close.index, close.values


# ------------------------------------------------------------------ helpers
def longest_run(mask):
    best = cur = 0
    for m in mask:
        cur = cur + 1 if m else 0
        best = max(best, cur)
    return best


def streak_before(x, i, thr=15.0):
    n, j = 0, i - 1
    while j >= 0 and x[j] < thr:
        n += 1
        j -= 1
    return n


def rel_calm_share(x, i, win=WIN, look=LOOK, q=Q):
    """Share of the `win` days before i with VIX below the q-quantile of its own trailing year."""
    vals = [x[j] < np.quantile(x[j - look:j], q) for j in range(max(look, i - win), i)]
    return float(np.mean(vals)) if vals else np.nan


def find_spikes(x, rise=RISE):
    onsets, last = [], -10**9
    for t in range(LOOK + PRE + WIN, len(x) - 20):
        if x[t] >= rise * x[t - PRE:t].min() and t - last >= SEP:
            onsets.append(t)
            last = t
    return onsets


def spike_features(x, onsets):
    rows = []
    for t in onsets:
        base = x[t - PRE:t].min()
        peak = x[t:t + 21].max()
        end = t - PRE
        seg = x[end - WIN:end]
        ref_q = np.quantile(x[end - LOOK:end], Q)
        rows.append(dict(
            t=t, base=base, peak=peak,
            log_ratio=np.log(peak / base), jump=peak - base,
            calm_rel_streak=longest_run(seg < ref_q),
            calm_abs15=int((seg < 15).sum()),
            calm_lowvar=-np.var(np.diff(np.log(seg))),  # higher = calmer
        ))
    return pd.DataFrame(rows)


PAIRS = [(c, m) for c in ["calm_rel_streak", "calm_abs15", "calm_lowvar"]
         for m in ["log_ratio", "jump"]]


def hazard_ratio(x, horizon=HORIZON, step=5):
    ons = np.array(find_spikes(x))
    calm, hit = [], []
    for t in range(400, len(x) - horizon, step):
        q = np.quantile(x[t - LOOK:t], Q)
        calm.append(longest_run(x[t - WIN:t] < q))
        hit.append(np.any((ons > t) & (ons <= t + horizon)))
    calm, hit = np.array(calm), np.array(hit)
    hi = calm >= np.quantile(calm, 2 / 3)
    lo = calm <= np.quantile(calm, 1 / 3)
    return hit[hi].mean() / max(hit[lo].mean(), 1e-9), hit[hi].mean(), hit[lo].mean()


# ------------------------------------------------------------------ surrogate model
class HAR:
    """HAR(1,5,22) model of log VIX (Corsi 2009) with block-bootstrapped residuals."""

    def __init__(self, x):
        lx = np.log(x)
        n = len(lx)
        d1 = lx[21:-1]
        w5 = np.array([lx[i - 4:i + 1].mean() for i in range(21, n - 1)])
        m22 = np.array([lx[i - 21:i + 1].mean() for i in range(21, n - 1)])
        y = lx[22:]
        X = np.column_stack([np.ones_like(d1), d1, w5, m22])
        self.beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        self.res = y - X @ self.beta
        self.init = lx[:22]
        self.n = n

    def simulate(self, rng):
        steps = self.n - 22
        b = self.beta
        starts = rng.integers(0, len(self.res) - BLOCK, size=steps // BLOCK + 1)
        eps = np.concatenate([self.res[s:s + BLOCK] for s in starts])[:steps]
        a = np.empty(self.n)
        a[:22] = self.init
        for k in range(steps):
            i = k + 22
            a[i] = b[0] + b[1] * a[i - 1] + b[2] * a[i - 5:i].mean() + b[3] * a[i - 22:i].mean() + eps[k]
        return np.exp(a)


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", help="path to a VIX CSV with DATE and CLOSE columns")
    ap.add_argument("--end", default="2026-09-22", help="last date used (default reproduces the paper)")
    ap.add_argument("--n-sims", type=int, default=300, help="surrogates for the size test")
    ap.add_argument("--n-sims-hazard", type=int, default=120, help="surrogates for the hazard test")
    ap.add_argument("--quick", action="store_true", help="30 surrogates each, for a fast check")
    ap.add_argument("--out", default="results")
    a = ap.parse_args()
    if a.quick:
        a.n_sims = a.n_sims_hazard = 30
    os.makedirs(a.out, exist_ok=True)

    dates, x = load(a.data, a.end)
    print(f"VIX closes: {len(x)} days, {dates[0].date()} to {dates[-1].date()}\n")

    # 1. audit of v1 events
    rows = []
    for label, d, kind in EVENTS:
        i = dates.searchsorted(pd.Timestamp(d))
        rows.append(dict(event=label, v1_class=kind, date=str(dates[i].date()),
                         prev_close=round(x[i - 1], 2),
                         streak_before=streak_before(x, i),
                         win90_max_streak=longest_run(x[max(0, i - WIN):i] < 15),
                         rel_calm_share_90=round(rel_calm_share(x, i), 2)))
    ev = pd.DataFrame(rows)
    tests = []
    for col in ["streak_before", "win90_max_streak", "rel_calm_share_90"]:
        e = ev.loc[ev.v1_class == "endo", col].values
        o = ev.loc[ev.v1_class == "exo", col].values
        r = stats.mannwhitneyu(e, o, alternative="two-sided", method="exact")
        tests.append(dict(definition=col, U=r.statistic, exact_p=round(r.pvalue, 4)))
    tests = pd.DataFrame(tests)
    ev.to_csv(f"{a.out}/1_v1_events.csv", index=False)
    tests.to_csv(f"{a.out}/1_v1_mann_whitney.csv", index=False)
    print("1. v1 events under three definitions of calm")
    print(ev.to_string(index=False))
    print(tests.to_string(index=False), "\n")

    # 2. all spikes, ex ante
    F = spike_features(x, find_spikes(x))
    F.insert(0, "onset", [str(dates[t].date()) for t in F.t])
    F.drop(columns="t").round(4).to_csv(f"{a.out}/2_all_spikes.csv", index=False)
    obs = {p: stats.spearmanr(F[p[0]], F[p[1]]) for p in PAIRS}
    print(f"2. {len(F)} spikes (rise >= {RISE}x over {PRE}d, onsets >= {SEP}d apart)")

    # 3. surrogate null
    har = HAR(x)
    print(f"3. HAR coefficients (const, d, w, m): {np.round(har.beta, 4)}; {a.n_sims} surrogates ...")
    rng = np.random.default_rng(SEED_SIZE)
    null = {p: [] for p in PAIRS}
    for _ in range(a.n_sims):
        sim = har.simulate(rng)
        on = find_spikes(sim)
        if len(on) < 10:
            continue
        G = spike_features(sim, on)
        for p in PAIRS:
            null[p].append(stats.spearmanr(G[p[0]], G[p[1]])[0])
    rows = []
    for p in PAIRS:
        v = np.array(null[p])
        rho = obs[p][0]
        rows.append(dict(calm=p[0], size=p[1], rho=round(rho, 3), p_parametric=round(obs[p][1], 3),
                         null_mean=round(v.mean(), 3), null_lo95=round(np.quantile(v, .025), 3),
                         null_hi95=round(np.quantile(v, .975), 3),
                         p_one_sided_vs_null=round((np.sum(v >= rho) + 1) / (len(v) + 1), 3)))
    size = pd.DataFrame(rows)
    size.to_csv(f"{a.out}/3_size_test_vs_surrogates.csv", index=False)
    print(size.to_string(index=False), "\n")

    # 4. robustness to spike threshold
    rob = []
    for r in [1.5, 1.6, 1.8, 2.0]:
        G = spike_features(x, find_spikes(x, rise=r))
        r1 = stats.spearmanr(G.calm_rel_streak, G.log_ratio)
        r2 = stats.spearmanr(G.calm_abs15, G.log_ratio)
        rob.append(dict(rise=r, n=len(G), rho_rel_streak=round(r1[0], 3), p_rel=round(r1[1], 3),
                        rho_abs15=round(r2[0], 3), p_abs15=round(r2[1], 3)))
    rob = pd.DataFrame(rob)
    rob.to_csv(f"{a.out}/4_robustness.csv", index=False)
    print("4. Robustness of the size test (log ratio)")
    print(rob.to_string(index=False), "\n")

    # 5. hazard
    hr, p_hi, p_lo = hazard_ratio(x)
    rng_h = np.random.default_rng(SEED_HAZARD)
    hn = np.array([hazard_ratio(har.simulate(rng_h))[0] for _ in range(a.n_sims_hazard)])
    haz = pd.DataFrame([dict(hazard_ratio=round(hr, 3), rate_top_tercile=round(p_hi, 3),
                             rate_bottom_tercile=round(p_lo, 3), null_mean=round(hn.mean(), 3),
                             null_lo95=round(np.quantile(hn, .025), 3), null_hi95=round(np.quantile(hn, .975), 3),
                             p_one_sided=round((np.sum(hn >= hr) + 1) / (len(hn) + 1), 3),
                             n_surrogates=len(hn))])
    haz.to_csv(f"{a.out}/5_hazard_test.csv", index=False)
    print(f"5. Hazard of a spike within {HORIZON} days, top vs bottom tercile of calm")
    print(haz.to_string(index=False))
    print(f"\nAll tables written to ./{a.out}/")


if __name__ == "__main__":
    sys.exit(main())
