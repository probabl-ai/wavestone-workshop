# Cells: `audit/01_baseline.py`

## Cell 0: `# %% [markdown]`

# Audit — 01_baseline: default skrub tabular pipeline on raw features
#
Read-only review of the stored report below: its checks and metrics.

## Cell 1: `# %%`

## Cell 2: `# %% [markdown]`

## Open the project
#
Open the same project the experiment wrote to. The init block below
must match `experiments/01_baseline.py` exactly — copy it from
there rather than retyping it.

## Cell 3: `# %%`

```python
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
```

**stdout:**
```
╭───────────────────────────────── Login to Skore Hub ─────────────────────────────────╮
│                                                                                      │
│                        Successfully logged in, using API key.                        │
│                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────╯
Out[0]: Project(name='wavestone-cv', mode='hub', workspace='workshop-wavestone')
```

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
Out[0]: 
                                                                report_id  \
  id                                                                        
0 skore:report:cross-validation:94   01a0a96e-5651-7277-869b-22fd10a6fb65   
1 skore:report:cross-validation:101  01a0a980-4cb1-7f3b-be2d-6595728e9402   
2 skore:report:cross-validation:108  01a0a9d4-d088-7c28-894a-37efb3eabca8   
3 skore:report:cross-validation:115  01a0a9d7-a326-708f-b6ce-9338ff1fbe4b   

                                             key  \
  id                                               
0 skore:report:cross-validation:94   01_baseline   
1 skore:report:cross-validation:101  01_baseline   
2 skore:report:cross-validation:108  01_baseline   
3 skore:report:cross-validation:115  01_baseline   

                                                                date  \
  id                                                                   
0 skore:report:cross-validation:94  2026-09-16 08:57:55.040100+00:00   
1 skore:report:cross-validation:101 2026-09-16 09:17:17.262835+00:00   
2 skore:report:cross-validation:108 2026-09-16 10:50:19.761839+00:00   
3 skore:report:cross-validation:115 2026-09-16 10:53:04.348219+00:00   

                                          learner                ml_task  \
  id                                                                       
0 skore:report:cross-validation:94   SkrubLearner  binary-classification   
1 skore:report:cross-validation:101  SkrubLearner  binary-classification   
2 skore:report:cross-validation:108  SkrubLearner  binary-classification   
3 skore:report:cross-validation:115  SkrubLearner  binary-classification   

                                          report_type  \
  id                                                    
0 skore:report:cross-validation:94   cross-validation   
1 skore:report:cross-validation:101  cross-validation   
2 skore:report:cross-validation:108  cross-validation   
3 skore:report:cross-validation:115  cross-validation   

                                                              dataset  rmse  \
  id                                                                          
0 skore:report:cross-validation:94   3fcd137b7952dc1fb7a01efe5a9aedf1  None   
1 skore:report:cross-validation:101  3fcd137b7952dc1fb7a01efe5a9aedf1  None   
2 skore:report:cross-validation:108  7c4b9da01c803d3c82ec34d2fd5ce89c  None   
3 skore:report:cross-validation:115  7c4b9da01c803d3c82ec34d2fd5ce89c  None   

                                     log_loss   roc_auc  fit_time  \
  id                                                                
0 skore:report:cross-validation:94   0.004109  0.976778  0.810804   
1 skore:report:cross-validation:101  0.004109  0.976778  0.708487   
2 skore:report:cross-validation:108  0.033753  0.809786  4.248568   
3 skore:report:cross-validation:115  0.033129  0.815401  3.087809   

                                     predict_time rmse_std  log_loss_std  \
  id                                                                       
0 skore:report:cross-validation:94       0.028572     None      0.000481   
1 skore:report:cross-validation:101      0.022084     None      0.000481   
2 skore:report:cross-validation:108      0.252166     None      0.009227   
3 skore:report:cross-validation:115      0.121210     None      0.010521   

                                     roc_auc_std  fit_time_std  \
  id                                                             
0 skore:report:cross-validation:94      0.009152      0.125627   
1 skore:report:cross-validation:101     0.009152      0.111381   
2 skore:report:cross-validation:108     0.050356      0.582922   
3 skore:report:cross-validation:115     0.057641      0.188982   

                                     predict_time_std  
  id                                                   
0 skore:report:cross-validation:94           0.008786  
1 skore:report:cross-validation:101          0.007002  
2 skore:report:cross-validation:108          0.110503  
3 skore:report:cross-validation:115          0.017027  
```

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
REPORT_ID = "skore:report:cross-validation:115"

report = project.get(REPORT_ID)
report
```

