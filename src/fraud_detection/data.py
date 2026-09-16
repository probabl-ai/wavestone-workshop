"""Data loading for the creditcard fraud dataset (read-only view of the raw CSV)."""

from pathlib import Path

import pandas as pd

TARGET_COL = "Class"


def load_raw(data_dir: str) -> pd.DataFrame:
    """Load the raw creditcard transactions from ``<data_dir>/creditcard.csv``.

    The file is all-numeric with no missing values (see ``data/eda.md``), so
    the loader does nothing beyond reading the CSV.

    Parameters
    ----------
    data_dir : str
        Directory containing ``creditcard.csv``.

    Returns
    -------
    pd.DataFrame
        The 284,807 × 31 transaction table with the binary ``Class`` column.
    """
    return pd.read_csv(Path(data_dir) / "creditcard.csv")
