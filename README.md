# Wavestone Workshop

Credit-card fraud detection with [skore](https://skore.probabl.ai). Participants iterate on models with the skore agent, then compare reports on the Hub.

## Setup

### 1. Clone the project repository

```bash
git clone https://github.com/probabl-ai/wavestone-workshop.git ./wavestone-workshop/
cd wavestone-workshop
```

### 2. Add the data file

If `data/creditcard.csv` (or `creditcard.csv` at the project root) is already present, skip this step.

Otherwise download the [Kaggle credit card fraud dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data) (`creditcard.csv`) and place it in `data/` (or at the project root).

### 3. Claim your skore.probabl.ai account

Make sure you received an email invitation to join the **workshop-wavestone** workspace on skore.probabl.ai. Follow the account creation steps. You will then be able to access [https://saint-gobain.skore.probabl.ai/workshop-wavestone](https://saint-gobain.skore.probabl.ai/workshop-wavestone).

### 4. Launch the skore agent

Install the `skore-cli` package and start the agent with `uv`. For this workshop, use the OpenCode harness:

```bash
uvx --from skore-cli skore agent --harness opencode --hub-url https://saint-gobain.api.skore.probabl.ai
```

When prompted, select the **workshop-wavestone** workspace. Other assistants (Claude Code, Pi, Copilot, Codex) are available if you omit `--harness opencode` and pick one interactively.

## Iterate, then validate

Once the setup is done, start prompting the agent. It will guide you through each step: feature engineering, model choice, cross-validation, evaluation, and each subsequent iteration.

- **Hub mode:** When the agent asks whether you prefer working locally or synchronizing with the hub, select **hub**.
- **Metric:** The ranking metric is **AUPRC** (area under the precision-recall curve). Instruct the agent to **create a custom AUPRC metric** and use it for all evaluation and comparison. Accuracy is not a valid ranking metric here — the target class is rare (~0.173% fraud).

## Browse the reports

Head to [https://saint-gobain.skore.probabl.ai/workshop-wavestone](https://saint-gobain.skore.probabl.ai/workshop-wavestone) to browse your model reports and those of other participants. A live leaderboard will be displayed in the room, updated each time a participant pushes a model to the hub.
