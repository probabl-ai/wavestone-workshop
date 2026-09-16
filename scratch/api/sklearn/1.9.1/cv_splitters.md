# CV splitters (KFold, TimeSeriesSplit)

Source: inspect: sklearn @ 1.9.1
Probed: 2025-09-15

## KFold

### Signature
```
(n_splits=5, *, shuffle=False, random_state=None)
```

### help()
```
Python Library Documentation: class KFold in module sklearn.model_selection._split

class KFold(_UnsupportedGroupCVMixin, _BaseKFold)
 |  KFold(n_splits=5, *, shuffle=False, random_state=None)
 |
 |  K-Fold cross-validator.
 |
 |  Provides train/test indices to split data in train/test sets. Split
 |  dataset into k consecutive folds (without shuffling by default).
 |
 |  Each fold is then used once as a validation while the k - 1 remaining
 |  folds form the training set.
 |
 |  Read more in the :ref:`User Guide <k_fold>`.
 |
 |  For visualisation of cross-validation behaviour and
 |  comparison between common scikit-learn split methods
 |  refer to :ref:`sphx_glr_auto_examples_model_selection_plot_cv_indices.py`
 |
 |  Parameters
 |  ----------
 |  n_splits : int, default=5
 |      Number of folds. Must be at least 2.
 |
 |      .. versionchanged:: 0.22
 |          ``n_splits`` default value changed from 3 to 5.
 |
 |  shuffle : bool, default=False
 |      Whether to shuffle the data before splitting into batches.
 |      Note that the samples within each split will not be shuffled.
 |
 |  random_state : int, RandomState instance or None, default=None
 |      When `shuffle` is True, `random_state` affects the ordering of the
 |      indices, which controls the randomness of each fold. Otherwise, this
 |      parameter has no effect.
 |      Pass an int for reproducible output across multiple function calls.
 |      See :term:`Glossary <random_state>`.
 |
 |  Examples
 |  --------
 |  >>> import numpy as np
 |  >>> from sklearn.model_selection import KFold
 |  >>> X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
 |  >>> y = np.array([1, 2, 3, 4])
 |  >>> kf = KFold(n_splits=2)
 |  >>> kf.get_n_splits()
 |  2
 |  >>> print(kf)
 |  KFold(n_splits=2, random_state=None, shuffle=False)
 |  >>> for i, (train_index, test_index) in enumerate(kf.split(X)):
 |  ...     print(f"Fold {i}:")
 |  ...     print(f"  Train: index={train_index}")
 |  ...     print(f"  Test:  index={test_index}")
 |  Fold 0:
 |    Train: index=[2 3]
 |    Test:  index=[0 1]
 |  Fold 1:
 |    Train: index=[0 1]
 |    Test:  index=[2 3]
 |
 |  Notes
 |  -----
 |  The first ``n_samples % n_splits`` folds have size
 |  ``n_samples // n_splits + 1``, other folds have size
 |  ``n_samples // n_splits``, where ``n_samples`` is the number of samples.
 |
 |  Randomized CV splitters may return different results for each call of
 |  split. You can make the results identical by setting `random_state`
 |  to an integer.
 |
 |  See Also
 |  --------
 |  StratifiedKFold : Takes class information into account to avoid building
 |      folds with imbalanced class distributions (for binary or multiclass
 |      classification tasks).
 |
 |  GroupKFold : K-fold iterator variant with non-overlapping groups.
 |
 |  RepeatedKFold : Repeats K-Fold n times.
 |
 |  Method resolution order:
 |      KFold
 |      _UnsupportedGroupCVMixin
 |      _BaseKFold
 |      BaseCrossValidator
 |      sklearn.utils._metadata_requests._MetadataRequester
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, n_splits=5, *, shuffle=False, random_state=None)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __abstractmethods__ = frozenset()
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from _UnsupportedGroupCVMixin:
 |
 |  split(self, X, y=None, groups=None)
 |      Generate indices to split data into training and test set.
 |
 |      Parameters
 |      ----------
 |      X : array-like of shape (n_samples, n_features)
 |          Training data, where `n_samples` is the number of samples
 |          and `n_features` is the number of features.
 |
 |      y : array-like of shape (n_samples,), default=None
 |          The target variable for supervised learning problems.
 |
 |      groups : array-like of shape (n_samples,), default=None
 |          Always ignored, exists for API compatibility.
 |
 |      Yields
 |      ------
 |      train : ndarray
 |          The training set indices for that split.
 |
 |      test : ndarray
 |          The testing set indices for that split.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from _UnsupportedGroupCVMixin:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from _BaseKFold:
 |
 |  get_n_splits(self, X=None, y=None, groups=None)
 |      Returns the number of splitting iterations as set with the `n_splits` param
 |      when instantiating the cross-validator.
 |
 |      Parameters
 |      ----------
 |      X : array-like of shape (n_samples, n_features), default=None
 |          Always ignored, exists for API compatibility.
 |
 |      y : array-like of shape (n_samples,), default=None
 |          Always ignored, exists for API compatibility.
 |
 |      groups : array-like of shape (n_samples,), default=None
 |          Always ignored, exists for API compatibility.
 |
 |      Returns
 |      -------
 |      n_splits : int
 |          Returns the number of splitting iterations in the cross-validator.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseCrossValidator:
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.utils._metadata_requests._MetadataRequester:
 |
 |  get_metadata_routing(self)
 |      Get metadata routing of this object.
 |
 |      Please check :ref:`User Guide <metadata_routing>` on how the routing
 |      mechanism works.
 |
 |      Returns
 |      -------
 |      routing : MetadataRequest
 |          A :class:`~sklearn.utils.metadata_routing.MetadataRequest` encapsulating
 |          routing information.
 |
 |  ----------------------------------------------------------------------
 |  Class methods inherited from sklearn.utils._metadata_requests._MetadataRequester:
 |
 |  __init_subclass__(**kwargs) from abc.ABCMeta
 |      Set the ``set_{method}_request`` methods.
 |
 |      This uses PEP-487 [1]_ to set the ``set_{method}_request`` methods. It
 |      looks for the information available in the set default values which are
 |      set using ``__metadata_request__*`` class attributes, or inferred
 |      from method signatures.
 |
 |      The ``__metadata_request__*`` class attributes are used when a method
 |      does not explicitly accept a metadata through its arguments or if the
 |      developer would like to specify a request value for those metadata
 |      which are different from the default ``None``.
 |
 |      References
 |      ----------
 |      .. [1] https://www.python.org/dev/peps/pep-0487

```

