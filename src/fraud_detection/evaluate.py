"""Inputs to `skore.evaluate`.

Holds only the objects passed to `skore.evaluate(...)`:

- `splitter` — the cross-validator,
- optional metric overrides (skore picks task-appropriate defaults
  otherwise).

The evaluation itself — running `skore.evaluate`, opening a project,
persisting the report — happens in the experiment scripts, not here.
"""

from __future__ import annotations

from sklearn.metrics import average_precision_score, make_scorer
from sklearn.model_selection import KFold

# G-CV-SPLITTER pick (2026-09-16): user chose to treat the 2-day window
# as IID and ignore the `Time` ordering. Extreme class imbalance does
# not drive splitter choice, so no stratified variant.
splitter = KFold(n_splits=5, shuffle=True, random_state=0)

# Workshop metric of record: AUPRC (average precision). Registered on
# the produced reports via `report.metrics.add(auprc_scorer, ...)`.
auprc_scorer = make_scorer(
    average_precision_score, response_method="predict_proba", pos_label=1
)
