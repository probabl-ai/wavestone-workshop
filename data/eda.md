# EDA — Credit card fraud (Kaggle mlg-ulb/creditcardfraud)

_Generated from `data/eda.py` on 2025-09-15._

## Dataset at a glance

- **Tables:** 1 — `creditcard.csv`
- **Shape:** 284,807 rows × 31 columns
- **Target:** `Class` (binary: 0 = legitimate, 1 = fraud)
- **Rich reports:** [eda_creditcard.html](eda_creditcard.html)

## Per-column findings

- 31 columns, **zero missing values anywhere** (`null_pct = 0.0` for all).
- All predictors are numeric: 28 PCA-anonymized features (`V1`–`V28`),
  plus `Time` (seconds elapsed since first transaction) and `Amount`
  (transaction amount, both float). `Class` is int64.
- No constant columns, no string/categorical columns, no text.

## Target

- **Severely imbalanced:** 492 frauds out of 284,807 transactions —
  **0.173% positive class** (mean of `Class` = 0.00173).
- Accuracy is meaningless here; the baseline majority classifier would
  score 99.83% while detecting nothing.

## Structure

- **No datetime-typed columns.** `Time` is a numeric offset in seconds
  from the first transaction — the rows are implicitly time-ordered.
- **No entity/id-like column.** The V-features are per-transaction PCA
  components; no customer/card identifier repeats across rows. There is
  no obvious grouping key for `GroupKFold`.

## Associations

Strongest feature↔target links (Cramér's V with `Class`):

| Feature | Cramér's V | Pearson |
|---|---|---|
| `V17` | 0.711 | −0.33 |
| `V14` | 0.653 | −0.30 |
| `V12` | 0.648 | −0.26 |
| `V10` | 0.592 | −0.22 |
| `V11` | 0.576 | +0.15 |
| `V16` | 0.565 | −0.20 |

- These PCA components are strong candidate predictors — plausible for
  fraud detection, not an implausibly perfect signal (nothing near 1.0),
  so **no leakage flag**.
- Notable feature↔feature links (`V5`–`V6`, `V6`–`V7`, `V7`–`Amount`,
  `V20`–`Amount`) are moderate, not collinear enough to force action.

## Modelling implications

- **Extreme class imbalance (0.173%)** → cross-validation should be
  `StratifiedKFold`; report **ROC-AUC / PR-AUC (average precision)**,
  not accuracy.
- **Time-ordered rows, no groups** → a plain stratified split is
  defensible for the baseline; if the deployment story is "model sees
  future transactions", a time-based split on `Time` is a candidate
  follow-up experiment.
- **All-numeric, no missing values** → no imputation needed; scaling may
  still matter for `Amount` (heavy-tailed) if a linear model is chosen.
- **Strong linear-ish signal in V17/V14/V12/V10** → a logistic
  regression baseline is a reasonable start; tree ensembles likely
  improve PR-AUC.
- **No categorical / text features** → no encoding step needed in the
  pipeline.

## Open questions

- Should the baseline treat `Time` as a feature (seconds-of-day cycles)
  or drop it?
- Is `Amount` to be used raw, log-transformed, or scaled?
- Do we owe the evaluation a fixed holdout (`test.csv` per workshop
  rules) in addition to CV, and if so how should it be carved from the
  time-ordered data?
