# skrub DataOps core (var, apply, apply_func, mark_as_X/y, make_learner)

Source: inspect: skrub @ 0.10.1
Probed: 2025-09-15

## skrub.var

### Signature
```
(name, value=NULL, *, becomes_default=False)
```

### help()
```
Python Library Documentation: function var in module skrub._data_ops._data_ops

var(name, value=NULL, *, becomes_default=False)
    Create a skrub variable.

    Variables represent inputs to a DataOps plan, and the corresponding learner.
    They can be combined with other variables, constants, operators, function
    calls etc. to build up complex DataOps, which implicitly define the plan.

    See the example gallery for more information about skrub DataOps.

    Parameters
    ----------
    name : str
        The name for this input. It corresponds to a key in the dictionary that
        is passed to the learner's ``fit()`` method (see Examples below).
        Names must be unique within a learner and must not start with
        ``"_skrub_"``
    value : object, optional
        Optionally, an initial value can be given to the variable. When it is
        available, it is used to provide a preview of the learner's results,
        to detect errors in the learner early, and to provide better help and
        tab-completion in interactive Python shells.
    becomes_default : bool, default = False
        If True, the provided ``value`` is not only used for previews but also
        becomes the default value for this variable when creating a learner
        (for example with :meth:`DataOp.skb.make_learner`). Thus passing this
        variable in the environment is always optional.

    Returns
    -------
    A skrub variable

    Raises
    ------
    TypeError
        If the provided value is a skrub DataOp or a skrub choose_* function.

    See also
    --------
    skrub.X :
        Create a skrub variable and mark it as being ``X``.

    skrub.y :
        Create a skrub variable and mark it as being ``y``.

    Examples
    --------
    Variables without a value:

    >>> import skrub
    >>> a = skrub.var('a')
    >>> a
    <Var 'a'>
    >>> b = skrub.var('b')
    >>> c = a + b
    >>> c
    <BinOp: add>
    >>> print(c.skb.describe_steps())
    Var 'a'
    Var 'b'
    BinOp: add

    The names of variables correspond to keys in the inputs:

    >>> c.skb.eval({'a': 10, 'b': 6})
    16

    And also to keys to the inputs to the DataOps plan:

    >>> learner = c.skb.make_learner()
    >>> learner.fit_transform({'a': 5, 'b': 4})
    9

    When providing a value, we see what the learner produces for the values we
    provided:

    >>> a = skrub.var('a', 2)
    >>> b = skrub.var('b', 3)
    >>> b
    <Var 'b'>
    Result:
    ―――――――
    3
    >>> c = a + b
    >>> c
    <BinOp: add>
    Result:
    ―――――――
    5

    The values are also used for ``eval()`` when no environment is provided:

    >>> c.skb.eval()
    5

    But we can still override them. And inputs must be provided explicitly when
    using the learner returned by ``.skb.make_learner()``.

    >>> c.skb.eval({'a': 10, 'b': 6})
    16

    When passing ``becomes_default=True``, the preview value is treated as a
    default value for that variable. It is kept when cloning the DataOp or
    creating a Learner, and is always optional (does not need to be present) in
    the provided environment.

    >>> c = skrub.var('a', 0, becomes_default=True) + skrub.var('b', 1)
    >>> c.skb.get_data()
    {'a': 0, 'b': 1}
    >>> c.skb.clone().skb.get_data()
    {'a': 0}

    For the learner 'b' is mandatory but 'a' is optional and has default value
    0.

    >>> c.skb.make_learner().fit_transform({'b': 10})
    10
    >>> c.skb.make_learner().fit_transform({'b': 10, 'a': 100})
    110

    Much more information about skrub variables is provided in the examples
    gallery.

```

## DataOp.skb.apply

### Signature
```
(estimator, *, y=None, cols=all(), exclude_cols=None, no_wrap=False, how='auto', allow_reject=False, unsupervised=False, fit_kwargs=None, fit_transform_kwargs=None, transform_kwargs=None, predict_kwargs=None, predict_proba_kwargs=None, decision_function_kwargs=None, score_kwargs=None)
```

