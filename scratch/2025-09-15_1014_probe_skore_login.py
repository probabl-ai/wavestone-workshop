"""Shape 1 probe: skore.login -> cache file."""

import inspect
import os

import pydoc
import skore

OUT = os.path.join(os.path.dirname(__file__), "api", "skore", "0.25.0", "login.md")


def card(title, obj):
    try:
        sig = f"```\n{inspect.signature(obj)}\n```"
    except (TypeError, ValueError):
        sig = "(no signature)"
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    return f"## {title}\n\n### Signature\n{sig}\n\n### help()\n```\n{doc}\n```\n"


with open(OUT, "w") as f:
    f.write("# skore.login\n\n")
    f.write("Source: inspect: skore @ 0.25.0\n")
    f.write("Probed: 2025-09-15\n\n")
    f.write(card("skore.login", skore.login))

print("wrote", OUT)
