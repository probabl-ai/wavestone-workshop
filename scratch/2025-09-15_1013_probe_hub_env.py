"""Diagnose hub auth env: report presence + shape of the env vars, never values."""

import os

for name in ["SKORE_HUB_URI", "SKORE_HUB_API_KEY"]:
    val = os.environ.get(name)
    if val is None:
        print(name, "= <unset>")
    else:
        print(name, f"= <set, len={len(val)}, starts={'https://' + val[len('https://'):][:0] if False else val[:8]}>")
