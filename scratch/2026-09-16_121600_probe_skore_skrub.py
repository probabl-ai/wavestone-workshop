import inspect

import pathlib

import pydoc

import skore

import skrub

D = pathlib.Path("scratch/api")
(D / "skore/0.25.0").mkdir(parents=True, exist_ok=True)
(D / "skrub/0.10.1").mkdir(parents=True, exist_ok=True)

for path, qual, obj in [
    (D / "skore/0.25.0/evaluate.md", "skore.evaluate", skore.evaluate),
    (D / "skrub/0.10.1/tabular_pipeline.md", "skrub.tabular_pipeline", skrub.tabular_pipeline),
]:
    sig = inspect.signature(obj)
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    path.write_text(
        f"# {qual.split('.')[-1]}\n\n"
        f"Source: inspect: {qual} @ {skore.__version__ if 'skore' in qual else skrub.__version__}\n"
        f"Probed: 2026-09-16\n\n"
        f"## Signature\n\n```python\n{qual}{sig}\n```\n\n"
        f"## help()\n\n```\n{doc}\n```\n"
    )
    print("written", path)
