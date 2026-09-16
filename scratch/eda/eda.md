# Cells: `data/eda.py`

## Cell 0: `# %% [markdown]`

# EDA: Kaggle credit-card fraud dataset
#
Exploratory data analysis of `creditcard.csv` (284,807 × 31, target `Class`),
run before designing a model.
#
- **Raw data** is read-only — point `RAW` at it below (it may live in
  `data/`, another folder, or an absolute path). This file never
  cleans or modifies the raw data.
- **Outputs** go under `EDA_DIR` (`<project>/data/`): an
  `eda_creditcard.html` report per table, summarized in `eda.md`.

## Cell 1: `# %%`

```python
import json

import pandas as pd
import skrub

from fraud_detection import PROJECT_ROOT

# EDA outputs always land here (created if missing); the raw data may
# live elsewhere.
EDA_DIR = PROJECT_ROOT / "data"
EDA_DIR.mkdir(parents=True, exist_ok=True)
```

## Cell 2: `# %% [markdown]`

## Load the raw data
#
Load the raw table(s) into `RAW`. With several tables, load each into
its own variable and repeat the overview cell per table.

## Cell 3: `# %%`

```python
RAW = pd.read_csv(PROJECT_ROOT / "data" / "creditcard.csv")
RAW.shape
```

**stdout:**
```
Out[0]: (284807, 31)
```

## Cell 4: `# %% [markdown]`

## Table overview
#
Per-table report (column types, distributions, associations) saved to
`data/eda_creditcard.html`, plus a compact per-column summary: dtype,
fraction missing, and number of unique values.

## Cell 5: `# %%`

```python
report = skrub.TableReport(RAW, title="creditcard", verbose=0)
report.write_html(EDA_DIR / "eda_creditcard.html")

summary = json.loads(report.json())
n_rows = summary.get("n_rows")
overview = [
    {
        "column": col.get("name"),
        "dtype": col.get("dtype"),
        "null_pct": col.get("null_proportion"),
        "n_unique": col.get("nunique"),
    }
    for col in summary.get("columns", [])
]
{"n_rows": n_rows, "n_columns": len(overview), "columns": overview}
```

**stdout:**
```
Out[0]: 
{'n_rows': 284807,
 'n_columns': 31,
 'columns': [{'column': 'Time',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V1', 'dtype': 'Float64DType', 'null_pct': 0.0, 'n_unique': None},
  {'column': 'V2', 'dtype': 'Float64DType', 'null_pct': 0.0, 'n_unique': None},
  {'column': 'V3', 'dtype': 'Float64DType', 'null_pct': 0.0, 'n_unique': None},
  {'column': 'V4', 'dtype': 'Float64DType', 'null_pct': 0.0, 'n_unique': None},
  {'column': 'V5', 'dtype': 'Float64DType', 'null_pct': 0.0, 'n_unique': None},
  {'column': 'V6', 'dtype': 'Float64DType', 'null_pct': 0.0, 'n_unique': None},
  {'column': 'V7', 'dtype': 'Float64DType', 'null_pct': 0.0, 'n_unique': None},
  {'column': 'V8', 'dtype': 'Float64DType', 'null_pct': 0.0, 'n_unique': None},
  {'column': 'V9', 'dtype': 'Float64DType', 'null_pct': 0.0, 'n_unique': None},
  {'column': 'V10',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V11',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V12',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V13',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V14',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V15',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V16',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V17',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V18',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V19',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V20',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V21',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V22',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V23',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V24',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V25',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V26',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V27',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'V28',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'Amount',
   'dtype': 'Float64DType',
   'null_pct': 0.0,
   'n_unique': None},
  {'column': 'Class',
   'dtype': 'Int64DType',
   'null_pct': 0.0,
   'n_unique': None}]}
```

## Cell 6: `# %% [markdown]`

## Target
#
The target's distribution — class balance for classification, or
spread / skew for regression. This shapes the metric and whether
cross-validation should stratify.

## Cell 7: `# %%`

```python
TARGET = "Class"
next((col for col in summary.get("columns", []) if col.get("name") == TARGET), None)
```

