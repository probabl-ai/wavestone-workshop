"""Read login.credentials resolution."""

import subprocess

base = "/Users/emmatysinger/Develop/workshop/wavestone-workshop/.venv/lib/python3.12/site-packages/skore/_plugins/hub/authentication"
print(subprocess.run(["cat", f"{base}/login.py"], capture_output=True, text=True).stdout)
