# %% [markdown]
# # Audit — 01_baseline: default skrub tabular pipeline on raw features
#
# Read-only review of the stored report below: its checks and metrics.

# %%
# %% [markdown]
# ## Open the project
#
# Open the same project the experiment wrote to. The init block below
# must match `experiments/01_baseline.py` exactly — copy it from
# there rather than retyping it.
# %%
import json
import os

import skore

from fraud_detection import PROJECT_ROOT

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
project = cv_project
project

# %% [markdown]
# ## List the available reports
#
# `project.summarize()` provides an overview of all reports in this
# Project — useful to confirm the experiment's report landed and to
# spot duplicate keys from accidental re-runs.

# %%
summary = project.summarize()
summary

# %% [markdown]
# ## Load the report
#
# **Hub mode** — `project.put()` prints a URL of the form:
#
#   `https://skore.probabl.ai/workshop-wavestone/<project>/<type-plural>/<N>`
#
# The report id is `skore:report:<type-singular>:<N>`.  The URL path
# segment is the plural; the id uses the singular (drop the trailing
# `s`).  Examples:
#
#   `.../cross-validations/42`  →  `skore:report:cross-validation:42`
#   `.../estimators/7`          →  `skore:report:estimator:7`
#
# Copy `<N>` and `<type-singular>` from the experiment's stdout and
# set `REPORT_ID` below — no `summarize()` traversal needed.
#
# **Local mode** — `project.put()` does not print a URL.  Read the
# `"id"` column value from the `summary` DataFrame above for the row
# whose `"key"` matches this experiment's stem, and set `REPORT_ID` to
# that value.

# %%
REPORT_ID = "skore:report:cross-validation:115"

report = project.get(REPORT_ID)
report

# %% [markdown]
# ## Checks summary
#
# `report.checks.summarize().frame()` returns a DataFrame whose rows
# each carry a `code` (e.g. `SKD003`), a `severity` (`passed` /
# `issue` / `tip`), and a `documentation_url` — the linked page
# describes what the check tests and what to try next.
#
# Available on `EstimatorReport` and `CrossValidationReport` in
# skore ≥ 0.18. Mute a noisy check via
# `report.checks.summarize(ignore=['<code>']).frame()`.
#
# Docs: https://docs.skore.probabl.ai/0.18/user_guide/automated_checks.html

# %%
report.checks.summarize().frame()

# %% [markdown]
# ## Metrics summary
#
# `report.metrics.summarize().frame()` covers task-appropriate
# defaults in one call:
#
# - regression: RMSE / MAE / R² + fit/predict timings,
# - binary classification: accuracy / precision / recall / F1 /
#   ROC-AUC / log-loss + timings,
# - multiclass: macro / micro averages of the above.
#
# Same accessor on both `EstimatorReport` and
# `CrossValidationReport`; the latter additionally reports mean ±
# std across folds. This is the headline reading; the actionable
# findings come from the checks section above.

# %%
report.metrics.summarize().frame()

# %% [markdown]
# ## End of audit
#
# This file is the durable record of how the experiment's report was
# reviewed; re-run it any time to refresh the checks and metrics
# above.
