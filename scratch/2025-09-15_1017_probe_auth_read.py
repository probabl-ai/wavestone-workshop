"""Read the apikey auth module + the raise site context."""

import subprocess

base = "/Users/emmatysinger/Develop/workshop/wavestone-workshop/.venv/lib/python3.12/site-packages/skore/_plugins/hub"

print(subprocess.run(["cat", f"{base}/authentication/apikey.py"], capture_output=True, text=True).stdout)
print("---- raise site ----")
print(subprocess.run(["sed", "-n", "215,245p", f"{base}/client/client.py"], capture_output=True, text=True).stdout)
