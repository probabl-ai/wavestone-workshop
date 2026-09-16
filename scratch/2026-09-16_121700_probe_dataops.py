import inspect

import pathlib

import pydoc

import skrub

D = pathlib.Path("scratch/api/skrub/0.10.1")
D.mkdir(parents=True, exist_ok=True)

node = skrub.var("x")

targets = [
    ("skrub", "var", skrub.var),
    ("skrub.var().skb", "mark_as_X", node.skb.mark_as_X),
    ("skrub.var().skb", "mark_as_y", node.skb.mark_as_y),
    ("skrub.var().skb", "apply_func", node.skb.apply_func),
    ("skrub.var().skb", "make_learner", node.skb.make_learner),
]

sections = [
    "# data_ops_core",
    "",
    "Source: inspect: skrub DataOps core @ 0.10.1",
    "Probed: 2026-09-16",
    "",
]
for owner, name, obj in targets:
    qual = f"{owner}.{name}"
    try:
        sig = inspect.signature(obj)
        sections += [f"## {qual}", "", "## Signature", "", f"```python\n{qual}{sig}\n```", ""]
    except (TypeError, ValueError):
        sections += [f"## {qual}", "", "## Signature", "", "n/a", ""]
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    sections += [f"## help() — {qual}", "", "```", doc, "```", ""]

(D / "data_ops_core.md").write_text("\n".join(sections))
print("written", D / "data_ops_core.md")
