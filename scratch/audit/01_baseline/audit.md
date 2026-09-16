# Cells: `audit/01_baseline.py`

## Cell 0: `# %% [markdown]`

# Audit — 01_baseline: <what this experiment tested>
#
Read-only review of the stored report below: its checks and metrics.

## Cell 1: `# %%`

```python
import skore

from fraud_detection import PROJECT_ROOT
```

## Cell 2: `# %% [markdown]`

## Open the project
#
Open the same project the experiment wrote to. The init block below
must match `experiments/01_baseline.py` exactly — copy it from
there rather than retyping it.

## Cell 3: `# %%`

```python
# _skore_cfg = json.loads((PROJECT_ROOT / ".skore").read_text())
os.environ.setdefault("SKORE_HUB_URI", _skore_cfg["hub_url"])
os.environ.setdefault("SKORE_HUB_API_KEY", _skore_cfg["api_key"])
assert os.environ.get("SKORE_HUB_API_KEY")
skore.login()
project = skore.Project(
    name="fraud_detection",
    mode="local",
    workspace=str(PROJECT_ROOT / "reports"),
)
project
```

**stdout:**
```
[31m---------------------------------------------------------------------------[39m
[31mNameError[39m                                 Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[1][39m[32m, line 2[39m
[32m      1[39m [38;5;66;03m# _skore_cfg = json.loads((PROJECT_ROOT / ".skore").read_text())[39;00m
[32m----> [39m[32m2[39m [30;43mos[39;49m.environ.setdefault([33m"[39m[33mSKORE_HUB_URI[39m[33m"[39m, _skore_cfg[[33m"[39m[33mhub_url[39m[33m"[39m])
[32m      3[39m os.environ.setdefault([33m"[39m[33mSKORE_HUB_API_KEY[39m[33m"[39m, _skore_cfg[[33m"[39m[33mapi_key[39m[33m"[39m])
[32m      4[39m [38;5;28;01massert[39;00m os.environ.get([33m"[39m[33mSKORE_HUB_API_KEY[39m[33m"[39m)

[31mNameError[39m: name 'os' is not defined
```

**error:** `NameError: name 'os' is not defined`

## Cell 4: `# %% [markdown]`

## List the available reports
#
`project.summarize()` provides an overview of all reports in this
Project — useful to confirm the experiment's report landed and to
spot duplicate keys from accidental re-runs.

## Cell 5: `# %%`

```python
summary = project.summarize()
summary
```

**stdout:**
```
[31m---------------------------------------------------------------------------[39m
[31mNameError[39m                                 Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[1][39m[32m, line 1[39m
[32m----> [39m[32m1[39m summary = [30;43mproject[39;49m.summarize()
[32m      2[39m summary

[31mNameError[39m: name 'project' is not defined
```

**error:** `NameError: name 'project' is not defined`

## Cell 6: `# %% [markdown]`

## Load the report
#
**Hub mode** — `project.put()` prints a URL of the form:
#
  `https://skore.probabl.ai/workshop-wavestone/<project>/<type-plural>/<N>`
#
The report id is `skore:report:<type-singular>:<N>`.  The URL path
segment is the plural; the id uses the singular (drop the trailing
`s`).  Examples:
#
  `.../cross-validations/42`  →  `skore:report:cross-validation:42`
  `.../estimators/7`          →  `skore:report:estimator:7`
#
Copy `<N>` and `<type-singular>` from the experiment's stdout and
set `REPORT_ID` below — no `summarize()` traversal needed.
#
**Local mode** — `project.put()` does not print a URL.  Read the
`"id"` column value from the `summary` DataFrame above for the row
whose `"key"` matches this experiment's stem, and set `REPORT_ID` to
that value.

## Cell 7: `# %%`

```python
REPORT_ID = "skore:report:cross-validation:87"

report = project.get(REPORT_ID)
report
```

**stdout:**
```
[31m---------------------------------------------------------------------------[39m
[31mNameError[39m                                 Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[1][39m[32m, line 3[39m
[32m      1[39m REPORT_ID = [33m"[39m[33mskore:report:cross-validation:87[39m[33m"[39m
[32m----> [39m[32m3[39m report = [30;43mproject[39;49m.get(REPORT_ID)
[32m      4[39m report

[31mNameError[39m: name 'project' is not defined
```

**error:** `NameError: name 'project' is not defined`

## Cell 8: `# %% [markdown]`

## Checks summary
#
`report.checks.summarize().frame()` returns a DataFrame whose rows
each carry a `code` (e.g. `SKD003`), a `severity` (`passed` /
`issue` / `tip`), and a `documentation_url` — the linked page
describes what the check tests and what to try next.
#
Available on `EstimatorReport` and `CrossValidationReport` in
skore ≥ 0.18. Mute a noisy check via
`report.checks.summarize(ignore=['<code>']).frame()`.
#
Docs: https://docs.skore.probabl.ai/0.18/user_guide/automated_checks.html

## Cell 9: `# %%`

```python
report.checks.summarize().frame()
```

**stdout:**
```
[31m---------------------------------------------------------------------------[39m
[31mNameError[39m                                 Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[1][39m[32m, line 1[39m
[32m----> [39m[32m1[39m [30;43mreport[39;49m.checks.summarize().frame()

[31mNameError[39m: name 'report' is not defined
```

**error:** `NameError: name 'report' is not defined`

## Cell 10: `# %% [markdown]`

## Metrics summary
#
`report.metrics.summarize().frame()` covers task-appropriate
defaults in one call:
#
- regression: RMSE / MAE / R² + fit/predict timings,
- binary classification: accuracy / precision / recall / F1 /
  ROC-AUC / log-loss + timings,
- multiclass: macro / micro averages of the above.
#
Same accessor on both `EstimatorReport` and
`CrossValidationReport`; the latter additionally reports mean ±
std across folds. This is the headline reading; the actionable
findings come from the checks section above.

## Cell 11: `# %%`

```python
report.metrics.summarize().frame()
```

**stdout:**
```
[31m---------------------------------------------------------------------------[39m
[31mNameError[39m                                 Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[1][39m[32m, line 1[39m
[32m----> [39m[32m1[39m [30;43mreport[39;49m.metrics.summarize().frame()

[31mNameError[39m: name 'report' is not defined
```

**error:** `NameError: name 'report' is not defined`

## Cell 12: `# %% [markdown]`

## End of audit
#
This file is the durable record of how the experiment's report was
reviewed; re-run it any time to refresh the checks and metrics
above.
