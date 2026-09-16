"""Smoke test for `experiments/01_baseline.py`.

Diagnostic shape: two disjoint real-data slices, each written to its
own temp directory as `creditcard.csv` — the source binding the
pipeline consumes. The predict slice carries no pre-history buffer;
the hard assertion is one prediction per predict row.
"""

from __future__ import annotations

import pandas as pd
import pytest

from fraud_detection import PROJECT_ROOT
from fraud_detection.pipeline import build_learner

N_TRAIN = 4000
N_FRAUD_TRAIN = 492
N_PREDICT = 2000
RANDOM_STATE = 0


def _write_slice(frame: pd.DataFrame, directory, name: str) -> str:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / name
    frame.to_csv(path, index=False)
    return str(path)


@pytest.fixture
def train_predict_envs(tmp_path):
    """Build `(train_env, predict_env, n_predict_grid_rows)`.

    Predict env is disjoint from the train slice and deliberately
    carries only the rows we want predictions for.
    """
    raw = pd.read_csv(PROJECT_ROOT / "data" / "creditcard.csv")
    frauds = raw[raw["Class"] == 1]
    legits = raw[raw["Class"] == 0]

    train_legits = legits.sample(n=N_TRAIN, random_state=RANDOM_STATE)
    train = pd.concat(
        [train_legits, frauds.sample(n=N_FRAUD_TRAIN, random_state=RANDOM_STATE)]
    )
    remaining = raw.drop(train_legits.index).drop(frauds.index)
    predict = remaining.sample(n=N_PREDICT, random_state=RANDOM_STATE)

    train_env = {"csv_path": _write_slice(train, tmp_path / "train", "train.csv")}
    predict_env = {"csv_path": _write_slice(predict, tmp_path / "predict", "test.csv")}
    return train_env, predict_env, len(predict)


def test_01_baseline(train_predict_envs):
    """Predict-time replay must produce one prediction per predict row."""
    train_env, predict_env, n_predict_grid_rows = train_predict_envs

    learner = build_learner()
    learner.fit(train_env)
    predictions = learner.predict(predict_env)

    assert len(predictions) == n_predict_grid_rows, (
        f"got {len(predictions)} predictions for {n_predict_grid_rows} "
        f"predict-grid rows — pipeline is dropping rows; check `mark_as_X` "
        f"placement in src/fraud_detection/pipeline.py."
    )

    # SOFT: skipped — no CV headline exists yet (experiment not run).
    # Pin an AUPRC-vs-CV-mean bound here once
    # journal/01_baseline.md § Status.headline lands.
