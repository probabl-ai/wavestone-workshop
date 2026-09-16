# 01_baseline

<!--
Design note for experiments/01_baseline.py (same stem, one to one
with the script). Write and agree on it before creating the script.
-->

## Question / hypothesis

Can a simple, all-numeric baseline learner separate fraud from
legitimate transactions well enough (PR-AUC / ROC-AUC under CV) to
serve as the reference point for all later fraud-detection
experiments?

## Motivation

- **Sourcing strategy:** bootstrap default (forced — first experiment;
  no sourcing menu in bootstrap mode).
- **Source(s):**
  - `data/eda.md` (2025-09-15): 284,807 × 31, all numeric, zero
    missing; target `Class` 0.173% positive; strongest signal in PCA
    components `V17`, `V14`, `V12`, `V10` (Cramér's V 0.59–0.71).
- **Why this matters:** every later improvement (feature engineering,
  resampling, model family) needs a defensible reference number. The
  EDA shows a strong, nearly-linear signal in the V-features, so a
  regularized linear model is the natural baseline before adding any
  complexity.

## Method

- **Files touched:** `src/fraud_detection/data.py` (load + X/y split,
  read-only view of `data/creditcard.csv`), `src/fraud_detection/
  pipeline.py` (declare the learner as a skrub DataOps graph with an
  early X marker), `src/fraud_detection/evaluate.py` (CV evaluation
  via `skore.evaluate`).
- **Change versus baseline:** n/a — this **is** the baseline.
- **Pipeline shape:** keep the raw feature set intact (all 28 V
  features + `Amount` + `Time`); scale the heavy-tailed `Amount`
  (and other features) so a penalized logistic regression behaves;
  no imputation needed (zero missing). Learner: `LogisticRegression`
  with default regularization. No resampling, no class weights in the
  baseline — record imbalance behaviour first, act on it later.
- **Cross-validation:** decided at the evaluation step, data-driven from the
  data's structure — the EDA shows extreme imbalance and no groups, so
  stratification is the strong prior, but the splitter is chosen at
  `G-CV-SPLITTER` (evaluate step), not fixed here.
  **Resolved 2025-09-15 at G-CV-SPLITTER:** user picked *KFold ignoring time
  (IID)* → `KFold(n_splits=5, shuffle=True, random_state=0)` in
  `evaluate.py`; the `Time` column stays a plain covariate.
- **Metrics:** defaults from `skore.evaluate` for binary
  classification (incl. ROC-AUC and average precision / PR-AUC);
  accuracy is explicitly not the headline given the 0.173% positives.
  `pos_label=1` (fraud).
- **Out of scope for this experiment:** feature engineering
  (`Time`→cyclical, `Amount` log-transform, feature selection),
  resampling / class weighting, non-linear model families, time-based
  holdout. The frozen `test.csv`-style holdout is not built here.

## Risks / things that could invalidate the result

- **Class imbalance:** with 0.173% positives, a stratified splitter is
  effectively mandatory; an unstratified fold could contain zero or
  two frauds and swing the PR-AUC wildly. If the chosen splitter
  doesn't stratify, the result is not interpretable.
- **`Time` as a plain numeric feature:** its raw seconds-since-first-
  transaction encoding may make the model learn a spurious trend;
  accept for the baseline, flag for a follow-up.
- **CV-on-imbalanced-data optimism:** shuffling across time ignores
  the deployment reality of scoring future transactions; the headline
  number will be optimistic relative to a temporal split. Noted, not
  fixed in the baseline.
- **Leakage risk is low** — no groups, no post-outcome columns (the
  V-features are PCA of transaction features; `Class` is the label).

## Status

- **State:** done
- **Approved by user on:** 2025-09-15 — user quote: "Please run the baseline now, I approve"
- **Headline result:** 5-fold shuffled KFold — **AUPRC 0.760 ± 0.027** (custom
  metric, added 2025-09-15), ROC-AUC **0.977 ± 0.009**, Precision 0.876 ± 0.025,
  Recall 0.613 ± 0.058. Hub: CV → [wavestone-cv #101](https://saint-gobain.skore.probabl.ai/workshop-wavestone/wavestone-cv/cross-validations/101); fitted →
  [wavestone-leaderboard #107](https://saint-gobain.skore.probabl.ai/workshop-wavestone/wavestone-leaderboard/estimators/107) (re-pushed with AUPRC; superseded #94/#100).
- **Implication for next iteration:** Strong linear signal; next levers are class weighting / PR-focused training, or a temporal split to check optimism of the IID KFold headline.
