"""Inspect the gitignored .skore config: list keys only, never print values."""

import json
from pathlib import Path

cfg = json.loads(Path(".skore").read_text())
print("keys:", sorted(cfg.keys()))
for k in cfg:
    if "key" not in k.lower():
        print(f"{k} = {cfg[k]!r}")
    else:
        print(f"{k} = <redacted, len={len(str(cfg[k]))}>")
