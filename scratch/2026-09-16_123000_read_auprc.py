import json
import os
from pathlib import Path

import skore

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / ".skore").open() as f:
    cfg = json.load(f)
os.environ.setdefault("SKORE_HUB_URI", cfg["hub_url"])
os.environ.setdefault("SKORE_HUB_API_KEY", cfg["api_key"])

from skore import login

login(mode="hub")

cv_project = skore.Project(name="wavestone-cv", mode="hub", workspace="workshop-wavestone")
lb_project = skore.Project(
    name="wavestone-leaderboard", mode="hub", workspace="workshop-wavestone"
)

for proj, key in [(cv_project, "01_baseline"), (lb_project, "01_baseline_fitted")]:
    frame = proj.summarize().frame()
    urns = sorted(
        (i[1] for i in frame.index if str(i[1]).startswith("skore:report:")),
        key=lambda u: int(str(u).rsplit(":", 1)[1]),
    )
    urn = urns[-1]
    report = proj.get(urn)
    print(f"== {key} ({urn}) ==")
    print(report.metrics.summarize(metric="auprc").frame())
    print()
