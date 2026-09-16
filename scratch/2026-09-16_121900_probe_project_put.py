import inspect

import pathlib

import pydoc

import skore

D = pathlib.Path("scratch/api/skore/0.25.0")
D.mkdir(parents=True, exist_ok=True)

obj = skore.Project.put
sig = inspect.signature(obj)
doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
(D / "project_put.md").write_text(
    f"# project_put\n\nSource: inspect: skore.Project.put @ {skore.__version__}\n"
    f"Probed: 2026-09-16\n\n"
    f"## Signature\n\n```python\nProject.put{sig}\n```\n\n"
    f"## help()\n\n```\n{doc}\n```\n"
)
print("written")
