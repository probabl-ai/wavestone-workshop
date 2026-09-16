import inspect

import pathlib

import pydoc

import sklearn
from sklearn.model_selection import KFold

D = pathlib.Path("scratch/api/sklearn")
(D / sklearn.__version__).mkdir(parents=True, exist_ok=True)

sig = inspect.signature(KFold)
doc = pydoc.render_doc(KFold, renderer=pydoc.plaintext)
(D / sklearn.__version__ / "cv_splitters.md").write_text(
    f"# cv_splitters\n\nSource: inspect: sklearn.model_selection.KFold @ {sklearn.__version__}\n"
    f"Probed: 2026-09-16\n\n"
    f"## Signature\n\n```python\nKFold{sig}\n```\n\n"
    f"## help()\n\n```\n{doc}\n```\n"
)
print("written", D / sklearn.__version__ / "cv_splitters.md")
