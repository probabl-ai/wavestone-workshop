# %% [markdown]
# # Experiment: 01_baseline
#
# **Date:** 2026-09-16
# **Goal:** default skrub tabular classifier on the raw features, ranked by a
# custom AUPRC metric — the comparable fraud-detection reference for all
# later iterations.
# **Result:** filled in after the run.

# %%
import skore

from fraud_detection import PROJECT_ROOT
from fraud_detection.data import load_dataset
from fraud_detection.evaluate import auprc_scorer, splitter
from fraud_detection.pipeline import build_learner

# %% [markdown]
# ## Paths
#
# `PROJECT_ROOT` comes from the package's `__init__.py` and resolves
# from `__file__` — independent of the current working directory.
# The same absolute path is passed both as the pipeline preview and
# via `data=` to `skore.evaluate`, so `learner.skb.preview()` and
# `skore.evaluate(...)` see the same binding.

# %%
DATA_DIR = PROJECT_ROOT / "data"
TRAIN_CSV = DATA_DIR / "train.csv"
TEST_CSV = DATA_DIR / "test.csv"

# %% [markdown]
# ## Projects
#
# Workshop convention: CV reports go to `wavestone-cv`, the fitted
# estimator (fit on the full training data) to `wavestone-leaderboard`.
# Hub credentials come from the gitignored `.skore` file.

# %%
import json
import os

with (PROJECT_ROOT / ".skore").open() as f:
    _skore_config = json.load(f)
os.environ.setdefault("SKORE_HUB_URI", _skore_config["hub_url"])
os.environ.setdefault("SKORE_HUB_API_KEY", _skore_config["api_key"])

from skore import login

login(mode="hub")

cv_project = skore.Project(
    name="wavestone-cv",
    mode="hub",
    workspace="workshop-wavestone",
)
leaderboard_project = skore.Project(
    name="wavestone-leaderboard",
    mode="hub",
    workspace="workshop-wavestone",
)

# %% [markdown]
# ## Data and learner
#
# `data_dir_preview=DATA_DIR` makes `learner.skb.preview()` work; it
# does not affect what `skore.evaluate` actually fits on (that comes
# from `data=` below). `load_dataset()` stays in the namespace for
# interactive inspection; the DataOps graph binds the directory, not
# the materialized frame.

# %%
X, y = load_dataset(str(TRAIN_CSV))
learner = build_learner(csv_path_preview=TRAIN_CSV)

# %% [markdown]
# ## Evaluate
#
# CV runs on the frozen **train** split only (`train.csv`); `test.csv`
# is held out for the leaderboard report. `splitter` (KFold,
# user-picked IID treatment at the G-CV-SPLITTER gate) and the AUPRC
# scorer come from `fraud_detection.evaluate`. `SkrubLearner.fit`
# takes a single environment dict (it does *not* implement
# `fit(X, y)`), so bindings pass via `data=`.

# %%
report = skore.evaluate(learner, data={"csv_path": str(TRAIN_CSV)}, splitter=splitter)
report

# %% [markdown]
# ## Custom AUPRC metric
#
# The workshop's metric of record. Registered at position "first" so
# every summarize() view leads with AUPRC.

# %%
report.metrics.add(auprc_scorer, name="auprc", position="first")
report.metrics.summarize()

# %% [markdown]
# ## Fitted estimator for the leaderboard
#
# Fit on the full train split, evaluate on the frozen test split.
# `EstimatorReport` with env-dict bindings is the persistable form of
# a fitted skrub learner.

# %%
leaderboard_report = skore.EstimatorReport(
    learner,
    train_data={"csv_path": str(TRAIN_CSV)},
    test_data={"csv_path": str(TEST_CSV)},
    pos_label=1,
)
leaderboard_report.metrics.add(auprc_scorer, name="auprc", position="first")
leaderboard_report.metrics.summarize()

# %% [markdown]
# ## Persist
#
# Keys = file stems (`01_baseline` for the CV report, `01_baseline_fitted`
# for the leaderboard). Reusing a key in a future run overwrites the
# stored artifact — fork into a new experiment file if you want both.

# %%
cv_project.put("01_baseline", report)
leaderboard_project.put("01_baseline_fitted", leaderboard_report)
