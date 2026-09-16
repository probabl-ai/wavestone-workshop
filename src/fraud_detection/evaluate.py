"""Evaluation helpers for the fraud-detection experiments.

The ``skore.evaluate`` / ``Project.put`` calls themselves live in the
``experiments/NN_*.py`` scripts (they are the sole producers of reports in
the skore Project); this module carries the CV strategy and the env-dict
construction they consume.
"""

from sklearn.metrics import average_precision_score, make_scorer
from sklearn.model_selection import KFold

#: Baseline CV strategy: 5-fold shuffled KFold. The ``Time`` column carries
#: an implicit temporal ordering (seconds since the first transaction, ~48h),
#: but the baseline deliberately treats the task as IID and keeps ``Time`` as
#: a plain covariate. Stratified variants are deliberately avoided: they
#: compress across-fold variance and give over-confident error bars on a
#: 0.17%-positive target.
CV_SPLITTER = KFold(n_splits=5, shuffle=True, random_state=0)


def add_auprc(report):
    """Register AUPRC (average precision) as a custom metric on a report.

    AUPRC is the headline metric for this dataset: with 0.17% positives,
    ROC-AUC is inflated by the huge true-negative mass, while average
    precision measures how precisely the model ranks actual frauds.

    Parameters
    ----------
    report : skore.EstimatorReport or skore.CrossValidationReport
        Report whose ``metrics`` namespace receives the custom metric.

    Returns
    -------
    The same report, with AUPRC registered for ``metrics.summarize()``.
    """
    report.metrics.add(
        make_scorer(
            average_precision_score,
            response_method="predict_proba",
            pos_label=1,
        ),
        name="AUPRC",
        greater_is_better=True,
        position="first",
    )
    return report


def make_env(data_dir):
    """Build the SkrubLearner environment dict for one data directory.

    Parameters
    ----------
    data_dir : str or Path
        Directory holding ``creditcard.csv``.

    Returns
    -------
    dict
        ``{"data_dir": <str>}``, mapping the ``skrub.var("data_dir")`` root
        of the pipeline graph to its source value.
    """
    return {"data_dir": str(data_dir)}
