"""Create the frozen train/test split for the workshop leaderboard.

One-off, deterministic: seed 42, stratified on `Class` so the 0.173%
fraud rate holds in the 20% test slice. Writes data/train.csv and
data/test.csv. Re-running reproduces byte-identical files.
"""

import pathlib

import pandas as pd
from sklearn.model_selection import train_test_split

DATA = pathlib.Path("data")
raw = pd.read_csv(DATA / "creditcard.csv")

train, test = train_test_split(
    raw, test_size=0.2, random_state=42, stratify=raw["Class"]
)

train.to_csv(DATA / "train.csv", index=False)
test.to_csv(DATA / "test.csv", index=False)

print(f"train: {len(train)} rows, {train['Class'].sum()} frauds")
print(f"test:  {len(test)} rows, {test['Class'].sum()} frauds")
