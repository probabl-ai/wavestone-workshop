"""Baseline fraud-detection learner, declared as a skrub DataOps graph."""

import skrub
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from fraud_detection.data import TARGET_COL, load_raw


def build_learner(data_dir_preview=None):
    """Return the unfit baseline learner (skrub SkrubLearner).

    Graph: ``data_dir`` source var -> ``load_raw`` -> mark X/y on the loaded
    frame -> StandardScaler (stateful, fit per training fold) ->
    ``LogisticRegression`` at the tail. No resampling or class weighting at
    the baseline; imbalance behaviour is recorded first, acted on later.

    Parameters
    ----------
    data_dir_preview : str, optional
        Directory holding ``creditcard.csv``, used only for interactive
        ``skb.preview()`` during development. Leave ``None`` for production
        fit / cross-validate; the caller passes the real directory in the
        environment dict.
    """
    data_dir = (
        skrub.var("data_dir", value=str(data_dir_preview))
        if data_dir_preview is not None
        else skrub.var("data_dir")
    )

    # Layer 1 + 2: pure load, then mark X / y on the loaded frame.
    # IID flat table with no cross-row feature steps, so the marker sits here.
    data = data_dir.skb.apply_func(load_raw)
    X = data.drop(columns=[TARGET_COL]).skb.mark_as_X()
    y = data[TARGET_COL].skb.mark_as_y()

    # Layer 3: scaling + estimator. All 28 V-features + Amount + Time are
    # kept intact; scaling makes the penalized logistic regression behave
    # across heavy-tailed Amount and raw Time seconds.
    features = X.skb.apply(StandardScaler())
    predictions = features.skb.apply(
        LogisticRegression(max_iter=1000, random_state=0), y=y
    )
    return predictions.skb.make_learner()
