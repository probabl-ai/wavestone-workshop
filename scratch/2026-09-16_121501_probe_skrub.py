import inspect

import pathlib

import pydoc

import skrub

OUT = pathlib.Path("scratch/api/skrub/0.10.1/table_report.md")
OUT.parent.mkdir(parents=True, exist_ok=True)

targets = [
    ("skrub", "TableReport"),
    ("skrub.TableReport", "write_html"),
    ("skrub.TableReport", "json"),
    ("skrub", "column_associations"),
]

sections = ["# table_report", "", "Source: inspect: skrub @ 0.10.1", "Probed: 2026-09-16", ""]
for owner, name in targets:
    obj = getattr(skrub, name) if "." not in owner else getattr(skrub, owner.split(".")[1]).__dict__.get(name)
    qual = f"{owner}.{name}"
    try:
        sig = inspect.signature(obj)
        sections += [f"## {qual}", "", "## Signature", "", f"```python\n{qual}{sig}\n```", ""]
    except (TypeError, ValueError):
        sections += [f"## {qual}", "", "## Signature", "", "n/a", ""]
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    sections += [f"## help() — {qual}", "", "```", doc, "```", ""]

with open(OUT, "w") as f:
    f.write("\n".join(sections))
print("written", OUT)
