"""Shape 1 probe: skore Project (init/put/summarize/get) -> cache file."""

import inspect
import os

import pydoc
import skore

OUT = os.path.join(os.path.dirname(__file__), "api", "skore", "0.25.0", "project_put.md")


def card(title, obj):
    try:
        sig = f"```\n{inspect.signature(obj)}\n```"
    except (TypeError, ValueError):
        sig = "(no signature)"
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    return f"## {title}\n\n### Signature\n{sig}\n\n### help()\n```\n{doc}\n```\n"


sections = [
    card("Project", skore.Project),
    card("Project.put", skore.Project.put),
    card("Project.summarize", skore.Project.summarize),
    card("Project.get", skore.Project.get),
]

with open(OUT, "w") as f:
    f.write("# skore Project: init, put, summarize, get\n\n")
    f.write("Source: inspect: skore @ 0.25.0\n")
    f.write("Probed: 2025-09-15\n\n")
    f.write("\n".join(sections))

print("wrote", OUT)
