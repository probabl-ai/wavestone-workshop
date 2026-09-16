# 01_baseline

<!--
Design note for experiments/01_baseline.py (same stem, one to one
with the script). Write and agree on it before creating the script.
-->

## Question / hypothesis

Can a default tabular learner on the raw features establish a strong, comparable fraud-detection baseline under AUPRC — and what does the CV report reveal to iterate on?

## Motivation

- **Sourcing strategy:** my-pick (bootstrap — baseline is forced by workspace defaults)
- **Source(s):**
  - EDA (`data/eda.md`): 0.173% positives → AUPRC of record; zero missingness, all-numeric → minimal preprocessing; strongest discriminants V17/V14/V12/V10 (no leakage-level association).
  - Workshop brief (AGENT.md): baseline must be comparable across participants; custom AUPRC metric mandatory.
- **Why this matters:** every later experiment is judged against this number; establishing a clean, leak-free reference with skrub's defaults removes hand-tuned bias from the comparison.

## Method

- **Files touched:** `src/fraud_detection/data.py`, `src/fraud_detection/pipeline.py`, `src/fraud_detection/evaluate.py`, `experiments/01_baseline.py` (fill template body).
- **Change versus (no) previous experiment:** first declaration. DataOps graph: `skrub.var("data_dir")` → `load_raw` (pandas read of `data/creditcard.csv`) → drop `Class`, `mark_as_X`; `Class` via `mark_as_y`. No cross-row features → marker sits on the loaded frame. Learner at the tail: `skrub.tabular_pipeline("classifier")` (skrub's default tree-ensemble tabular stack — handles scaling internally). No feature engineering: opt-in, after baseline, per workshop rule.
- **Metric:** custom AUPRC registered on the report via `report.metrics.add(make_scorer(average_precision_score, response_method="predict_proba"), name="auprc", position="first")` (signature confirmed against skore 0.25.0: `metrics.add(metric, *, name, greater_is_better, position, **kwargs)`).
- **Cross-validation:** decided at the evaluation step (G-CV-SPLITTER), data-driven. EDA evidence on the table: no group column (rules out GroupKFold); `Time` carries temporal order (favors a time-aware split); extreme imbalance (favors stratification). No splitter is fixed in this note.
- **Skore pushes (workshop convention):** the `CrossValidationReport` → project `wavestone-cv`; the fitted estimator (fit on the full training data) → project `wavestone-leaderboard` (both in hub workspace `workshop-wavestone`). Never mixed.
- **Out of scope for this experiment:** feature engineering (incl. `Time`-of-day derivation), class weighting / resampling, hyperparameter tuning, the held-out leaderboard evaluation against a frozen `test.csv`.

## Risks / things that could invalidate the result

- **AGENTS brief names a frozen `test.csv` as the test set, but only `data/creditcard.csv` exists in the workspace.** The leaderboard push this round carries the fitted estimator; the held-out AUPRC lands in a later turn once `test.csv` appears (or the user clarifies it's derived from `creditcard.csv`). Comparability risk until then.
- Stratified-shuffle CV may be optimistic vs the temporal shift fraud patterns exhibit over `Time`; headline may not transfer to the frozen test set.
- Default learner trains on ~285k rows × 30 features — runtime is fine, but a failing AUPRC near 0.5 would indicate a wiring bug (e.g. y mis-bind), not a modelling insight.
- `skore.evaluate` default (80/20 holdout) is NOT used: an explicit splitter will be chosen at G-CV-SPLITTER, so the result stays CV-comparable.

## Status

- **State:** done
- **Approved by user on:** 2026-09-16
- **Headline result:** CV AUPRC **0.524 ± 0.085** (KFold-5, `train.csv` only); frozen-test (`test.csv`, seed 42) AUPRC **0.438**. ROC-AUC 0.815 ± 0.058; fraud-class precision 0.492, recall 0.725.
- **Implication for next iteration:** skore's own checks flag **SKD002 (near-dummy underfitting)** and **SKD008 (correlated features, tip)** — a plain HistGradientBoosting baseline already scores AUPRC 0.477 on the test slice, so the default stack adds little. Clear headroom: feature engineering (Time-of-day) and tuning; CV-vs-test gap (0.52 → 0.44) hints at temporal drift, worth revisiting the IID-split decision.
