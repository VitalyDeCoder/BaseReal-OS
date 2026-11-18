# Duet of Algorithms — VIX replication code (v2.0)

Replication code for **Section 8** of:

> Colesnicenco, V. (2026). *Duet of Algorithms: A Two-Process Architecture of Threshold Transitions, from Dissipative Systems to Topological and Measurement-Induced Phases, and the Role of Conditional Intent as a Directing Operator.* Version 2.0.

One script reproduces every number in Section 8.

## What it tests

| # | Test | Output file |
|---|---|---|
| 1 | Audit of the eight hand-picked events of v1 under three definitions of "calm" (exact Mann–Whitney) | `1_v1_events.csv`, `1_v1_mann_whitney.csv` |
| 2 | Ex-ante detection of **all** VIX spikes, 1990–2026 (no hand selection) | `2_all_spikes.csv` |
| 3 | Does preceding calm predict spike size? Spearman ρ vs a surrogate null (HAR model of log VIX, block-bootstrapped residuals, 300 series) | `3_size_test_vs_surrogates.csv` |
| 4 | Robustness of test 3 to the spike threshold (1.5×–2.0×) | `4_robustness.csv` |
| 5 | Does a long calm raise the probability of a spike within 63 trading days? Hazard ratio vs surrogate null (120 series) | `5_hazard_test.csv` |

The design parameters (spike rule, window lengths, quantiles, seeds) are fixed constants at the top of `duet_vix.py`.

## Run

```bash
pip install -r requirements.txt
python duet_vix.py                       # downloads data from the public mirror
python duet_vix.py --data vix-daily.csv  # or use a local copy
python duet_vix.py --quick               # 30 surrogates, ~5 s, for a smoke test
```

The full run takes about 30 seconds on a laptop. Tables are written to `./results/`. The reference output from the paper is included in `results/` for comparison.

## Data

The data are **not** redistributed in this archive. The script reads the daily CBOE Volatility Index (VIX) closing values from:

- the public mirror `datasets/finance-vix` on GitHub (`data/vix-daily.csv`, downloaded automatically); or
- the original CBOE file, <https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv> (pass it with `--data`).

Any CSV with `DATE` and `CLOSE` columns works. The paper uses 9,278 trading days, from 1990-01-02 to 2026-09-22. The default `--end 2026-09-22` truncates later data so that the published numbers are reproduced exactly. The mirror is updated over time, so if earlier values in it are ever revised, small differences can appear.

## Expected key results

| Test | Result |
|---|---|
| v1 events, longest streak below 15 inside 90-day window | U = 16, exact p = 0.029 |
| v1 events, unbounded streak below 15 before event | U = 14, exact p = 0.114 |
| v1 events, regime-relative calm | U = 9.5, exact p = 0.886 |
| Spikes found | 40 |
| Calm (regime-relative streak) vs log(peak/base) | ρ = −0.02; surrogate 95% band [−0.27, +0.30] |
| Hazard ratio, top vs bottom tercile of calm | 1.24; surrogate 95% band [0.68, 1.84], p = 0.35 |

## Tested with

Python 3.13, numpy 2.5, pandas 3.0, scipy 1.18. The minimum versions in `requirements.txt` should also work.

## Licence

Code: MIT (see `LICENSE`). The paper is distributed separately under CC BY 4.0.

## Citation

See `CITATION.cff`. Please cite both the paper and this software record.
