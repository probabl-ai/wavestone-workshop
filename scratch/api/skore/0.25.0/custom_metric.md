# custom_metric

Source: inspect: EstimatorReport.metrics.add @ 0.25.0
Probed: 2026-09-16

## Signature

```python
metrics.add(self, metric: 'MetricLike', *, name: 'str | None' = None, verbose_name: 'str | None' = None, greater_is_better: 'bool' = True, position: "Literal['first', 'last']" = 'first', **kwargs: 'Any') -> 'None'
```

## help()

```
Python Library Documentation: function add in module skore._sklearn._estimator.metrics_accessor

add(self, metric: 'MetricLike', *, name: 'str | None' = None, verbose_name: 'str | None' = None, greater_is_better: 'bool' = True, position: "Literal['first', 'last']" = 'first', **kwargs: 'Any') -> 'None'
    Add a custom metric to :meth:`summarize`.

    Parameters
    ----------
    metric : str, sklearn scorer, or callable
        The metric to add.

        - If a string, it will be run through :func:`sklearn.metrics.get_scorer`.
          Metrics that require a ``neg_`` prefix (e.g. ``"neg_mean_squared_error"``)
          may also be passed without it (e.g. ``"mean_squared_error"``); the alias
          is resolved automatically.
        - If a callable, it must have the signature
          ``(estimator, X, y_true, **kw) -> float``. It may also return a ``dict``
          mapping class labels to floats (e.g. ``{0: 0.9, 1: 0.85}``), in which case
          :meth:`summarize` will show one row per class label under the metric name.
          If your metric has the form ``(y_true, y_pred, **kw) -> float``, see
          :func:`sklearn.metrics.make_scorer` to convert it to a scorer.

    name : str or None, default=None
        Custom name for the metric. If ``None``, the name is inferred
        from the metric (e.g. the function's ``__name__``).

    verbose_name : str or None, default=None
        Custom verbose name for the metric which will be used for display
        purposes. If ``None``, the verbose name is inferred from the metric
        name.

    greater_is_better : bool, default=True
        Whether higher values are better (only for callables).

    position : {"first", "last"}, default="first"
        Where to place the metric in default :meth:`summarize` ordering.
        ``"first"`` inserts at the front; repeated ``"first"`` adds stack
        newest-first. ``"last"`` appends at the end.

    **kwargs : Any
        Default keyword arguments passed to the score function at call
        time. Only used when *metric* is a plain callable.

    Examples
    --------
    >>> from sklearn.datasets import load_breast_cancer
    >>> from sklearn.linear_model import LogisticRegression
    >>> from sklearn.metrics import make_scorer, mean_absolute_error
    >>> from skore import evaluate
    >>> X, y = load_breast_cancer(return_X_y=True)
    >>> classifier = LogisticRegression(max_iter=10_000)
    >>> report = evaluate(classifier, X, y, pos_label=1)
    >>> report.metrics.add(
    ...     make_scorer(mean_absolute_error, response_method="predict")
    ... )
    >>> report.metrics.summarize(metric="mean_absolute_error").frame(
    ...     verbose_name=True, flat_index=False
    ... )
    Metric
    Mean Absolute Error    0.05...
    Name: LogisticRegression, dtype: float64
    >>> report.metrics.mean_absolute_error()
    0.05...

```