### help()
```
Python Library Documentation: method apply in module skrub._data_ops._skrub_namespace

apply(estimator, *, y=None, cols=all(), exclude_cols=None, no_wrap=False, how='auto', allow_reject=False, unsupervised=False, fit_kwargs=None, fit_transform_kwargs=None, transform_kwargs=None, predict_kwargs=None, predict_proba_kwargs=None, decision_function_kwargs=None, score_kwargs=None) method of skrub._data_ops._skrub_namespace.SkrubNamespace instance
    Apply an estimator that follows the scikit-learn API to a dataframe or numpy array.

    Parameters
    ----------
    estimator : scikit-learn estimator
        The transformer or predictor to apply.

    y : dataframe, column or numpy array, optional
        The prediction targets when ``estimator`` is a supervised estimator.

    cols : string, list of strings or skrub selector, optional
        The columns to transform, when ``estimator`` is a transformer.

    exclude_cols : string, list of strings or skrub selector, optional
        When ``estimator`` is a transformer, columns to which it should
        _not_ be applied. The columns that are matched by ``cols`` AND not
        matched by ``exclude_cols`` are transformed.

    no_wrap : bool, default = False
        Disable wrapping of transformers in :class:`ApplyToCols`.

        By default, when ``estimator`` is a transformer and the input is a
        DataFrame, the transformer is wrapped in an instance of
        :class:`ApplyToCols`, which allows applying it to part of the
        dataframe only through the ``cols`` and ``allow_reject``
        parameters. Passing ``no_wrap=True`` disables this wrapping in all
        cases. When ``no_wrap`` is True, ``cols`` and ``allow_reject``
        cannot be used.

    how : "auto", "cols", "frame" or "no_wrap", optional
        Deprecated. Use ``no_wrap`` instead.

        How the estimator is applied. In most cases the default "auto"
        is appropriate.

        - "cols" means `estimator` is wrapped in a :class:`ApplyToEachCol`
          transformer, which fits a separate clone of `estimator` each
          column in `cols`. `estimator` must be a transformer (have a
          ``fit_transform`` method).
        - "frame" means `estimator` is wrapped in a :class:`ApplyToSubFrame`
          transformer, which fits a single clone of `estimator` to the
          selected part of the input dataframe. `estimator` must be a
          transformer.
        - "no_wrap" means no wrapping, `estimator` is applied directly to
          the unmodified input.
        - "auto" chooses the wrapping depending on the input and estimator.
          If the input is not a dataframe or the estimator is not a
          transformer, the "no_wrap" strategy is chosen. Otherwise if the
          estimator has a ``__single_column_transformer__`` attribute,
          "cols" is chosen. Otherwise "frame" is chosen.

        .. deprecated:: 0.9.0

    allow_reject : bool, optional
        Whether the transformer can refuse to transform columns for which
        it does not apply, in which case they are passed through unchanged.
        This can be useful to avoid specifying exactly which columns should
        be transformed. For example if we apply :class:`~skrub.ToDatetime()`
        to all columns with ``allow_reject=True``, string columns that can be
        parsed as dates will be converted and all other columns will be
        passed through. If we use ``allow_reject=False`` (the default), an
        error would be raised if the dataframe contains columns for which
        :class:`~skrub.ToDatetime()` does not apply (eg a column of numbers).

    unsupervised : bool, optional
        Use this to indicate that ``y`` is required for scoring but not
        fitting, as is the case for clustering algorithms. If ``y`` is not
        required at all (for example when applying an unsupervised
        transformer, or when we are not interested in scoring with
        ground-truth labels), simply leave the default ``y=None`` and there
        is no need to pass a value for ``unsupervised``.

    fit_kwargs : dict, optional, default=None
        Extra named arguments to pass to the estimator's ``fit()`` method,
        for example ``fit_kwargs={'sample_weights': [.1, .5, .4]}``. May be
        (or contain) a DataOp, which will be evaluated before passing the
        kwargs to ``fit``.
    fit_transform_kwargs : dict, optional, default=None
        Extra named arguments for ``fit_transform``. See the description of
        the ``fit_kwargs`` parameter.
    transform_kwargs : dict, optional, default=None
        Extra named arguments for ``transform``. See the description of the
        ``fit_kwargs`` parameter.
    predict_kwargs : dict, optional, default=None
        Extra named arguments for ``predict``. See the description of the
        ``fit_kwargs`` parameter.
    predict_proba_kwargs : dict, optional, default=None
        Extra named arguments for ``predict_proba``. See the description of
        the ``fit_kwargs`` parameter.
    decision_function_kwargs : dict, optional, default=None
        Extra named arguments for ``decision_function``. See the
        description of the ``fit_kwargs`` parameter.
    score_kwargs : dict, optional, default=None
        Extra named arguments for ``score``. See the description of the
        ``fit_kwargs`` parameter.

    Returns
    -------
    result
        The transformed dataframe when ``estimator`` is a transformer, and
        the fitted ``estimator``'s predictions if it is a supervised
        predictor.

    See also
    --------
    skrub.DataOp.skb.make_learner :
        Get a skrub learner for this DataOp.
    skrub.ApplyToCols :
        Transformer that applies a given estimator to selected columns of a
        dataframe.

    Examples
    --------
    >>> import skrub
    >>> data = skrub.datasets.toy_orders()
    >>> x = skrub.X(data.X)
    >>> x
    <Var 'X'>
    Result:
    ―――――――
       ID product  quantity        date
    0   1     pen         2  2020-04-03
    1   2     cup         3  2020-04-04
    2   3     cup         5  2020-04-04
    3   4   spoon         1  2020-04-05

    >>> datetime_encoder = skrub.DatetimeEncoder(add_total_seconds=False)
    >>> x.skb.apply(skrub.TableVectorizer(datetime=datetime_encoder))
    <Apply TableVectorizer>
    Result:
    ―――――――
        ID  product_cup  product_pen  ...  date_year  date_month  date_day
    0  1.0          0.0          1.0  ...     2020.0         4.0       3.0
    1  2.0          1.0          0.0  ...     2020.0         4.0       4.0
    2  3.0          1.0          0.0  ...     2020.0         4.0       4.0
    3  4.0          0.0          0.0  ...     2020.0         4.0       5.0

    Transform only the ``'product'`` column:

    >>> x.skb.apply(skrub.StringEncoder(n_components=2), cols='product') # doctest: +SKIP
    <Apply StringEncoder>
    Result:
    ―――――――
       ID     product_0     product_1  quantity        date
    0   1 -2.560113e-16  1.000000e+00         2  2020-04-03
    1   2  1.000000e+00  7.447602e-17         3  2020-04-04
    2   3  1.000000e+00  7.447602e-17         5  2020-04-04
    3   4 -3.955170e-16 -8.326673e-17         1  2020-04-05

    Transform all but the ``'ID'`` and ``'quantity'`` columns:

    >>> x.skb.apply(
    ...     skrub.StringEncoder(n_components=2), exclude_cols=["ID", "quantity"]
    ... ) # doctest: +SKIP
    <Apply StringEncoder>
    Result:
    ―――――――
       ID     product_0     product_1  quantity    date_0    date_1
    0   1  9.775252e-08  7.830415e-01         2  0.766318 -0.406667
    1   2  9.999999e-01  0.000000e+00         3  0.943929  0.330148
    2   3  9.999998e-01 -1.490116e-08         5  0.943929  0.330149
    3   4  9.910963e-08 -6.219692e-01         1  0.766318 -0.406668

    More complex selection of the columns to transform, here all numeric
    columns except the ``'ID'``:

    >>> from sklearn.preprocessing import StandardScaler
    >>> from skrub import selectors as s

    >>> x.skb.apply(StandardScaler(), cols=s.numeric() - "ID")
    <Apply StandardScaler>
    Result:
    ―――――――
       ID product        date  quantity
    0   1     pen  2020-04-03 -0.507093
    1   2     cup  2020-04-04  0.169031
    2   3     cup  2020-04-04  1.521278
    3   4   spoon  2020-04-05 -1.183216

    For supervised estimators, pass the targets as the argument for ``y``:

    >>> from sklearn.dummy import DummyClassifier
    >>> y = skrub.y(data.y)
    >>> y
    <Var 'y'>
    Result:
    ―――――――
    0    False
    1    False
    2     True
    3    False
    Name: delayed, dtype: bool

    >>> x.skb.apply(skrub.TableVectorizer()).skb.apply(DummyClassifier(), y=y)
    <Apply DummyClassifier>
    Result:
    ―――――――
    0    False
    1    False
    2    False
    3    False
    Name: delayed, dtype: bool

    We can also pass additional keyword arguments to the estimator's
    methods. For example a StandardScaler can be passed sample weights.
    We first apply it without weights for comparison:

    >>> import pandas as pd
    >>> X = skrub.var("X", pd.DataFrame({"count": [10, 1], "value": [2.0, -2.0]}))
    >>> count, value = X["count"], X[["value"]]
    >>> value.skb.apply(StandardScaler())
    <Apply StandardScaler>
    Result:
    ―――――――
       value
    0    1.0
    1   -1.0

    Now we weight by ``count``. Note that ``count`` is itself a DataOp -- the
    kwargs, like X and y, can be computed during the DataOp's evaluation:

    >>> value.skb.apply(StandardScaler(), fit_transform_kwargs={"sample_weight": count})
    <Apply StandardScaler>
    Result:
    ―――――――
          value
    0  0.316...
    1 -3.162...

    Another example would be passing evaluation sets to the ``fit`` method
    of an ``xgboost`` estimator.

    Sometimes we want to pass a value for ``y`` because it is required for
    scoring and cross-validation, but it is not needed for fitting the
    estimator. In this case pass ``unsupervised=True``.

    >>> from sklearn.datasets import make_blobs
    >>> from sklearn.cluster import KMeans

    >>> X, y = make_blobs(n_samples=10, random_state=0)
    >>> e = skrub.X(X).skb.apply(
    ...     KMeans(n_clusters=2, n_init=1, random_state=0),
    ...     y=skrub.y(y),
    ...     unsupervised=True,
    ... )
    >>> e.skb.cross_validate()["test_score"]  # doctest: +SKIP
    0   -19.437348
    1   -12.463938
    2   -11.804288
    3   -37.238832
    4    -4.857855
    Name: test_score, dtype: float64
    >>> learner = e.skb.make_learner().fit({"X": X})
    >>> learner.predict({"X": X})  # doctest: +SKIP
    array([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], dtype=int32)

```

