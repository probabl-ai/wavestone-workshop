"""Shape 1 probe: skrub DataOps core symbols -> cache data_ops_core.md."""
import inspect
import os

import pydoc
import skrub

OUT = os.path.join(os.path.dirname(__file__), "api", "skrub", "0.10.1", "data_ops_core.md")


def card(title, obj):
    try:
        sig = f"```\n{inspect.signature(obj)}\n```"
    except (TypeError, ValueError):
        sig = "(no signature)"
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    return f"## {title}\n\n### Signature\n{sig}\n\n### help()\n```\n{doc}\n```\n"


sections = [card("skrub.var", skrub.var)]
# Methods on the DataOps .skb namespace: introspect a live DataOp
op = skrub.var("x", value=None)
for name in ["apply", "apply_func", "mark_as_X", "mark_as_y", "make_learner"]:
    sections.append(card(f"DataOp.skb.{name}", getattr(op.skb, name)))

with open(OUT, "w") as f:
    f.write("# skrub DataOps core (var, apply, apply_func, mark_as_X/y, make_learner)\n\n")
    f.write("Source: inspect: skrub @ 0.10.1\n")
    f.write("Probed: 2025-09-15\n\n")
    f.write("\n".join(sections))

print("wrote", OUT)
