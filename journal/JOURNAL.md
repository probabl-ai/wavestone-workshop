# JOURNAL

<!--
Durable index of every experiment in this workspace. Four sections,
in order: Status, Data understanding (EDA), History, Backlog — keep
them so the file stays quick to scan. Each journal/NN_short_name.md
design note pairs one-to-one with experiments/NN_short_name.py (same
stem).
-->

## Status

- **Project / dataset:** Kaggle credit-card fraud detection (`mlg-ulb/creditcardfraud`, ~284,807 × 31; target `Class`, ~0.173% positives)
- **Goal:** a strong, comparable fraud-detection baseline, then iterative improvements; primary ranking metric is **AUPRC** (custom metric), never accuracy
- **Last experiment:** 01_baseline — done
- **Last result:** CV AUPRC 0.524 ± 0.085 (train.csv, KFold-5); frozen-test AUPRC 0.438 (test.csv, seed 42)

<!--
Workspace decisions: one-time project-setup choices. Record each when
it is made and treat it as fixed unless you deliberately change one
(e.g. switch pandas → polars), updating the recorded date. Reading
this block on later sessions avoids re-deciding what's already settled.
-->

- **Workspace decisions** (immutable unless the user pivots):
  - tabular library: pandas — recorded: 2026-09-16
  - env manager: uv — recorded: 2026-09-16
  - agent feature: installed — recorded: 2026-09-16
  - optional features: none — recorded: 2026-09-16
  - package name (`src/fraud_detection/`): fraud_detection — recorded: 2026-09-16
  - skore mode: hub — recorded: 2026-09-16
  - skore hub workspace: workshop-wavestone — recorded: 2026-09-16
  - skore mlflow tracking uri: n/a — recorded: 2026-09-16
  - frozen test split: `data/test.csv`, 20% stratified on `Class`, seed 42 (`scratch/make_test_split.py`); CV binds `data/train.csv` only, test.csv is never trained/tuned on — recorded: 2026-09-16 (user decision at G-RUN)
  - CV splitter family: KFold(n_splits=5, shuffle=True, random_state=0) — user pick at G-CV-SPLITTER, treating the 2-day window as IID (time ignored) — recorded: 2026-09-16

## Data understanding (EDA)

<!--
Short index entry — the full analysis lives in data/eda.md. If the
data exploration was skipped, keep just the Status: skipped line.
-->

- **Status:** done — 2026-09-16
- **Summary:** 284,807 × 31 single table, all numeric, zero missing values. Extreme target imbalance: 492 frauds (0.173%) → AUPRC is the metric of record, accuracy is meaningless. Strongest fraud discriminants: V17, V14, V12, V10, V11, V16 (no leakage-level association). No group column; `Time` carries temporal order, so CV strategy (stratified vs time-aware) is a live decision for the G-CV-SPLITTER gate.
- **Summary:** <2–4 lines — dataset shape, target balance/skew, and the
  one or two findings that most shape the modelling choices. "n/a"
  until the data has been explored.>
- **Report:** [data/eda.md](../data/eda.md)

## History

<!--
One row per experiment, in chronological order. Newest at the bottom.
Status values: planned | approved | running | done | abandoned.
-->

| Stem | Intent (one line) | Status | Headline result | Design note |
|---|---|---|---|---|
| 01_baseline | tabular_pipeline on raw features, custom AUPRC metric | done | CV AUPRC 0.524 ± 0.085; frozen-test AUPRC 0.438 | [design note](01_baseline.md) |

## Backlog

<!--
Ideas not yet committed to a journal/NN_*.md design note. Each row
has a stable B<N> index so it can be picked by number ("go with B2").

Columns:
  - #      — stable index (B1, B2, ...); don't renumber on removal.
  - Item   — one-line description of the idea.
  - Source — where it came from, e.g. a finding from a prior
             experiment's report (`skore:<stem>`), a synthesized idea
             (`my-pick:<stem>`), or a user request (`user`).

When an item becomes a design note, remove its row here and add the
experiment to History above.
-->

| # | Item | Source |
|---|---|---|
| <!-- B1 --> | <!-- "investigate target-bin>0.95 residual bias via target transform" --> | <!-- `skore:01_baseline` --> |
| <!-- B2 --> | <!-- "audit hourly-vs-15min data resolution split — likely fix for fold variance" --> | <!-- `my-pick:02_calendar_features` --> |
