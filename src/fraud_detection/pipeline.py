"""Learner declaration.

Owns: the function that builds and returns the (unfit) learner —
typically a `SkrubLearner` produced from a skrub DataOps graph that
composes the steps in `data.py` and `features.py` with the chosen
estimator. Fitting, evaluation, and persistence happen elsewhere.

Note on the source-binding preview. When the graph roots a
`skrub.var(name, value=...)` on a source identifier (path, URL,
table name), the `value` is the **preview** — the binding used by
`learner.skb.preview()` while iterating interactively. The preview
is intentionally exposed as an **optional** keyword on
`build_learner` so the caller (typically the experiment script) can
pass an absolute path resolved from the package root, instead of a
CWD-relative literal baked into this file. Without a preview, the
graph still fits and evaluates — only `.skb.preview()` is
unavailable.
"""

from __future__ import annotations

from pathlib import Path

import skrub

from fraud_detection.data import TARGET_COL, load_raw


def build_learner(csv_path_preview: str | Path | None = None):
    """Return the unfit learner for the experiment scripts to consume.

    Parameters
    ----------
    csv_path_preview : str or Path or None, optional
        Preview value for the source-bound `skrub.var("csv_path", ...)`
        root. Pass an absolute path (e.g. `fraud_detection.PROJECT_ROOT / "data"`)
        when iterating interactively so `learner.skb.preview()` works.
        Leave as `None` for fit / cross-validate runs — the env-dict
        passed to `skore.evaluate(..., data={"csv_path": ...})`
        supplies the binding regardless.

    Returns
    -------
    skrub.SkrubLearner
        The unfit learner: raw load → X/y markers → skrub's default
        tabular classifier stack.
    """
    csv_path = (
        skrub.var("csv_path", value=str(csv_path_preview))
        if csv_path_preview is not None
        else skrub.var("csv_path")
    )

    data = csv_path.skb.apply_func(load_raw)
    X = data.drop(columns=[TARGET_COL]).skb.mark_as_X()
    y = data[TARGET_COL].skb.mark_as_y()

    classifier = skrub.tabular_pipeline("classifier")
    predictions = X.skb.apply(classifier, y=y)
    return predictions.skb.make_learner()
