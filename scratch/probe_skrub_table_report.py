"""Shape 1 probe: skrub TableReport + column_associations signatures."""
import inspect

import pydoc
import skrub

TOPICS = [
    "skrub.TableReport",
    "skrub.TableReport.write_html",
    "skrub.TableReport.json",
    "skrub.column_associations",
]

OUT = "scratch/api/skrub/0.10.1/table_report.md"
sections = []
for dotted in TOPICS:
    obj = skrub
    for part in dotted.split(".")[1:]:
        obj = getattr(obj, part)
    sig = ""
    try:
        sig = str(inspect.signature(obj))
    except (TypeError, ValueError):
        sig = "<no signature>"
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    sections.append(
        f"# {dotted}\n\nSource: inspect: {dotted} @ skrub {skrub.__version__}\n\n"
        f"## Signature\n```\n{sig}\n```\n\n## help()\n```\n{doc[:4000]}\n```\n"
    )

with open(OUT, "w") as f:
    f.write("\n".join(sections))
print("wrote", OUT)
print("sig TableReport:", inspect.signature(skrub.TableReport))
print("sig write_html:", inspect.signature(skrub.TableReport.write_html))
print("sig json:", inspect.signature(skrub.TableReport.json))
print("sig column_associations:", inspect.signature(skrub.column_associations))
