# data_ops_core

Source: inspect: skrub DataOps core @ 0.10.1
Probed: 2026-09-16

## skrub.var

## Signature

```python
skrub.var(name, value=NULL, *, becomes_default=False)
```

## help() — skrub.var

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

## skrub.var().skb.mark_as_X

## Signature

```python
skrub.var().skb.mark_as_X(*, cv=None, split_kwargs=None)
```

## help() — skrub.var().skb.mark_as_X

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

## skrub.var().skb.mark_as_y

## Signature

```python
skrub.var().skb.mark_as_y()
```

## help() — skrub.var().skb.mark_as_y

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

## skrub.var().skb.apply_func

## Signature

```python
skrub.var().skb.apply_func(func, *args, **kwargs)
```

## help() — skrub.var().skb.apply_func

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

## skrub.var().skb.make_learner

## Signature

```python
skrub.var().skb.make_learner(*, fitted=False, keep_subsampling=False, choose='default')
```

## help() — skrub.var().skb.make_learner

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
