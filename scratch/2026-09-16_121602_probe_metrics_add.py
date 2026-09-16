import inspect

import pathlib

import pydoc

from skore import EstimatorReport

D = pathlib.Path("scratch/api/skore/0.25.0")
D.mkdir(parents=True, exist_ok=True)

obj = EstimatorReport.metrics.add
sig = inspect.signature(obj)
doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
(D / "custom_metric.md").write_text(
    f"# custom_metric\n\nSource: inspect: EstimatorReport.metrics.add @ {__import__('skore').__version__}\n"
    f"Probed: 2026-09-16\n\n"
    f"## Signature\n\n```python\nmetrics.add{sig}\n```\n\n"
    f"## help()\n\n```\n{doc}\n```\n"
)
print("written", D / "custom_metric.md")
