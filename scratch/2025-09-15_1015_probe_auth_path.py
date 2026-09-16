"""Inspect skore hub Project auth path: where does 'not logged in' come from?"""

import inspect
import os

import skore

os.environ.setdefault("SKORE_HUB_URI", "https://saint-gobain.api.skore.probabl.ai")

src_mod = inspect.getsourcefile(skore.Project)
print("module:", src_mod)

# Find the raise site
import subprocess

out = subprocess.run(
    ["grep", "-rn", "not logged in", os.path.dirname(src_mod)],
    capture_output=True, text=True,
)
print(out.stdout)
