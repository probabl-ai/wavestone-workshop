"""Find the auth raise site under site-packages/skore."""

import os
import subprocess

site = os.path.dirname(__import__("skore")._project.project.__file__)
root = os.path.dirname(site)
out = subprocess.run(["grep", "-rn", "not logged in", root], capture_output=True, text=True)
print(out.stdout or out.stderr)
out2 = subprocess.run(["grep", "-rn", "SKORE_HUB_API_KEY", root], capture_output=True, text=True)
print(out2.stdout)