## TimeSeriesSplit

### Signature
```
(n_splits=5, *, max_train_size=None, test_size=None, gap=0)
```

### help()
```
Python Library Documentation: class TimeSeriesSplit in module sklearn.model_selection._split

class TimeSeriesSplit(_BaseKFold)
 |  TimeSeriesSplit(n_splits=5, *, max_train_size=None, test_size=None, gap=0)
 |
 |  Time Series cross-validator.
 |
 |  Provides train/test indices to split time-ordered data, where other
 |  cross-validation methods are inappropriate, as they would lead to training
 |  on future data and evaluating on past data.
 |  To ensure comparable metrics across folds, samples must be equally spaced.
 |  Once this condition is met, each test set covers the same time duration,
 |  while the train set size accumulates data from previous splits.
 |
 |  This cross-validation object is a variation of :class:`KFold`.
 |  In the k-th split, it returns the first k folds as the train set and the
 |  (k+1)-th fold as the test set.
 |
 |  Note that, unlike standard cross-validation methods, successive
 |  training sets are supersets of those that come before them.
 |
 |  Read more in the :ref:`User Guide <time_series_split>`.
 |
 |  For visualisation of cross-validation behaviour and
 |  comparison between common scikit-learn split methods
 |  refer to :ref:`sphx_glr_auto_examples_model_selection_plot_cv_indices.py`
 |
 |  .. versionadded:: 0.18
 |
 |  Parameters
 |  ----------
 |  n_splits : int, default=5
 |      Number of splits. Must be at least 2.
 |
 |      .. versionchanged:: 0.22
 |          ``n_splits`` default value changed from 3 to 5.
 |
 |  max_train_size : int, default=None
 |      Maximum size for a single training set.
 |
 |  test_size : int, default=None
 |      Used to limit the size of the test set. Defaults to
 |      ``n_samples // (n_splits + 1)``, which is the maximum allowed value
 |      with ``gap=0``.
 |
 |      .. versionadded:: 0.24
 |
 |  gap : int, default=0
 |      Number of samples to exclude from the end of each train set before
 |      the test set.
 |
 |      .. versionadded:: 0.24
 |
 |  Examples
 |  --------
 |  >>> import numpy as np
 |  >>> from sklearn.model_selection import TimeSeriesSplit
 |  >>> X = np.array([[1, 2], [3, 4], [1, 2], [3, 4], [1, 2], [3, 4]])
 |  >>> y = np.array([1, 2, 3, 4, 5, 6])
 |  >>> tscv = TimeSeriesSplit()
 |  >>> print(tscv)
 |  TimeSeriesSplit(gap=0, max_train_size=None, n_splits=5, test_size=None)
 |  >>> for i, (train_index, test_index) in enumerate(tscv.split(X)):
 |  ...     print(f"Fold {i}:")
 |  ...     print(f"  Train: index={train_index}")
 |  ...     print(f"  Test:  index={test_index}")
 |  Fold 0:
 |    Train: index=[0]
 |    Test:  index=[1]
 |  Fold 1:
 |    Train: index=[0 1]
 |    Test:  index=[2]
 |  Fold 2:
 |    Train: index=[0 1 2]
 |    Test:  index=[3]
 |  Fold 3:
 |    Train: index=[0 1 2 3]
 |    Test:  index=[4]
 |  Fold 4:
 |    Train: index=[0 1 2 3 4]
 |    Test:  index=[5]
 |  >>> # Fix test_size to 2 with 12 samples
 |  >>> X = np.random.randn(12, 2)
 |  >>> y = np.random.randint(0, 2, 12)
 |  >>> tscv = TimeSeriesSplit(n_splits=3, test_size=2)
 |  >>> for i, (train_index, test_index) in enumerate(tscv.split(X)):
 |  ...     print(f"Fold {i}:")
 |  ...     print(f"  Train: index={train_index}")
 |  ...     print(f"  Test:  index={test_index}")
 |  Fold 0:
 |    Train: index=[0 1 2 3 4 5]
 |    Test:  index=[6 7]
 |  Fold 1:
 |    Train: index=[0 1 2 3 4 5 6 7]
 |    Test:  index=[8 9]
 |  Fold 2:
 |    Train: index=[0 1 2 3 4 5 6 7 8 9]
 |    Test:  index=[10 11]
 |  >>> # Add in a 2 period gap
 |  >>> tscv = TimeSeriesSplit(n_splits=3, test_size=2, gap=2)
 |  >>> for i, (train_index, test_index) in enumerate(tscv.split(X)):
 |  ...     print(f"Fold {i}:")
 |  ...     print(f"  Train: index={train_index}")
 |  ...     print(f"  Test:  index={test_index}")
 |  Fold 0:
 |    Train: index=[0 1 2 3]
 |    Test:  index=[6 7]
 |  Fold 1:
 |    Train: index=[0 1 2 3 4 5]
 |    Test:  index=[8 9]
 |  Fold 2:
 |    Train: index=[0 1 2 3 4 5 6 7]
 |    Test:  index=[10 11]
 |
 |  For a more extended example see
 |  :ref:`sphx_glr_auto_examples_applications_plot_cyclical_feature_engineering.py`.
 |
 |  Notes
 |  -----
 |  The training set has size ``i * n_samples // (n_splits + 1)
 |  + n_samples % (n_splits + 1)`` in the ``i`` th split,
 |  with a test set of size ``n_samples//(n_splits + 1)`` by default,
 |  where ``n_samples`` is the number of samples. Note that this
 |  formula is only valid when ``test_size`` and ``max_train_size`` are
 |  left to their default values.
 |
 |  Method resolution order:
 |      TimeSeriesSplit
 |      _BaseKFold
 |      BaseCrossValidator
 |      sklearn.utils._metadata_requests._MetadataRequester
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, n_splits=5, *, max_train_size=None, test_size=None, gap=0)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  split(self, X, y=None, groups=None)
 |      Generate indices to split data into training and test set.
 |
 |      Parameters
 |      ----------
 |      X : array-like of shape (n_samples, n_features)
 |          Training data, where `n_samples` is the number of samples
 |          and `n_features` is the number of features.
 |
 |      y : array-like of shape (n_samples,), default=None
 |          Always ignored, exists for API compatibility.
 |
 |      groups : array-like of shape (n_samples,), default=None
 |          Always ignored, exists for API compatibility.
 |
 |      Yields
 |      ------
 |      train : ndarray
 |          The training set indices for that split.
 |
 |      test : ndarray
 |          The testing set indices for that split.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __abstractmethods__ = frozenset()
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from _BaseKFold:
 |
 |  get_n_splits(self, X=None, y=None, groups=None)
 |      Returns the number of splitting iterations as set with the `n_splits` param
 |      when instantiating the cross-validator.
 |
 |      Parameters
 |      ----------
 |      X : array-like of shape (n_samples, n_features), default=None
 |          Always ignored, exists for API compatibility.
 |
 |      y : array-like of shape (n_samples,), default=None
 |          Always ignored, exists for API compatibility.
 |
 |      groups : array-like of shape (n_samples,), default=None
 |          Always ignored, exists for API compatibility.
 |
 |      Returns
 |      -------
 |      n_splits : int
 |          Returns the number of splitting iterations in the cross-validator.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseCrossValidator:
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.utils._metadata_requests._MetadataRequester:
 |
 |  get_metadata_routing(self)
 |      Get metadata routing of this object.
 |
 |      Please check :ref:`User Guide <metadata_routing>` on how the routing
 |      mechanism works.
 |
 |      Returns
 |      -------
 |      routing : MetadataRequest
 |          A :class:`~sklearn.utils.metadata_routing.MetadataRequest` encapsulating
 |          routing information.
 |
 |  ----------------------------------------------------------------------
 |  Class methods inherited from sklearn.utils._metadata_requests._MetadataRequester:
 |
 |  __init_subclass__(**kwargs) from abc.ABCMeta
 |      Set the ``set_{method}_request`` methods.
 |
 |      This uses PEP-487 [1]_ to set the ``set_{method}_request`` methods. It
 |      looks for the information available in the set default values which are
 |      set using ``__metadata_request__*`` class attributes, or inferred
 |      from method signatures.
 |
 |      The ``__metadata_request__*`` class attributes are used when a method
 |      does not explicitly accept a metadata through its arguments or if the
 |      developer would like to specify a request value for those metadata
 |      which are different from the default ``None``.
 |
 |      References
 |      ----------
 |      .. [1] https://www.python.org/dev/peps/pep-0487
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from sklearn.utils._metadata_requests._MetadataRequester:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

```
