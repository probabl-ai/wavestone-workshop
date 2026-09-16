# estimator_report

Source: inspect: skore.EstimatorReport @ 0.25.0
Probed: 2026-09-16

## Signature

```python
EstimatorReport.__init__(self, estimator: 'EstimatorLike', *, X_train: 'ArrayLike | None' = None, y_train: 'ArrayLike | None' = None, X_test: 'ArrayLike | None' = None, y_test: 'ArrayLike | None' = None, train_data: 'dict | None' = None, test_data: 'dict | None' = None, pos_label: 'PositiveLabel | None' = None) -> 'None'
```

## help()

```
Python Library Documentation: class EstimatorReport in module skore._sklearn._estimator.report

class EstimatorReport(skore._sklearn._base._BaseReport, skore._externals._pandas_accessors.DirNamesMixin)
 |  EstimatorReport(estimator: 'EstimatorLike', *, X_train: 'ArrayLike | None' = None, y_train: 'ArrayLike | None' = None, X_test: 'ArrayLike | None' = None, y_test: 'ArrayLike | None' = None, train_data: 'dict | None' = None, test_data: 'dict | None' = None, pos_label: 'PositiveLabel | None' = None) -> 'None'
 |
 |  Provide tools to validate and inspect a fitted estimator.
 |
 |  Refer to the :ref:`estimator_report` section of the user guide for more details.
 |
 |  Parameters
 |  ----------
 |  estimator : estimator object
 |      Estimator to make the report from. An estimator can be one of the following:
 |
 |      - a scikit-learn compatible estimator as a :class:`~sklearn.base.BaseEstimator`;
 |      - a skrub :class:`~skrub.DataOp` to preprocess the data;
 |      - a skrub :class:`~skrub.SkrubLearner` extracted from a :class:`~skrub.DataOp`
 |        by calling :meth:`~skrub.DataOp.skb.make_learner`.
 |
 |      If the estimator is not fitted, it is cloned and then fitted on the training
 |      data. If the estimator is already fitted, training data must not be provided.
 |
 |  X_train : {array-like, sparse matrix} of shape (n_samples, n_features) or             None
 |      Training data. Must not be provided when ``estimator`` is already fitted.
 |
 |  y_train : array-like of shape (n_samples,) or (n_samples, n_outputs) or None
 |      Training target. Must not be provided when ``estimator`` is already fitted.
 |
 |  X_test : {array-like, sparse matrix} of shape (n_samples, n_features) or None
 |      Testing data. It should have the same structure as the training data.
 |
 |  y_test : array-like of shape (n_samples,) or (n_samples, n_outputs) or None
 |      Testing target.
 |
 |  train_data : dict or None
 |      When ``estimator`` is a skrub :class:`~skrub.SkrubLearner`, bindings for
 |      variables contained in the DataOp that was used to create this learner
 |      (e.g. ``{"X": X_df, "other_table": df, ...}``). Must not be provided when
 |      ``estimator`` is already fitted.
 |
 |  test_data : dict or None
 |      When ``estimator`` is a skrub :class:`~skrub.SkrubLearner`, bindings for
 |      variables contained in the DataOp that was used to create this learner
 |      (e.g. ``{"X": X_df, "other_table": df, ...}``).
 |
 |  pos_label : int, float, bool or str, default=None
 |      For binary classification, the positive class to use for metrics and displays
 |      that need one. If `None`, skore does not infer a default positive class.
 |      Binary metrics and displays that support it will expose all classes instead.
 |      This parameter is rejected for non-binary tasks.
 |
 |  Attributes
 |  ----------
 |  estimator_ : estimator object
 |      The fitted estimator, exposed with the same interface as ``estimator``:
 |
 |      - if the input was a regular scikit-learn estimator, its ``predict`` method
 |        should be used with arrays as usual, e.g. ``Report.estimator_.predict(X)``;
 |      - if the input was a :class:`skrub.DataOp` or a :class:`skrub.SkrubLearner`,
 |        ``estimator_`` is a :class:`skrub.SkrubLearner` so its ``predict`` method
 |        should be used with an environment dict, e.g.
 |        ``Report.estimator_.predict({"a": ..., "b": ...})``.
 |
 |  estimator : estimator object
 |      The estimator that was given as input.
 |
 |  learner_ : skrub.SkrubLearner
 |      The fitted estimator wrapped in a :class:`skrub.SkrubLearner`. If the
 |      input was already a :class:`skrub.SkrubLearner`, it is used as-is without
 |      further wrapping.
 |
 |  estimator_name_ : str
 |      The name of the estimator.
 |
 |  ml_task : str
 |      The machine learning task inferred from the data and estimator.
 |
 |  metrics : MetricsAccessor
 |      Accessor for computing and plotting metrics.
 |
 |  inspection : InspectionAccessor
 |      Accessor for model inspection (coefficients, feature importance, etc.).
 |
 |  data : DataAccessor
 |      Accessor for dataset analysis.
 |
 |  checks : ChecksAccessor
 |      Accessor for running diagnostic checks.
 |
 |  See Also
 |  --------
 |  skore.evaluate
 |      Evaluate one or more estimators and return a report.
 |
 |  skore.CrossValidationReport
 |      Report of cross-validation results.
 |
 |  skore.ComparisonReport
 |      Report of comparison between estimators.
 |
 |  Examples
 |  --------
 |  >>> from sklearn.datasets import make_classification
 |  >>> from sklearn.model_selection import train_test_split
 |  >>> from sklearn.linear_model import LogisticRegression
 |  >>> X, y = make_classification(random_state=42)
 |  >>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
 |  >>> estimator = LogisticRegression()
 |  >>> from skore import EstimatorReport
 |  >>> report = EstimatorReport(
 |  ...     estimator, X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test
 |  ... )
 |
 |  Method resolution order:
 |      EstimatorReport
 |      skore._sklearn._base._BaseReport
 |      skore._utils.repr.base.ReportHelpMixin
 |      skore._utils.repr.rich_repr._RichReportHelpMixin
 |      skore._utils.repr.html_repr._HTMLReportHelpMixin
 |      skore._utils.repr.data._ReportHelpDataMixin
 |      skore._utils.repr.data._BaseHelpDataMixin
 |      skore._utils.repr.rich_repr._BaseRichHelpMixin
 |      skore._utils.repr.html_repr._BaseHTMLHelpMixin
 |      abc.ABC
 |      skore._externals._pandas_accessors.DirNamesMixin
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, estimator: 'EstimatorLike', *, X_train: 'ArrayLike | None' = None, y_train: 'ArrayLike | None' = None, X_test: 'ArrayLike | None' = None, y_test: 'ArrayLike | None' = None, train_data: 'dict | None' = None, test_data: 'dict | None' = None, pos_label: 'PositiveLabel | None' = None) -> 'None'
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self) -> 'str'
 |      Return a string representation.
 |
 |  get_predictions(self, *, data_source: 'DataSource', response_method: "Literal['predict', 'predict_proba', 'decision_function']" = 'predict') -> 'ArrayLike'
 |      Get estimator's predictions.
 |
 |      This method has the advantage to reload from the cache if the predictions
 |      were already computed in a previous call.
 |
 |      Parameters
 |      ----------
 |      data_source : {"test", "train"}
 |          The data source to use.
 |
 |          - "test" : use the test set provided when creating the report.
 |          - "train" : use the train set provided when creating the report.
 |
 |      response_method : {"predict", "predict_proba", "decision_function"},                 default="predict"
 |          The response method to use to get the predictions.
 |
 |      Returns
 |      -------
 |      np.ndarray of shape (n_samples,) or (n_samples, n_classes)
 |          The predictions.
 |
 |      Raises
 |      ------
 |      ValueError
 |          If the data source is invalid.
 |
 |      Examples
 |      --------
 |      >>> from sklearn.datasets import load_breast_cancer
 |      >>> from sklearn.linear_model import LogisticRegression
 |      >>> from skore import evaluate
 |      >>> X, y = load_breast_cancer(return_X_y=True)
 |      >>> classifier = LogisticRegression(max_iter=10_000)
 |      >>> report = evaluate(classifier, X, y, splitter=0.2)
 |      >>> predictions = report.get_predictions(data_source="test")
 |      >>> predictions.shape
 |      (114,)
 |
 |  to_dict(self) -> 'dict[str, Any]'
 |      Return a serializable representation of the report state.
 |
 |      This state is meant to ease serialization/deserialization of
 |      reports while preserving some backward compatibility across skore
 |      versions. In particular, this is more stable than pickling a report
 |      object directly, which can break when internal implementations change.
 |
 |  to_markdown(self) -> 'str'
 |      Return a markdown summary of the report.
 |
 |      The summary contains four sections (Estimator, Metrics, Checks, Data) that
 |      mirror the tabs of the HTML representation. Each section ends with a pointer
 |      to the corresponding accessor for full details.
 |
 |      Returns
 |      -------
 |      str
 |          The markdown summary of the report.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  from_dict(state: 'dict[str, Any]') -> 'EstimatorReport' from abc.ABCMeta
 |      Build a report from :meth:`to_dict` output.
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties defined here:
 |
 |  X_test
 |
 |  X_train
 |
 |  estimator_
 |      The report's fitted estimator.
 |
 |  estimator_name_
 |
 |  ml_task
 |
 |  pos_label
 |
 |  test_data
 |
 |  train_data
 |
 |  y_test
 |
 |  y_train
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __abstractmethods__ = frozenset()
 |
 |  __annotations__ = {'_ACCESSOR_CONFIG': 'dict[str, dict[str, str]]', '_...
 |
 |  checks = <class 'skore._sklearn._checks.accessor._ChecksAccessor'>
 |      Accessor for checks-related operations.
 |
 |      You can access this accessor using the `checks` attribute.
 |
 |
 |  data = <class 'skore._sklearn._estimator.data_accessor._DataAccessor'>
 |      The data accessor helps you to get insights about the train and test datasets.
 |
 |      It provides methods to create plots and to visualise the datasets.
 |
 |
 |  inspection = <class 'skore._sklearn._estimator.inspection_accessor._In...
 |      Accessor for model inspection related operations.
 |
 |      You can access this accessor using the `inspection` attribute.
 |
 |
 |  metrics = <class 'skore._sklearn._estimator.metrics_accessor._MetricsA...
 |      Accessor for metrics-related operations.
 |
 |      You can access this accessor using the `metrics` attribute.
 |
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from skore._sklearn._base._BaseReport:
 |
 |  __setstate__(self, state: 'dict[str, Any]') -> 'None'
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from skore._sklearn._base._BaseReport:
 |
 |  id
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from skore._utils.repr.base.ReportHelpMixin:
 |
 |  help(self) -> '_HelpDisplay | None'
 |      Display report help using rich or HTML.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from skore._utils.repr.data._BaseHelpDataMixin:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from skore._externals._pandas_accessors.DirNamesMixin:
 |
 |  __dir__(self) -> list[str]
 |      Default dir() implementation.

```
