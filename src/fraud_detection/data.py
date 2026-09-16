"""Data loading and X-marker wiring.

Owns: how raw data is materialized into `(X, y)`, and how structural
metadata (groups, time ordering, ...) is attached at the X marker via
`split_kwargs`. Data paths are decided by the caller — this module
does not invent a `data/` directory.
"""

from __future__ import annotations

import pandas as pd

TARGET_COL = "Class"


def load_raw(csv_path: str):
    """Load a credit-card transaction CSV.

    Parameters
    ----------
    csv_path : str
        Absolute path to the CSV file (`train.csv` or `test.csv`,
        the frozen split produced by `scratch/make_test_split.py`).

    Returns
    -------
    pandas.DataFrame
        The full table (features + `Class`).
    """
    return pd.read_csv(csv_path)


def load_dataset(csv_path: str):
    """Return `(X, y)` ready for the pipeline.

    Parameters
    ----------
    csv_path : str
        Absolute path to the CSV file (`train.csv` or `test.csv`).

    Returns
    -------
    tuple of (pandas.DataFrame, pandas.Series)
        Features (all columns except `Class`) and the binary `Class`
        target (0 = legitimate, 1 = fraud).
    """
    data = load_raw(csv_path)
    return data.drop(columns=[TARGET_COL]), data[TARGET_COL]
