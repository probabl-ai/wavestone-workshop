"""Trace how client.py resolves `credentials`."""

import subprocess

base = "/Users/emmatysinger/Develop/workshop/wavestone-workshop/.venv/lib/python3.12/site-packages/skore/_plugins/hub"
out = subprocess.run(["grep", "-rn", "APIKey\\|credentials", f"{base}/client/client.py"], capture_output=True, text=True)
print(out.stdout)
