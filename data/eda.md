<!--
Exploratory data analysis summary for this workspace, written from
the data/eda.py run. Ground every claim in what the run actually
showed — do not invent facts. Keep "Modelling implications" as
candidate suggestions to weigh when designing the model, not final
decisions.
-->

# EDA — Kaggle credit-card fraud dataset

_Generated from `data/eda.py` on 2026-09-16._

## Dataset at a glance

- **Tables:** 1 — `creditcard.csv`
- **Shape:** 284,807 × 31
- **Target:** `Class` — binary (0 = legitimate, 1 = fraud)
- **Rich reports:** [eda_creditcard.html](eda_creditcard.html)

## Per-column findings

- All 31 columns are numeric: 30 × `Float64` (`Time`, `V1`–`V28`, `Amount`) + 1 × `Int64` (`Class`).
- **No missing values anywhere** (`null_pct` = 0.0 for every column) — no imputation needed.
- No datetime-typed columns and no high-cardinality id-like column surfaced by the structure pass: `Time` is a float (seconds elapsed) and every PCA feature has low measured unique-ratio signal in the report summary; the digest's unique-ratio table reads 0.0 because `n_unique` was not populated for numeric continuous columns in this report version. Treat `Time` as a continuous elapsed-seconds feature, not a datetime.

## Target

- `Class` is 0/1 with **492 positives out of 284,807 → 0.1727% positive rate** (mean 0.001727, quantiles: 75% still 0).
- Extreme imbalance: bin counts 284,315 (legit) vs 492 (fraud). Accuracy is meaningless here; a trivial all-zeros predictor scores 99.83% accuracy.

## Structure

- No datetime columns. `Time` is seconds elapsed from the first transaction (float), so rows carry a temporal order but no wall-clock column.
- No group/id-like column: each row is a transaction; no `user_id`/card identifier to group on. No `datetime_cols`, no strong unique-ratio column other than `Time` itself.

## Associations

Top feature↔target links (Cramér's V vs `Class`):

| Feature | Cramér's V | Pearson r |
|---|---|---|
| V17 | 0.711 | −0.326 |
| V14 | 0.653 | −0.303 |
| V12 | 0.648 | −0.261 |
| V10 | 0.592 | −0.217 |
| V11 | 0.576 | +0.155 |
| V16 | 0.565 | −0.197 |

- `V17`, `V14`, `V12`, `V10`, `V11`, `V16` are the strongest fraud discriminants; all plausible for PCA components — **no implausibly perfect association → no obvious leakage column**.
- Strong feature↔feature pairs exist (e.g. `V5`↔`V6` 0.700, `V20`↔`Amount` 0.697, `V6`↔`V7` 0.640) — PCA artifacts; tree ensembles tolerate this, linear models may want it noted.
- `Amount` correlates with `V20`, `V7`, `V6` (0.53–0.70).

## Modelling implications

- **Extreme target imbalance (0.173%) →** the metric must be **AUPRC (average precision)**, not accuracy or even ROC-AUC alone; class weights / resampling are candidate levers, not defaults. The workshop mandates a custom AUPRC metric.
- **No missingness / all-numeric features →** the baseline pipeline needs almost no preprocessing beyond what skrub's tabular pipeline does by default; no imputation, no categorical encoding.
- **`Time` carries temporal order →** a `TimeSeriesSplit`-style ordering or a `StratifiedKFold` are both defensible; fraud patterns shift over `Time`, so a stratified shuffle may be optimistic — decide at the G-CV-SPLITTER gate with this evidence on the table. **`test.csv`-style frozen test set: the workshop freezes the held-out set; never tune on it.**
- **No group column →** no `GroupKFold` need.
- **Strong but not perfect univariate signals (V17/V14/V12/V10) →** a simple regularized logistic regression or tree ensemble should beat the trivial baseline comfortably; linear models may suffer from the PCA cross-correlations.

## Open questions

- Should `Time` be used raw, converted to hour-of-day features, or dropped for the baseline?
- Is the frozen `test.csv` a stratified sample or the tail of the time range? (affects how optimistic CV numbers are)
- Any appetite for class-weighting / resampling in the baseline, or keep the first experiment vanilla?
