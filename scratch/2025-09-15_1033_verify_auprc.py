"""Verify metrics.add('average_precision') works on a CV report (small data)."""

from sklearn.base import clone
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import get_scorer
from sklearn.model_selection import StratifiedKFold
from skore import CrossValidationReport

from fraud_detection.evaluate import add_auprc

X, y = make_classification(n_samples=300, weights=[0.99, 0.01], random_state=0)
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=0)
est = get_scorer  # noqa (keep imports tidy)
rep = CrossValidationReport(
    clone(LogisticRegression(max_iter=200)), X=X, y=y, splitter=cv
)
add_auprc(rep)
summary = rep.metrics.summarize().frame()
print(summary)
assert "AUPRC" in summary.index or "AUPRC" in summary.columns, summary.columns
print("OK: AUPRC registered on CrossValidationReport")