## DataOp.skb.apply_func

### Signature
```
(func, *args, **kwargs)
```

### help()
```
Python Library Documentation: method apply_func in module skrub._data_ops._skrub_namespace

apply_func(func, *args, **kwargs) method of skrub._data_ops._skrub_namespace.SkrubNamespace instance
    Apply the given function.

    This is a convenience function; ``X.skb.apply_func(func)`` is
    equivalent to ``skrub.deferred(func)(X)``.

    Parameters
    ----------
    func : function
        The function to apply to the DataOp.

    args
        additional positional arguments passed to ``func``.

    kwargs
        named arguments passed to ``func``.

    Returns
    -------
    data_op
        The DataOp that evaluates to the result of calling ``func`` as
        ``func(self, *args, **kwargs)``.

    Examples
    --------
    >>> import skrub

    >>> def count_words(text, sep=None):
    ...     return len(text.split(sep))

    >>> text = skrub.var("text", "Hello, world!")
    >>> text
    <Var 'text'>
    Result:
    ―――――――
    'Hello, world!'

    >>> count = text.skb.apply_func(count_words)
    >>> count
    <Call 'count_words'>
    Result:
    ―――――――
    2
    >>> count.skb.eval({"text": "one two three four"})
    4

    We can pass extra arguments:

    >>> text.skb.apply_func(count_words, sep="\n")
    <Call 'count_words'>
    Result:
    ―――――――
    1

    Using ``.skb.apply_func`` is the same as using ``deferred``, for example:

    >>> skrub.deferred(count_words)(text)
    <Call 'count_words'>
    Result:
    ―――――――
    2

```

