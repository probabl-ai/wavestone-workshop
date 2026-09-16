"""Shape 2 probe: metrics namespace surface on a fitted EstimatorReport."""

import inspect

import skore
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from skore import EstimatorReport

X, y = make_classification(n_samples=200, random_state=0)
rep = EstimatorReport(LogisticRegression(), X_train=X, y_train=y, X_test=X, y_test=y)
ns = rep.metrics
print("metrics attrs:", [n for n in dir(ns) if not n.startswith("_")])
for name in dir(ns):
    if "custom" in name.lower():
        print("SIG", name, inspect.signature(getattr(ns, name)))
        print(pydoc := __import__("pydoc").render_doc(getattr(ns, name), renderer=__import__("pydoc").plaintext)[:1500])
