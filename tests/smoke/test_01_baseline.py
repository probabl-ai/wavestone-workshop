"""Smoke test for ``experiments/01_baseline.py``.

Fits the baseline learner on a slice of the real creditcard data and
predicts on a disjoint slice carried in its own temp directory. The
binding is IID (no cross-row feature steps), so the hard row-count
assertion is a sanity check rather than a cold-start probe; the soft
ROC-AUC floor catches NaN-poisoned or degenerate predictions.
"""


import pandas as pd
import pytest
from sklearn.metrics import roc_auc_score

from fraud_detection import PROJECT_ROOT
from fraud_detection.pipeline import build_learner

# CV headline for the baseline: ROC-AUC 0.977 ± 0.009
# (journal/01_baseline.md § Status). The smoke slice (every 7th row) gets a
# generous floor well below the CV mean; a value under 0.8 would mean
# degenerate predictions, not honest generalization gap.
ROC_AUC_FLOOR = 0.8

DATA_CSV = PROJECT_ROOT / "data" / "creditcard.csv"


@pytest.fixture
def train_predict_envs(tmp_path):
    """Build (train_env, predict_env, n_predict_grid_rows, y_true).

    The learner binds a single ``data_dir`` var, so each env is a temp
    directory holding the sliced CSV. The predict slice carries only the
    rows we want predictions for — no padding beyond that.
    """
    frame = pd.read_csv(DATA_CSV)
    # Disjoint slices: every 7th row is held out for prediction.
    predict = frame.iloc[::7].reset_index(drop=True)
    train = frame.drop(index=frame.index[::7])

    train_dir = tmp_path / "train"
    predict_dir = tmp_path / "predict"
    train_dir.mkdir()
    predict_dir.mkdir()
    train.to_csv(train_dir / "creditcard.csv", index=False)
    predict.to_csv(predict_dir / "creditcard.csv", index=False)

    return (
        {"data_dir": str(train_dir)},
        {"data_dir": str(predict_dir)},
        len(predict),
        predict["Class"],
    )


def test_01_baseline(train_predict_envs):
    """Predict on the held-out slice must yield exactly one prediction per row."""
    train_env, predict_env, n_predict_grid_rows, y_true = train_predict_envs

    learner = build_learner()
    learner.fit(train_env)
    predictions = learner.predict(predict_env)

    # HARD: structural correctness.
    assert len(predictions) == n_predict_grid_rows, (
        f"got {len(predictions)} predictions for "
        f"{n_predict_grid_rows} predict rows — the pipeline is dropping "
        f"rows; check `mark_as_X` placement."
    )

    # SOFT: predictions are not degenerate / NaN-poisoned.
    smoke_auc = roc_auc_score(y_true, predictions)
    assert smoke_auc > ROC_AUC_FLOOR, (
        f"smoke ROC-AUC {smoke_auc:.3f} <= floor {ROC_AUC_FLOOR} "
        f"— predictions may be degenerate; see journal/01_baseline.md."
    )
