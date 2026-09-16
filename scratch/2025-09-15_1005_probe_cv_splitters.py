"""Shape 1 probe: sklearn CV splitters relevant to the baseline (KFold, TimeSeriesSplit)."""

import inspect
import os

import pydoc
from sklearn.model_selection import KFold, TimeSeriesSplit

OUT = os.path.join(os.path.dirname(__file__), "api", "sklearn", "1.9.1", "cv_splitters.md")


def card(title, obj):
    try:
        sig = f"```\n{inspect.signature(obj)}\n```"
    except (TypeError, ValueError):
        sig = "(no signature)"
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    return f"## {title}\n\n### Signature\n{sig}\n\n### help()\n```\n{doc}\n```\n"


sections = [card("KFold", KFold), card("TimeSeriesSplit", TimeSeriesSplit)]

with open(OUT, "w") as f:
    f.write("# CV splitters (KFold, TimeSeriesSplit)\n\n")
    f.write("Source: inspect: sklearn @ 1.9.1\n")
    f.write("Probed: 2025-09-15\n\n")
    f.write("\n".join(sections))

print("wrote", OUT)
