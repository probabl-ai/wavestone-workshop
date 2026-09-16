# skore.CrossValidationReport

Source: inspect: skore @ 0.25.0
Probed: 2025-09-15

## CrossValidationReport

### Signature
```
(estimator: 'EstimatorLike', X: 'ArrayLike | None' = None, y: 'ArrayLike | None' = None, data: 'dict | None' = None, pos_label: 'PositiveLabel | None' = None, splitter: 'int | SKLearnCrossValidator | Generator | None' = None, n_jobs: 'int | None' = None) -> 'None'
```

### help()
```
Python Library Documentation: class CrossValidationReport in module skore._sklearn._cross_validation.report

class CrossValidationReport(skore._sklearn._base._BaseReport, skore._externals._pandas_accessors.DirNamesMixin)
 |  CrossValidationReport(estimator: 'EstimatorLike', X: 'ArrayLike | None' = None, y: 'ArrayLike | None' = None, data: 'dict | None' = None, pos_label: 'PositiveLabel | None' = None, splitter: 'int | SKLearnCrossValidator | Generator | None' = None, n_jobs: 'int | None' = None) -> 'None'
 |
 |  Provide a report of cross-validation results.
 |
 |  Upon initialization, clones ``estimator`` according to ``splitter`` and fits each
 |  fold in parallel.
 |
 |  Refer to the :ref:`cross_validation_report` section of the user guide for more
 |  details.
 |
 |  Parameters
 |  ----------
 |  estimator : estimator object
 |      Estimator to make the cross-validation report from. An estimator can
 |      be one of the following:
 |
 |      - a scikit-learn compatible estimator as a :class:`~sklearn.base.BaseEstimator`;
 |      - a skrub :class:`~skrub.DataOp` to preprocess the data;
 |      - a skrub :class:`~skrub.SkrubLearner` extracted from a :class:`~skrub.DataOp`
 |        by calling :meth:`~skrub.DataOp.skb.make_learner`.
 |
 |  X : {array-like, sparse matrix} of shape (n_samples, n_features) or None
 |      The data to fit. Can be for example a list, or an array.
 |
 |  y : array-like of shape (n_samples,) or (n_samples, n_outputs) or None
 |      The target variable to try to predict in the case of supervised learning.
 |
 |  data : dict or None
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
 |  splitter : int, cross-validation generator or an iterable, default=5
 |      Determines the cross-validation splitting strategy.
 |      Possible inputs for `splitter` are:
 |
 |      - int, to specify the number of splits in a `(Stratified)KFold`,
 |      - a scikit-learn :term:`CV splitter`,
 |      - An iterable yielding (train, test) splits as arrays of indices.
 |
 |      For int/None inputs, if the estimator is a classifier and ``y`` is
 |      either binary or multiclass, :class:`StratifiedKFold` is used. In all
 |      other cases, :class:`KFold` is used. These splitters are instantiated
 |      with `shuffle=False` so the splits will be the same across calls.
 |
 |      Refer to scikit-learn's :ref:`User Guide <cross_validation>` for the various
 |      cross-validation strategies that can be used here.
 |
 |  n_jobs : int, default=None
 |      Number of jobs to run in parallel. Training the estimator and computing
 |      the score are parallelized over the cross-validation splits.
 |      When accessing some methods of the `CrossValidationReport`, the `n_jobs`
 |      parameter is used to parallelize the computation.
 |      ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
 |      ``-1`` means using all processors.
 |
 |  Attributes
 |  ----------
 |  estimator_ : estimator object
 |      The fitted estimator.
 |
 |  estimator : estimator object
 |      The estimator that was given as input.
 |
 |  learner_ : skrub.SkrubLearner
 |      The estimator wrapped in a skrub Learner.
 |
 |  estimator_name_ : str
 |      The name of the estimator.
 |
 |  reports_ : list of EstimatorReport
 |      The estimator reports for each split.
 |
 |  ml_task : str
 |      The machine learning task inferred from the data and estimator.
 |
 |  metrics : MetricsAccessor
 |      Accessor for computing and plotting metrics aggregated over folds.
 |
 |  inspection : InspectionAccessor
 |      Accessor for model inspection aggregated over folds.
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
 |  skore.EstimatorReport
 |      Report for a fitted estimator.
 |
 |  skore.ComparisonReport
 |      Report of comparison between estimators.
 |
 |  Examples
 |  --------
 |  >>> from sklearn.datasets import make_classification
 |  >>> from sklearn.linear_model import LogisticRegression
 |  >>> X, y = make_classification(random_state=42)
 |  >>> estimator = LogisticRegression()
 |  >>> from skore import CrossValidationReport
 |  >>> report = CrossValidationReport(estimator, X=X, y=y, splitter=2)
 |
 |  Method resolution order:
 |      CrossValidationReport
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
 |  __init__(self, estimator: 'EstimatorLike', X: 'ArrayLike | None' = None, y: 'ArrayLike | None' = None, data: 'dict | None' = None, pos_label: 'PositiveLabel | None' = None, splitter: 'int | SKLearnCrossValidator | Generator | None' = None, n_jobs: 'int | None' = None) -> 'None'
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self) -> 'str'
 |      Return a string representation.
 |
 |  create_estimator_report(self, *, X_test: 'ArrayLike | None' = None, y_test: 'ArrayLike | None' = None, test_data: 'dict | None' = None) -> 'EstimatorReport'
 |      Create an estimator report from the cross-validation report.
 |
 |      This method creates a new :class:`~skore.EstimatorReport` with the same
 |      estimator and the same data as the cross-validation report. It is useful to
 |      evaluate and deploy a model that was deemed optimal with cross-validation.
 |      Provide a held-out test set to properly evaluate the performance of the model.
 |
 |      Parameters
 |      ----------
 |      X_test : {array-like, sparse matrix} of shape (n_samples, n_features)
 |          Testing data. It should have the same structure as the training data.
 |
 |      y_test : array-like of shape (n_samples,) or (n_samples, n_outputs)
 |          Testing target.
 |
 |      test_data : dict or None
 |          When ``estimator`` is a skrub :class:`~skrub.SkrubLearner`, bindings for
 |          variables contained in the DataOp that was used to create this learner
 |          (e.g. ``{"X": X_df, "other_table": df, ...}``).
 |
 |      Returns
 |      -------
 |      :class:`~skore.EstimatorReport`
 |          The estimator report.
 |
 |      Examples
 |      --------
 |      >>> from sklearn.datasets import make_classification
 |      >>> from sklearn.ensemble import RandomForestClassifier
 |      >>> from sklearn.model_selection import train_test_split
 |      >>> from skore import evaluate
 |      >>> X, y = make_classification(random_state=42)
 |      >>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
 |      >>> forest_report = evaluate(
 |      ...     RandomForestClassifier(random_state=42), X_train, y_train, splitter=5
 |      ... )
 |      >>> final_report = forest_report.create_estimator_report(
 |      ...     X_test=X_test, y_test=y_test
 |      ... )
 |      >>> final_report.metrics.summarize().frame()
 |
 |  get_predictions(self, *, data_source: "Literal['train', 'test']", response_method: "Literal['predict', 'predict_proba', 'decision_function']" = 'predict') -> 'list[ArrayLike]'
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
 |      list of np.ndarray of shape (n_samples,) or (n_samples, n_classes)
 |          The predictions for each cross-validation split.
 |
 |      Examples
 |      --------
 |      >>> from sklearn.datasets import make_classification
 |      >>> from sklearn.linear_model import LogisticRegression
 |      >>> X, y = make_classification(random_state=42)
 |      >>> estimator = LogisticRegression()
 |      >>> from skore import CrossValidationReport
 |      >>> report = CrossValidationReport(estimator, X=X, y=y, splitter=2)
 |      >>> predictions = report.get_predictions(data_source="test")
 |      >>> print([split_predictions.shape for split_predictions in predictions])
 |      [(50,), (50,)]
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
 |      The summary contains four sections (Results, Checks, Estimator, Data) that
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
 |  from_dict(state: 'dict[str, Any]') -> 'CrossValidationReport' from abc.ABCMeta
 |      Rebuild a report from :meth:`to_dict` output.
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties defined here:
 |
 |  X
 |
 |  estimator_
 |      The report's fitted estimator.
 |
 |  estimator_name_
 |
 |  input_data
 |
 |  ml_task
 |
 |  pos_label
 |
 |  split_indices
 |
 |  splitter
 |
 |  y
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
 |  data = <class 'skore._sklearn._cross_validation.data_accessor._DataAcc...
 |      The data accessor helps you to get insights about the dataset used.
 |
 |      It provides methods to create plots and to visualise the dataset.
 |
 |
 |  inspection = <class 'skore._sklearn._cross_validation.inspection_acces...
 |      Accessor for model inspection related operations.
 |
 |      You can access this accessor using the `inspection` attribute.
 |
 |
 |  metrics = <class 'skore._sklearn._cross_validation.metrics_accessor._M...
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
