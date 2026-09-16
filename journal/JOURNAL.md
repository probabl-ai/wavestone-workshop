# Journal

## Status

- **Date:** 2026-09-16
- **Goal:** Credit card fraud detection (Kaggle mlg-ulb/creditcardfraud) — Wavestone workshop.
- **Stage:** Baseline (`01_baseline`) done; CV on `wavestone-cv`, fitted report on `wavestone-leaderboard`.

### Workspace decisions

- package: `fraud_detection` — recorded: 2025-09-15
- env manager: `uv` — recorded: 2025-09-15
- tabular library: `pandas` — recorded: 2025-09-15
- skore mode: `hub` (via `.skore` config; `SKORE_HUB_URI` / `SKORE_HUB_API_KEY` loaded in scripts) — recorded: 2025-09-15
- Hub routing: CV → `wavestone-cv`; full train / fitted → `wavestone-leaderboard` (see `AGENT.md`)
- agent feature: installed (`ipython`, `pyright` in `agent` group) — recorded: 2025-09-15
- optional features: none — recorded: 2025-09-15
- dataset source: Kaggle `mlg-ulb/creditcardfraud` via `kagglehub` → `data/creditcard.csv` — recorded: 2025-09-15

## Data understanding (EDA)

- **Status:** done — 2025-09-15
- **Summary:** 284,807 × 31, all numeric, zero missing. Target `Class` is
  severely imbalanced (492 frauds = 0.173%). Strongest fraud signal in
  PCA components V17/V14/V12/V10; no groups, no datetime columns
  (implicit time ordering via `Time`).
- **Report:** [data/eda.md](../data/eda.md) · [data/eda_creditcard.html](../data/eda_creditcard.html)

## Experiments

| # | Experiment | Status | Key metrics |
|---|---|---|---|
| 01 | baseline | done | AUPRC 0.760 ± 0.027; ROC-AUC 0.977 ± 0.009; Precision 0.876; Recall 0.613 (5-fold KFold) |

### History

- **01_baseline** (2026-09-16): Scaled `LogisticRegression` on raw V-features + `Amount` + `Time`. Splitter: `KFold(n_splits=5, shuffle=True, random_state=0)` (IID). Hub: [CV #94](https://saint-gobain.skore.probabl.ai/workshop-wavestone/wavestone-cv/cross-validations/94) · [fitted #100](https://saint-gobain.skore.probabl.ai/workshop-wavestone/wavestone-leaderboard/estimators/100). Design: [journal/01_baseline.md](01_baseline.md).
- **01_baseline + AUPRC** (2026-09-16): registered AUPRC (average precision) as a custom metric via `fraud_detection.evaluate.add_auprc` (sklearn `make_scorer(average_precision_score, response_method="predict_proba", pos_label=1)` on `report.metrics.add`); both reports re-pushed — [CV #101](https://saint-gobain.skore.probabl.ai/workshop-wavestone/wavestone-cv/cross-validations/101) · [fitted #107](https://saint-gobain.skore.probabl.ai/workshop-wavestone/wavestone-leaderboard/estimators/107). AUPRC 0.760 ± 0.027 now the headline; ROC-AUC unchanged at 0.977 ± 0.009 (pipeline untouched).

## Backlog

- Consider time-based split / `Time` feature treatment as a follow-up.
- Class weighting or resampling given 0.173% positives (baseline left imbalance untreated).
