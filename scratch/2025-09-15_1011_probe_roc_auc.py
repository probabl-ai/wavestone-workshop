"""Shape 1 probe: sklearn.metrics.roc_auc_score -> cache file."""

import inspect
import os

import pydoc
from sklearn.metrics import roc_auc_score

OUT = os.path.join(os.path.dirname(__file__), "api", "sklearn", "1.9.1", "metrics_roc_auc.md")


def card(title, obj):
    try:
        sig = f"```\n{inspect.signature(obj)}\n```"
    except (TypeError, ValueError):
        sig = "(no signature)"
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    return f"## {title}\n\n### Signature\n{sig}\n\n### help()\n```\n{doc}\n```\n"


with open(OUT, "w") as f:
    f.write("# roc_auc_score\n\n")
    f.write("Source: inspect: sklearn @ 1.9.1\n")
    f.write("Probed: 2025-09-15\n\n")
    f.write(card("roc_auc_score", roc_auc_score))

print("wrote", OUT)