## DataOp.skb.mark_as_X

### Signature
```
(*, cv=None, split_kwargs=None)
```

### help()
```
Python Library Documentation: method mark_as_X in module skrub._data_ops._skrub_namespace

mark_as_X(*, cv=None, split_kwargs=None) method of skrub._data_ops._skrub_namespace.SkrubNamespace instance
    Mark this DataOp as being the ``X`` table.

    Returns a copy; the original DataOp is left unchanged.

    This is used for train/test splits and cross-validation.
    To create a split,

    - The nodes that are marked as ``X`` and ``y`` are materialized: all
      the operations that come before are executed, to compute the value of
      ``X`` and ``y``.
    - Then the resulting tables are divided into train and test parts
      according to the splitting strategy.
    - For each split, the rest of the DataOp is fitted on the train set and
      tested on the test set.

    In addition, ``mark_as_X`` can be passed a splitter (``cv``) and named
    arguments for the splitter. Those will be evaluated at the same time as
    ``X`` and ``y`` and used to create the train/test splits.

    Parameters
    ----------
    cv : int, cross-validation iterator or iterable, default=None
        Cross-validation splitting strategy. It can be:

        - None: 5-fold (stratified) cross-validation
        - integer: specify the number of folds
        - sklearn `CV splitter <https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators>`_
        - iterable yielding (train, test) splits as arrays of indices.

    split_kwargs : dict or None, default=None
        Named arguments for the ``split()`` function (such as groups for a
        :class:`~sklearn.model_selection.GroupKFold`). Note that
        ``split_kwargs`` (and ``cv``) can themselves be DataOps.

    Returns
    -------
    A new DataOp, which has been marked as being the ``X`` table (which
    must be split for cross-validation).

    See also
    --------
    :meth:`DataOp.skb.mark_as_y`
        The equivalent of this function for the targets: mark a node as
        being the ``y`` table.
    :func:`skrub.X`
        ``skrub.X(value)`` can be used as a shorthand for
        ``skrub.var('X', value).skb.mark_as_X()``.
    :meth:`DataOp.skb.train_test_split`
        Prepare training and testing sets for a DataOp.
    :meth:`DataOp.skb.cross_validate`
        Perform cross-validation on a DataOp.
    :meth:`DataOp.skb.make_randomized_search`
        Perform hyperparameter tuning driven by cross-validation scores.
    :meth:`DataOp.skb.make_grid_search`
        Perform hyperparameter tuning driven by cross-validation scores.

    Notes
    -----
    During cross-validation, all the previous steps are first executed,
    until X and y (and the splitter and its additional arguments, if any)
    have been materialized. Then, X and y are split into training and
    testing sets. The following steps in the DataOp are fitted on the train
    data, and applied to test data, within each split.

    This means that any step that comes before ``mark_as_X()`` or
    ``mark_as_y()``, meaning that it is needed to compute X and y, sees the
    full dataset and cannot benefit from hyperparameter tuning. So we
    should be careful to start our learner by building X and y, and to use
    ``mark_as_X()`` and ``mark_as_y()`` as soon as possible.

    ``skrub.X(value)`` can be used as a shorthand for
    ``skrub.var('X', value).skb.mark_as_X()``.

    Examples
    --------
    >>> import skrub
    >>> orders = skrub.var('orders', skrub.datasets.toy_orders(split='all').orders)
    >>> features = orders.drop(columns='delayed', errors='ignore')
    >>> features.skb.is_X
    False
    >>> X = features.skb.mark_as_X()
    >>> X.skb.is_X
    True

    Note the original is left unchanged

    >>> features.skb.is_X
    False

    >>> y = orders['delayed'].skb.mark_as_y()
    >>> y.skb.is_y
    True

    Now if we run cross-validation:

    >>> from sklearn.dummy import DummyClassifier
    >>> pred = X.skb.apply(DummyClassifier(), y=y)
    >>> pred.skb.cross_validate(cv=2)['test_score']
    0    0.666667
    1    0.666667
    Name: test_score, dtype: float64

    First (outside of the cross-validation loop) ``X`` and ``y`` are
    computed. Then, they are split into training and test sets. Then the
    rest of the learner (in this case the last step, the
    ``DummyClassifier``) is evaluated on those splits.

    We can pass additional data to the cross-validation splitter by using
    the ``cv`` and ``split_kwargs`` parameters:

    >>> df = skrub.datasets.toy_products()
    >>> df
       description  price            seller     category
    0       screen    100   supermarket.com  electronics
    1       hammer     15  bestproducts.com        tools
    2     keyboard     20   supermarket.com  electronics
    3      usb key      9  bestproducts.com  electronics
    4      charger     13  bestproducts.com  electronics
    5  screwdriver     12   supermarket.com        tools

    Suppose we want to assess generalization to new sellers. While splitting for
    cross-validation we must group products by seller. We do it with
    :class:`sklearn.model_selection.LeaveOneGroupOut`.

    >>> from sklearn.dummy import DummyClassifier
    >>> from sklearn.model_selection import LeaveOneGroupOut

    >>> data = skrub.var("df", df)
    >>> groups = data["seller"]
    >>> X = data[["description", "price"]].skb.mark_as_X(
    ...     cv=LeaveOneGroupOut(), split_kwargs={"groups": groups}
    ... )
    >>> y = data["category"].skb.mark_as_y()
    >>> pred = X.skb.apply(DummyClassifier(), y=y)
    >>> split = pred.skb.train_test_split()

    The train set only contains data from the "bestproducts.com" seller.

    >>> split["X_train"]
      description  price
    1      hammer     15
    3     usb key      9
    4     charger     13

    The test set only contains data from the "supermarket.com" seller.

    >>> split["X_test"]
       description  price
    0       screen    100
    2     keyboard     20
    5  screwdriver     12

```

