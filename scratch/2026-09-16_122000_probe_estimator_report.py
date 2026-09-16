import inspect

import pathlib

import pydoc

import skore

D = pathlib.Path("scratch/api/skore/0.25.0")
D.mkdir(parents=True, exist_ok=True)

obj = skore.EstimatorReport.__init__
sig = inspect.signature(obj)
doc = pydoc.render_doc(skore.EstimatorReport, renderer=pydoc.plaintext)
(D / "estimator_report.md").write_text(
    f"# estimator_report\n\nSource: inspect: skore.EstimatorReport @ {skore.__version__}\n"
    f"Probed: 2026-09-16\n\n"
    f"## Signature\n\n```python\nEstimatorReport.__init__{sig}\n```\n\n"
    f"## help()\n\n```\n{doc}\n```\n"
)
print("written")
