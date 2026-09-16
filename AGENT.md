# Agent brief — Wavestone workshop

Credit-card fraud detection on the Kaggle [mlg-ulb/creditcardfraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data) dataset.

## Task

Binary classification: predict `Class` (0 = legitimate, 1 = fraud). Goal is a strong, comparable baseline then iterative improvements.

Create a **custom AUPRC** metric (area under the precision-recall curve) and use it as the primary metric for cross-validation, held-out evaluation, and Hub reports. Do not rank models on accuracy (target is ~0.173% positive).

## Data

- Raw CSV: `data/creditcard.csv` (284,807 × 31)
- Features: `Time`, `V1`–`V28` (PCA), `Amount`; target: `Class`

## Skore Hub pushes

Hub workspace: **workshop-wavestone** ([hub](https://saint-gobain.skore.probabl.ai/workshop-wavestone)).

- Cross-validation report → project `wavestone-cv`
- Fitted estimator / full train + held-out test → project `wavestone-leaderboard`
- Never mix them: no CV reports on `wavestone-leaderboard`, no fitted/test reports on `wavestone-cv`.
