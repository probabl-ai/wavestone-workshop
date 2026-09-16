"""Shape 1 probe: metrics.add / metrics.get / metrics.remove -> cache file."""

import inspect
import os

import pydoc
import skore
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from skore import EstimatorReport

X, y = make_classification(n_samples=200, random_state=0)
rep = EstimatorReport(LogisticRegression(), X_train=X, y_train=y, X_test=X, y_test=y)

OUT = os.path.join(os.path.dirname(__file__), "api", "skore", "0.25.0", "metrics_add.md")


def card(title, obj):
    try:
        sig = f"```\n{inspect.signature(obj)}\n```"
    except (TypeError, ValueError):
        sig = "(no signature)"
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    return f"## {title}\n\n### Signature\n{sig}\n\n### help()\n```\n{doc}\n```\n"


sections = [card("metrics.add", rep.metrics.add), card("metrics.get", rep.metrics.get)]

with open(OUT, "w") as f:
    f.write("# skore metrics.add / metrics.get (custom metric plumbing)\n\n")
    f.write("Source: inspect: skore @ 0.25.0 (live EstimatorReport)\n")
    f.write("Probed: 2025-09-15\n\n")
    f.write("\n".join(sections))

print("wrote", OUT)
