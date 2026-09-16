# %% [markdown]
# # 01 — Baseline: logistic regression on the raw creditcard features
#
# Declared skrub DataOps learner (`fraud_detection.pipeline.build_learner`),
# evaluated with 5-fold shuffled KFold (the IID reading chosen for the
# baseline) through `skore.evaluate`, with AUPRC (average precision)
# registered as a custom metric on both reports. Hub routing (see AGENT.md):
# CV report → `wavestone-cv`; fitted EstimatorReport → `wavestone-leaderboard`.

# %%
import json
import os

import skore

from fraud_detection import PROJECT_ROOT
from fraud_detection.evaluate import CV_SPLITTER, add_auprc, make_env
from fraud_detection.pipeline import build_learner

# Hub auth: the gitignored .skore file carries the credentials; the skore
# library reads them from the environment. Never print the key.
_skore_cfg = json.loads((PROJECT_ROOT / ".skore").read_text())
os.environ.setdefault("SKORE_HUB_URI", _skore_cfg["hub_url"])
os.environ.setdefault("SKORE_HUB_API_KEY", _skore_cfg["api_key"])

# skore 0.25 hub mode requires a login() call before Project(...). With
# SKORE_HUB_API_KEY set this resolves via the API-key header — no browser,
# no interactive auth.
assert os.environ.get("SKORE_HUB_API_KEY")
skore.login()

# %% [markdown]
# ## Cross-validation report

# %%
DATA_DIR = PROJECT_ROOT / "data"
learner = build_learner()
cv_report = skore.evaluate(
    learner,
    data=make_env(DATA_DIR),
    splitter=CV_SPLITTER,
    pos_label=1,
)
add_auprc(cv_report)
print(cv_report)

# %% [markdown]
# ## Fitted estimator (paired with the CV report)
#
# Built unfitted below so EstimatorReport can fit it and record the train
# features; in-sample metrics here are reference only — the honest headline
# lives in the CV report (no separate holdout is spent at the baseline).
# Unfitted learner: EstimatorReport fits it on train_data itself, so the
# report carries train features (required for serialization) and the fitted
# estimator the workshop rule pairs with the CV report.
fitted_report = skore.EstimatorReport(
    build_learner(),
    train_data=make_env(DATA_DIR),
    test_data=make_env(DATA_DIR),
    pos_label=1,
)
add_auprc(fitted_report)

# %% [markdown]
# ## Push to Hub (per AGENT.md routing)
#
# - Cross-validation → `wavestone-cv`
# - Fitted train/eval report → `wavestone-leaderboard`

# %%
workspace = _skore_cfg["workspace"]
cv_project = skore.Project("wavestone-cv", mode="hub", workspace=workspace)
cv_project.put("01_baseline", cv_report)
print("pushed CV report to wavestone-cv")

lb_project = skore.Project("wavestone-leaderboard", mode="hub", workspace=workspace)
lb_project.put("01_baseline", fitted_report)
print("pushed fitted EstimatorReport to wavestone-leaderboard")
