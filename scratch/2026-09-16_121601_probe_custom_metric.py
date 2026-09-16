import pathlib

import pydoc

import skore

D = pathlib.Path("scratch/api/skore/0.25.0")
D.mkdir(parents=True, exist_ok=True)

import skore._sklearn._estimator as _est

print("skore module surface for metrics:")
print([n for n in dir(skore) if "metric" in n.lower()])

from skore import CrossValidationReport

print("\nCrossValidationReport.metrics surface:")
print([n for n in dir(CrossValidationReport.metrics) if not n.startswith("_")])

from skore import EstimatorReport

print("\nEstimatorReport.metrics surface:")
print([n for n in dir(EstimatorReport.metrics) if not n.startswith("_")])

for qual, obj in [
    ("skore.metrics.add_custom_metric", getattr(skore.metrics, "add_custom_metric", None)),
]:
    if obj is None:
        print("\nno add_custom_metric on skore.metrics")
        continue
    doc = pydoc.render_doc(obj, renderer=pydoc.plaintext)
    (D / "custom_metric.md").write_text(
        f"# custom_metric\n\nSource: inspect: {qual} @ {skore.__version__}\nProbed: 2026-09-16\n\n## help()\n\n```\n{doc}\n```\n"
    )
    print("\nwritten", D / "custom_metric.md")
