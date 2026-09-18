# Wavestone Workshop

Credit-card fraud detection with [skore](https://skore.probabl.ai). Participants iterate on models with the skore agent, then compare reports on the Hub.

## Setup

### 1. Clone the project repository

```bash
git clone https://github.com/probabl-ai/wavestone-workshop.git
cd wavestone-workshop
```

### 2. Add the data file

If `data/creditcard.csv` is already present, skip this step.

**macOS / Linux**

```bash
./download-data
```

If `./download-data` prints `Permission denied`, run `chmod +x download-data` and retry.

**Windows (PowerShell)**

```powershell
.\download-data.ps1
```

### 3. Claim your skore.probabl.ai account

Make sure you received an email invitation to join the **workshop-wavestone** workspace on skore.probabl.ai. Follow the account creation steps. You will then be able to access [https://workshop.probabl.ai/workshop-wavestone](https://workshop.probabl.ai/workshop-wavestone).

### 4. Launch the skore agent

Install `[skore-cli](https://pypi.org/project/skore-cli/)` so the `skore` command is on your `PATH`:

```bash
pip install skore-cli
```

This workshop uses **GitHub Copilot** — CLI, desktop app, or VS Code.

**macOS / Linux**

```bash
./skore-copilot cli        # Copilot CLI
./skore-copilot desktop    # GitHub Copilot desktop app — follow the printed steps
./skore-copilot vscode     # VS Code + Copilot
```

If `./skore-copilot` prints `Permission denied`, run `chmod +x skore-copilot` and retry.

**Windows (PowerShell)**

```powershell
.\skore-copilot.ps1 cli
.\skore-copilot.ps1 desktop
.\skore-copilot.ps1 vscode
```

When prompted, select the **workshop-wavestone** workspace.

## Look at the Hub while you wait

You do not need a finished model first. As soon as your account is ready, open the [workshop-wavestone workspace](https://workshop.probabl.ai/workshop-wavestone).

While the agent is running EDA or a first baseline, browse the **pre-pushed experiments** so you can see what a Hub report looks like:

- `[wavestone-cv](https://workshop.probabl.ai/workshop-wavestone)` — cross-validation reports
- `[wavestone-leaderboard](https://workshop.probabl.ai/workshop-wavestone)` — fitted estimators scored on the held-out test set

![Skore Hub project: a table of reports you can open and compare](docs/images/hub-reports.png)

Those two projects are the destination for your own pushes later. Do not mix them: no CV reports on `wavestone-leaderboard`, no fitted/test reports on `wavestone-cv`.

A live leaderboard will also be displayed in the room, updated each time a participant pushes a model.

## Steer the agent from `journal/JOURNAL.md`

After the first agent turn, a `journal/` directory appears. **Open** `journal/JOURNAL.md` **and keep it open.** This is the index the agent writes as it works: current status, EDA summary, experiment history, and the backlog of next ideas.

![Example journal/JOURNAL.md with status, EDA, history, and a backlog](docs/images/journal.png)

Read it, then tell the agent what to do next — for example “run B2” or “keep the current splitter”. If you never open this file, you are not piloting the agent.

## Iterate, then validate

Once the setup is done, start prompting the agent. It will guide you through each step: feature engineering, model choice, cross-validation, evaluation, and each subsequent iteration.

- **Metric:** The ranking metric is **AUPRC** (area under the precision-recall curve). Instruct the agent to **create a custom AUPRC metric** and use it for all evaluation and comparison. Accuracy is not a valid ranking metric here — the target class is rare (~0.173% fraud).

