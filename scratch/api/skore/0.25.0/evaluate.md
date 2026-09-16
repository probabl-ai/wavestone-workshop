# skore.evaluate

Source: inspect: skore.evaluate @ 0.25.0

## Signature
```
(estimator: 'EstimatorLike | list[EstimatorLike] | dict[str, EstimatorLike]', X: 'ArrayLike | None' = None, y: 'ArrayLike | None' = None, data: 'dict | None' = None, *, splitter: "float | int | Literal['prefit'] | SKLearnCrossValidator | Generator | _DefaultType" = <DEFAULT>, pos_label: 'int | float | bool | str | None' = None, n_jobs: 'int | None' = None) -> 'EstimatorReport | CrossValidationReport | ComparisonReport'
```

## help()
```
Python Library Documentation: function evaluate in module skore._sklearn.evaluate

evaluate(estimator: 'EstimatorLike | list[EstimatorLike] | dict[str, EstimatorLike]', X: 'ArrayLike | None' = None, y: 'ArrayLike | None' = None, data: 'dict | None' = None, *, splitter: "float | int | Literal['prefit'] | SKLearnCrossValidator | Generator | _DefaultType" = <DEFAULT>, pos_label: 'int | float | bool | str | None' = None, n_jobs: 'int | None' = None) -> 'EstimatorReport | CrossValidationReport | ComparisonReport'
    Evaluate one or more estimators on the given data.

    Passing several estimators provides a report to compare them, while the
    ``splitter`` parameter controls whether a train-test split or
    cross-validation is used.

    Parameters
    ----------
    estimator : estimator object, list of estimators, or dict of estimators
        The estimator to evaluate of several estimators to compare. An estimator can
        be one of the following:

        - a scikit-learn compatible estimator as a :class:`~sklearn.base.BaseEstimator`;
        - a skrub :class:`~skrub.DataOp` to preprocess the data;
        - a skrub :class:`~skrub.SkrubLearner` extracted from a :class:`~skrub.DataOp`
          by calling :meth:`~skrub.DataOp.skb.make_learner`.

    X : array-like or None
        Feature matrix shared by all estimators when comparing several models.
        When comparing prefit estimators and no test features are needed,
        pass ``X=None``. To compare estimators evaluated on different feature
        matrices, call :func:`~skore.evaluate` once per estimator, then
        :func:`~skore.compare`.

    y : array-like of shape (n_samples,), or None
        Target vector.

    data : dict or None
        When ``estimator`` is a skrub :class:`~skrub.SkrubLearner`, bindings for
        variables contained in the DataOp that was used to create this learner
        (e.g. ``{"X": X_df, "other_table": df, ...}``).

    splitter : float, int, "prefit", or cross-validation object, default=0.2
        Determines how the data is split. When omitted, a skrub learner whose
        DataOp was configured with an explicit cross-validation splitter via
        :meth:`~skrub.DataOp.skb.mark_as_X` uses that splitter (including
        ``split_kwargs`` such as ``groups``). Otherwise, the default is a
        single 80/20 train-test split:

        - ``float``: perform a single train-test split where the data is shuffled before
          splitting with a fixed seed (``random_state=0``) for reproducibility.
          Pass a :class:`~skore.TrainTestSplit` instance for more control over the
          splitting parameters.
        - ``"prefit"``: the estimator is assumed to be already fitted; ``X``
          and ``y`` are used as the test set.
        - ``int``: number of folds for cross-validation (passed to
          :class:`~skore.CrossValidationReport`).
        - cross-validation splitter (e.g. ``KFold``, ``StratifiedKFold``):
          passed directly to :class:`~skore.CrossValidationReport`.

    pos_label : int, float, bool or str, default=None
        The positive class label for binary classification metrics. Forwarded
        to the underlying report.

    n_jobs : int or None, default=None
        Number of jobs for parallel execution. Forwarded to
        :class:`~skore.CrossValidationReport` or
        :class:`~skore.ComparisonReport`.

    Returns
    -------
    report : :class:`~skore.EstimatorReport`, :class:`~skore.CrossValidationReport`             or :class:`~skore.ComparisonReport`
        The report corresponding to the evaluation strategy.

    See Also
    --------
    :func:`~skore.compare` :
        Compare already evaluated reports.
    :class:`~skore.EstimatorReport` :
        Report for a fitted estimator on a test set.
    :class:`~skore.CrossValidationReport` :
        Report for cross-validation of an estimator.
    :class:`~skore.ComparisonReport` :
        Report comparing several evaluated models.

    Examples
    --------
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.linear_model import LogisticRegression
    >>> from skore import evaluate
    >>> X, y = make_classification(random_state=42)

    Default 80/20 train-test split:

    >>> report = evaluate(LogisticRegression(), X, y)

    Cross-validation with 5 folds:

    >>> report = evaluate(LogisticRegression(), X, y, splitter=5)

    Evaluate a pre-fitted estimator:

    >>> from sklearn.model_selection import train_test_split
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    >>> fitted_model = LogisticRegression().fit(X_train, y_train)
    >>> report = evaluate(fitted_model, X_test, y_test, splitter="prefit")

    Compare several named estimators:

    >>> report = evaluate(
    ...     {"m1": LogisticRegression(), "m2": LogisticRegression(C=2.0)},
    ...     X,
    ...     y,
    ...     splitter=0.2,
    ... )
    >>> list(report.reports_)
    ['m1', 'm2']

```
