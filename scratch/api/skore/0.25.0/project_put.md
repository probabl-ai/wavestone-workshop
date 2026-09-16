# project_put

Source: inspect: skore.Project.put @ 0.25.0
Probed: 2026-09-16

## Signature

```python
Project.put(self, key: 'str', report: 'EstimatorReport | CrossValidationReport')
```

## help()

```
Python Library Documentation: function put in module skore._project.project

put(self, key: 'str', report: 'EstimatorReport | CrossValidationReport')
    Put a key-report pair to the project.

    If the key already exists, its last report is modified to point to this new
    report, while keeping track of the report history.

    Parameters
    ----------
    key : str
        The key to associate with ``report`` in the project.
        Name of the run for mode:mlflow
    report : EstimatorReport | CrossValidationReport
        The report to associate with ``key`` in the project.

    Returns
    -------
    None
        The report is persisted in the project backend.

    Examples
    --------
    >>> from sklearn.datasets import make_regression
    >>> from sklearn.linear_model import LinearRegression
    >>> from pathlib import Path
    >>> from tempfile import TemporaryDirectory
    >>> from skore import Project, evaluate
    >>> X, y = make_regression(random_state=42)
    >>> report = evaluate(LinearRegression(), X, y, splitter=0.2)
    >>> tmpdir = TemporaryDirectory()
    >>> project = Project(name="my-xp", mode="local", workspace=Path(tmpdir.name))
    >>> project.put("my-regression", report)
    >>> tmpdir.cleanup()

```
