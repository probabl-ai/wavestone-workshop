# Agent brief — Wavestone workshop

Credit-card fraud detection on the Kaggle [mlg-ulb/creditcardfraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data) dataset.

## Task

Binary classification: predict `Class` (0 = legitimate, 1 = fraud). Goal is a strong, comparable baseline then iterative improvements. Prefer **PR-AUC / ROC-AUC** over accuracy (target is ~0.173% positive).

## Data

- Raw CSV: `data/creditcard.csv` (284,807 × 31)
- Features: `Time`, `V1`–`V28` (PCA), `Amount`; target: `Class`

## Skore Hub pushes

Workspace: `wavestone-workshop`. Route reports by evaluation mode:

| Evaluation | Hub project |
|---|---|
| Cross-validation runs | `wavestone-cv` |
| Full train + evaluate on held-out test | `wavestone-leaderboard` |

When pushing an estimator or CV report, set the Hub project accordingly — do not send CV reports to the leaderboard or the final train/test run to `wavestone-cv`.