**stdout:**
```
Out[0]: 
{'position': 30,
 'idx': 30,
 'name': 'Class',
 'dtype': 'Int64DType',
 'value_is_constant': False,
 'is_ordered': False,
 'null_count': 0,
 'null_proportion': 0.0,
 'nulls_level': 'ok',
 'n_unique': 2,
 'unique_proportion': 7.0222993114635526e-06,
 'is_high_cardinality': False,
 'is_duration': False,
 'duration_unit': None,
 'standard_deviation': 0.04152718963546506,
 'mean': 0.001727485630620034,
 'inter_quartile_range': 0,
 'quantiles': {'0.0': 0, '0.25': 0, '0.5': 0, '0.75': 0, '1.0': 1},
 'histogram_data': {'n_low_outliers': 0,
  'n_high_outliers': 0,
  'bin_counts': [284315, 0, 0, 0, 0, 0, 0, 0, 0, 492],
  'bin_edges': [0.0,
   0.1,
   0.2,
   0.30000000000000004,
   0.4,
   0.5,
   0.6000000000000001,
   0.7000000000000001,
   0.8,
   0.9,
   1.0]},
 'plot_names': []}
```

## Cell 8: `# %% [markdown]`

## Structure signals
#
Datetime columns (which point to time-based validation) and
high-cardinality id / group-like columns (which point to grouped
validation, to avoid leaking an entity across folds).

## Cell 9: `# %%`

```python
datetime_cols = [
    col.get("name")
    for col in summary.get("columns", [])
    if "date" in str(col.get("dtype", "")).lower()
]
unique_ratio = sorted(
    (
        {
            "column": col.get("name"),
            "unique_ratio": (col.get("nunique") or 0) / n_rows if n_rows else None,
        }
        for col in summary.get("columns", [])
    ),
    key=lambda r: (r["unique_ratio"] is not None, r["unique_ratio"]),
    reverse=True,
)
{"datetime_cols": datetime_cols, "top_unique_ratio": unique_ratio[:10]}
```

**stdout:**
```
Out[0]: 
{'datetime_cols': [],
 'top_unique_ratio': [{'column': 'Time', 'unique_ratio': 0.0},
  {'column': 'V1', 'unique_ratio': 0.0},
  {'column': 'V2', 'unique_ratio': 0.0},
  {'column': 'V3', 'unique_ratio': 0.0},
  {'column': 'V4', 'unique_ratio': 0.0},
  {'column': 'V5', 'unique_ratio': 0.0},
  {'column': 'V6', 'unique_ratio': 0.0},
  {'column': 'V7', 'unique_ratio': 0.0},
  {'column': 'V8', 'unique_ratio': 0.0},
  {'column': 'V9', 'unique_ratio': 0.0}]}
```

## Cell 10: `# %% [markdown]`

## Associations
#
Strongest pairwise column associations. Strong feature↔target links
are candidate predictors; an implausibly perfect one is a possible
leakage flag to call out explicitly.

## Cell 11: `# %%`

```python
skrub.column_associations(RAW).head(20)
```

**stdout:**
```
Out[0]: 
   left_column_name  left_column_idx right_column_name  right_column_idx  \
0               V17               17             Class                30   
1                V5                5                V6                 6   
2               V20               20            Amount                29   
3               V14               14             Class                30   
4               V12               12             Class                30   
5                V6                6                V7                 7   
6                V5                5                V7                 7   
7                V8                8               V21                21   
8               V10               10             Class                30   
9               V11               11             Class                30   
10               V9                9               V10                10   
11              V16               16             Class                30   
12               V7                7            Amount                29   
13               V6                6            Amount                29   
14              V21               21               V22                22   
15               V3                3                V7                 7   
16               V7                7               V16                16   
17              V17               17               V18                18   
18               V3                3                V5                 5   
19               V5                5            Amount                29   

    cramer_v  pearson_corr  
0   0.710961 -3.264811e-01  
1   0.699568  2.208263e-16  
2   0.696627  3.394034e-01  
3   0.653194 -3.025437e-01  
4   0.648032 -2.605929e-01  
5   0.640117  1.213776e-16  
6   0.613892  2.691713e-16  
7   0.612967  3.830431e-16  
8   0.592418 -2.168829e-01  
9   0.575989  1.548756e-01  
10  0.573813 -4.638448e-16  
11  0.565133 -1.965389e-01  
12  0.542843  3.973113e-01  
13  0.534608  2.159812e-01  
14  0.532483  3.666786e-15  
15  0.532455  5.239200e-16  
16  0.518711  4.920492e-17  
17  0.514261 -4.899669e-15  
18  0.513743 -5.483554e-17  
19  0.508478 -3.863563e-01  
```

## Cell 12: `# %% [markdown]`

## Summary
#
The findings and their modelling implications are written up in
`data/eda.md`.