## DataOp.skb.mark_as_y

### Signature
```
()
```

### help()
```
Python Library Documentation: method mark_as_y in module skrub._data_ops._skrub_namespace

mark_as_y() method of skrub._data_ops._skrub_namespace.SkrubNamespace instance
    Mark this DataOp as being the ``y`` table.

    This is used for cross-validation and hyperparameter selection: operations
    done before :meth:`.skb.mark_as_X()` and :meth:`.skb.mark_as_y()` are executed
    on the entire data and cannot benefit from hyperparameter tuning.
    Returns a copy; the original DataOp is left unchanged.

    Returns
    -------
    The input DataOp, which has been marked as being ``y``

    Notes
    -----
    During cross-validation, all the previous steps are first executed,
    until X and y have been materialized. Then, those are split into
    training and testing sets. The following steps in the DataOp plan are
    fitted on the train data, and applied to test data, within each split.

    This means that any step that comes before ``mark_as_X()`` or
    ``mark_as_y()``, meaning that it is needed to compute X and y, sees the
    full dataset and cannot benefit from hyperparameter tuning. So we
    should be careful to start our learner by building X and y, and to use
    ``mark_as_X()`` and ``mark_as_y()`` as soon as possible.

    See also
    --------
    :func:`skrub.y`
        ``skrub.y(value)`` can be used as a shorthand for
        ``skrub.var('y', value).skb.mark_as_y()``.

    Examples
    --------
    >>> import skrub
    >>> orders = skrub.var('orders', skrub.datasets.toy_orders(split='all').orders)
    >>> X = orders.drop(columns='delayed', errors='ignore').skb.mark_as_X()
    >>> delayed = orders['delayed']
    >>> delayed.skb.is_y
    False
    >>> y = delayed.skb.mark_as_y()
    >>> y.skb.is_y
    True

    Note the original is left unchanged

    >>> delayed.skb.is_y
    False

    Now if we run cross-validation:

    >>> from sklearn.dummy import DummyClassifier
    >>> pred = X.skb.apply(DummyClassifier(), y=y)
    >>> pred.skb.cross_validate(cv=2)['test_score']
    0    0.666667
    1    0.666667
    Name: test_score, dtype: float64

    First (outside of the cross-validation loop) ``X`` and ``y`` are
    computed. Then, they are split into training and test sets. Then the
    rest of the learner (in this case the last step, the
    ``DummyClassifier``) is evaluated on those splits.

    Please see the examples gallery for more information.

```

