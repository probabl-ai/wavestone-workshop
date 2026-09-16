"""Shape 1 probe: skore.evaluate defaults (metrics / report type)."""
import inspect

import pydoc
import skore

OUT = "scratch/api/skore/0.25.0/evaluate.md"
doc = pydoc.render_doc(skore.evaluate, renderer=pydoc.plaintext)
with open(OUT, "w") as f:
    f.write(
        f"# skore.evaluate\n\nSource: inspect: skore.evaluate @ {skore.__version__}\n\n"
        f"## Signature\n```\n{inspect.signature(skore.evaluate)}\n```\n\n## help()\n```\n{doc[:6000]}\n```\n"
    )
print("wrote", OUT)
print(inspect.signature(skore.evaluate))