**stdout:**
```
Out[0]: 










CrossValidationReport:
        'SkrubLearner'

                                    mean       std
Metric           Label                    
Auprc                   0.523743  0.084982
Score                   0.998209  0.000273
Accuracy                0.998209  0.000273
Precision        0      0.999520  0.000139
                 1      0.491876  0.036495
Recall           0      0.998685  0.000272
                 1      0.725496  0.069195
ROC AUC                 0.815401  0.057641
Log loss                0.033129  0.010521
Brier score             0.001666  0.000289
Fit time (s)            3.087809  0.188982
Predict time (s)        0.112758  0.013584
        Call `report.to_markdown()` for a markdown summary of the report's contents.
```

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








Out[0]: 
      code                                                title  \
0   SKD001                                Potential overfitting   
1   SKD002                               Potential underfitting   
2   SKD003               Inconsistent performance across splits   
3   SKD004                                 High class imbalance   
4   SKD005                             Underrepresented classes   
5   SKD006                           Coefficient interpretation   
6   SKD007             MDI biased for high-cardinality features   
7   SKD008                     Highly correlated input features   
8   SKD009  Model performance vs. HistGradientBoosting baseline   
9   SKD010                           Model slower than baseline   
10  SKD011                                       Golden feature   
11  SKD012                                     Useless features   
12  SKD013                    Train-test overlap in time series   
13  SKD014                       Hyperparameters at search edge   
14  SKD015                         Hyperparameters worth tuning   
15  SKD016                                  Estimator not tuned   

           section  \
0           passed   
1            issue   
2           passed   
3            issue   
4   not_applicable   
5   not_applicable   
6   not_applicable   
7           passed   
8              tip   
9           passed   
10  not_applicable   
11  not_applicable   
12  not_applicable   
13  not_applicable   
14  not_applicable   
15  not_applicable   

                                                                                                                                                                                                                                                                                       explanation  \
0                                                                                                                                                                                                                                                                                              NaN   
1                                                                                                                                                                                   Train/test scores are on par and not significantly better than the dummy baseline for 6/10 comparable metrics.   
2                                                                                                                                                                                                                                                                                              NaN   
3                                                                                     Class [0] represents more than 80% of the dataset samples. Accuracy should not be used alone to assess model performance as it may be misleading by ignoring poor performance on the underrepresented class.   
4                                                                                                                                                                                                                             ML task is not multiclass classification. Got binary-classification.   
5                                                                                                                                                                                                                           Estimator is not a linear model: it does not have a `coef_` attribute.   
6                                                                                                                                                                                                        Estimator is not a tree-based model: it does not have a `feature_importances_` attribute.   
7                                                                                                                                                                                                                                                                                              NaN   
8   Your model is on par with or better than a HistGradientBoosting baseline. Baseline performance on the test set, for reference: Accuracy=0.998, Auprc=0.477, Brier score=0.00163, Log loss=0.0338, Precision (0)=0.999, Precision (1)=0.498, ROC AUC=0.791, Recall (0)=0.999, Recall (1)=0.669.   
9                                                                                                                                                                                                                                                                                              NaN   
10                                                                                                                                                                                                                                                    Failed to create report from single feature.   
11                                                                                                                                                                                                                                                       Failed to compute permutation importance.   
12                                                                                                                                                                                                                                                                       No datetime column found.   
13                                                                                                                                                                                                                                     Estimator is not a BaseSearchCV instance. Got SkrubLearner.   
14                                                                                                                                                                                                                                     Estimator is not a BaseSearchCV instance. Got SkrubLearner.   
15                                                                                                                                                                                                                                                    No parameter to recommend for the estimator.   

                                                                                          documentation_url  
0                    https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd001-overfitting  
1                   https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd002-underfitting  
2       https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd003-inconsistent-performance  
3           https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd004-high-class-imbalance  
4       https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd005-underrepresented-classes  
5          https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd006-unscaled-coefficients  
6           https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd007-mdi-cardinality-bias  
7            https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd008-correlated-features  
8            https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd009-worse-than-baseline  
9           https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd010-slower-than-baseline  
10                https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd011-golden-feature  
11              https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd012-useless-features  
12       https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd013-train-test-time-overlap  
13    https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd014-hyperparams-at-search-edge  
14  https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd015-hyperparameters-worth-tuning  
15           https://docs.skore.probabl.ai/0.25/user_guide/automated_checks.html#skd016-estimator-not-tuned  
```

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

Out[0]: 
              skrublearner_mean  skrublearner_std
auprc                  0.523743          0.084982
score                  0.998209          0.000273
accuracy               0.998209          0.000273
precision_0            0.999520          0.000139
precision_1            0.491876          0.036495
recall_0               0.998685          0.000272
recall_1               0.725496          0.069195
roc_auc                0.815401          0.057641
log_loss               0.033129          0.010521
brier_score            0.001666          0.000289
fit_time               3.087809          0.188982
predict_time           0.112758          0.013584
```

## Cell 12: `# %% [markdown]`

## End of audit
#
This file is the durable record of how the experiment's report was
reviewed; re-run it any time to refresh the checks and metrics
above.