## DataOp.skb.make_learner

### Signature
```
(*, fitted=False, keep_subsampling=False, choose='default')
```

### help()
```
Python Library Documentation: method make_learner in module skrub._data_ops._skrub_namespace

make_learner(*, fitted=False, keep_subsampling=False, choose='default') method of skrub._data_ops._skrub_namespace.SkrubNamespace instance
    Get a skrub learner for this DataOp.

    Returns a :class:`SkrubLearner` with a ``fit()`` method so it can be fit
    to some training data and then apply it to unseen data by calling
    ``transform()`` or ``predict()``. Unlike scikit-learn estimators, skrub
    learners accept a dictionary of inputs rather than ``X`` and ``y`` arguments.

    .. warning::

       If the DataOp contains choices (e.g. ``choose_from(...)``), by
       default this learner uses the default value of each choice. See the
       `choose` parameter for other options (random or from an
       `Optuna <https://optuna.readthedocs.io/en/stable/>`_ trial). To actually
       pick the best value with hyperparameter tuning, use
       :meth:`DataOp.skb.make_randomized_search`
       :meth:`DataOp.skb.make_grid_search` instead, or an Optuna
       :class:`~optuna.study.Study` as shown in this
       :ref:`example <example_optuna_choices>`.

    Parameters
    ----------
    fitted : bool (default=False)
        If true, the returned learner is fitted to the data provided when
        initializing variables in ``skrub.var("name", value=...)`` and
        ``skrub.X(value)``.

    keep_subsampling : bool (default=False)
        If True, and if subsampling has been configured (see
        :meth:`DataOp.skb.subsample`), fit on a subsample of the data. By
        default subsampling is not applied and all the data is used. This
        is only applied for fitting the estimator when ``fitted=True``,
        subsequent use of the estimator is not affected by subsampling.
        Therefore it is an error to pass ``keep_subsampling=True`` and
        ``fitted=False`` (because ``keep_subsampling=True`` would have no
        effect).

    choose : 'default', 'random', 'random([seed])' or                  :class:`optuna.Trial <optuna.trial.Trial>` instance
        How to resolve choices contained in the data_op. The different
        options are:

        - 'default': the corresponding parameters of the SkrubLearner are not
          set; the default values of the choices are used.
        - 'random': a random value is picked according to the distribution of
          each choice. The form 'random([seed])' is also accepted to set
          the random seed: for example 'random(0)' sets it to 0. 'random()'
          is the same as 'random'.
        - an instance of :class:`numpy.random.RandomState`. Same as 'random',
          but the provided RandomState is used to sample values.
        - an instance of :class:`optuna.Trial <optuna.trial.Trial>` or
          :class:`optuna.FrozenTrial <optuna.trial.FrozenTrial>`. It is
          used to suggest values for
          the choices.

        Note that none of these options picks the best choice value according to
        an evaluation criterion, as this function creates a single learner.
        These options can be combined with external logic to evaluate and
        select the resulting learners, or one of
        :meth:`DataOp.skb.make_grid_search`,
        :meth:`DataOp.skb.make_randomized_search`,
        :meth:`optuna.Study.optimize <optuna.study.Study.optimize>` (as
        shown in this :ref:`example <example_optuna_choices>`) can be used
        to automatically select the best hyperparameters.

    Returns
    -------
    learner
        A skrub learner with an interface similar to scikit-learn's, except
        that its methods accept a dictionary of named inputs rather than
        ``X`` and ``y`` arguments.

    Examples
    --------
    >>> import skrub
    >>> from sklearn.dummy import DummyClassifier
    >>> orders_df = skrub.datasets.toy_orders(split="train").orders
    >>> orders = skrub.var('orders', orders_df)
    >>> X = orders.drop(columns='delayed', errors='ignore').skb.mark_as_X()
    >>> y = orders['delayed'].skb.mark_as_y()
    >>> pred = X.skb.apply(skrub.TableVectorizer()).skb.apply(
    ...     DummyClassifier(), y=y
    ... )
    >>> pred
    <Apply DummyClassifier>
    Result:
    ―――――――
    0    False
    1    False
    2    False
    3    False
    Name: delayed, dtype: bool
    >>> learner = pred.skb.make_learner(fitted=True)
    >>> new_orders_df = skrub.datasets.toy_orders(split='test').X
    >>> new_orders_df
       ID product  quantity        date
    4   5     cup         5  2020-04-11
    5   6    fork         2  2020-04-12
    >>> learner.predict({'orders': new_orders_df})
    array([False, False])

    Note that the ``'orders'`` key in the dictionary passed to ``predict``
    corresponds to the name ``'orders'`` in ``skrub.var('orders',
    orders_df)`` above.

    The ``choose`` parameter allows us to control how choices contained in
    the DataOp should be handled. The default is to use the default value
    of each choice.

    >>> def mult(x, factor):
    ...     return x * factor
    >>> out = skrub.var("x").skb.apply_func(
    ...     mult, skrub.choose_int(-10, 10, default=2)
    ... )
    >>> out.skb.make_learner().fit_transform({'x': 1})
    2

    The 'random' option samples new choice outcomes for each created learner:

    >>> out.skb.make_learner(choose='random').fit_transform({'x': 1}) # doctest: +SKIP
    np.int64(3)
    >>> out.skb.make_learner(choose='random').fit_transform({'x': 1}) # doctest: +SKIP
    np.int64(-5)

    If an :class:`optuna.Trial <optuna.trial.Trial>` instance is passed
    instead, the choice outcomes are obtained by calling the trial's
    ``suggest_int``, ``suggest_float`` or ``suggest_categorical`` methods.
    This allows easily selecting hyperparameters with optuna.

    Please see the examples gallery for full information about DataOps
    and the learners they generate.

```
