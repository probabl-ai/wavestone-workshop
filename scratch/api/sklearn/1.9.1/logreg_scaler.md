# LogisticRegression + StandardScaler

Source: inspect: sklearn @ 1.9.1
Probed: 2025-09-15

## LogisticRegression

### Signature
```
(penalty='deprecated', *, C=1.0, l1_ratio=0.0, dual=False, tol=0.0001, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, verbose=0, warm_start=False, n_jobs=None)
```

### help()
```
Python Library Documentation: class LogisticRegression in module sklearn.linear_model._logistic

class LogisticRegression(sklearn.callback._callback_support.CallbackSupportMixin, sklearn.linear_model._base.LinearClassifierMixin, sklearn.linear_model._base.SparseCoefMixin, sklearn.base.BaseEstimator)
 |  LogisticRegression(penalty='deprecated', *, C=1.0, l1_ratio=0.0, dual=False, tol=0.0001, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, verbose=0, warm_start=False, n_jobs=None)
 |
 |  Logistic Regression (aka logit, MaxEnt) classifier.
 |
 |  This class implements regularized logistic regression using a set of available
 |  solvers. **Note that regularization is applied by default**. It can handle both
 |  dense and sparse input `X`. Use C-ordered arrays or CSR matrices containing 64-bit
 |  floats for optimal performance; any other input format will be converted (and
 |  copied).
 |
 |  The solvers 'lbfgs', 'newton-cg', 'newton-cholesky' and 'sag' support only L2
 |  regularization with primal formulation, or no regularization. The 'liblinear'
 |  solver supports both L1 and L2 regularization (but not both, i.e. elastic-net),
 |  with a dual formulation only for the L2 penalty. The Elastic-Net (combination of L1
 |  and L2) regularization is only supported by the 'saga' solver.
 |
 |  For :term:`multiclass` problems (whenever `n_classes >= 3`), all solvers except
 |  'liblinear' optimize the (penalized) multinomial loss. 'liblinear' only handles
 |  binary classification but can be extended to handle multiclass by using
 |  :class:`~sklearn.multiclass.OneVsRestClassifier`.
 |
 |  Read more in the :ref:`User Guide <logistic_regression>`.
 |
 |  Parameters
 |  ----------
 |  penalty : {'l1', 'l2', 'elasticnet', None}, default='l2'
 |      Specify the norm of the penalty:
 |
 |      - `None`: no penalty is added;
 |      - `'l2'`: add an L2 penalty term and it is the default choice;
 |      - `'l1'`: add an L1 penalty term;
 |      - `'elasticnet'`: both L1 and L2 penalty terms are added.
 |
 |      .. warning::
 |         Some penalties may not work with some solvers. See the parameter
 |         `solver` below, to know the compatibility between the penalty and
 |         solver.
 |
 |      .. versionadded:: 0.19
 |         l1 penalty with SAGA solver (allowing 'multinomial' + L1)
 |
 |      .. deprecated:: 1.8
 |         `penalty` was deprecated in version 1.8 and will be removed in 1.10.
 |         Use `l1_ratio` and `C` instead. `l1_ratio=0` for `penalty='l2'`,
 |         `l1_ratio=1` for `penalty='l1'`, `l1_ratio` set to any float between 0 and 1
 |         for `penalty='elasticnet'`, and `C=np.inf` for `penalty=None`.
 |
 |  C : float, default=1.0
 |      Inverse of regularization strength; must be a positive float.
 |      Like in support vector machines, smaller values specify stronger
 |      regularization. `C=np.inf` results in unpenalized logistic regression.
 |      For a visual example on the effect of tuning the `C` parameter
 |      with an L1 penalty, see:
 |      :ref:`sphx_glr_auto_examples_linear_model_plot_logistic_path.py`.
 |
 |  l1_ratio : float, default=0.0
 |      The Elastic-Net mixing parameter, with `0 <= l1_ratio <= 1`. Setting
 |      `l1_ratio=1` gives a pure L1-penalty, setting `l1_ratio=0` a pure L2-penalty.
 |      Any value between 0 and 1 gives an Elastic-Net penalty of the form
 |      `l1_ratio * L1 + (1 - l1_ratio) * L2`.
 |
 |      .. warning::
 |         Certain values of `l1_ratio`, i.e. some penalties, may not work with some
 |         solvers. See the parameter `solver` below, to know the compatibility between
 |         the penalty and solver.
 |
 |      .. versionchanged:: 1.8
 |          Default value changed from None to 0.0.
 |
 |      .. deprecated:: 1.8
 |          `None` is deprecated and will be removed in version 1.10. Always use
 |          `l1_ratio` to specify the penalty type.
 |
 |  dual : bool, default=False
 |      Dual (constrained) or primal (regularized, see also
 |      :ref:`this equation <regularized-logistic-loss>`) formulation. Dual formulation
 |      is only implemented for l2 penalty with liblinear solver. Prefer `dual=False`
 |      when n_samples > n_features.
 |
 |  tol : float, default=1e-4
 |      Tolerance for stopping criteria.
 |
 |  fit_intercept : bool, default=True
 |      Specifies if a constant (a.k.a. bias or intercept) should be
 |      added to the decision function.
 |
 |  intercept_scaling : float, default=1
 |      Useful only when the solver `liblinear` is used
 |      and `self.fit_intercept` is set to `True`. In this case, `x` becomes
 |      `[x, self.intercept_scaling]`,
 |      i.e. a "synthetic" feature with constant value equal to
 |      `intercept_scaling` is appended to the instance vector.
 |      The intercept becomes
 |      ``intercept_scaling * synthetic_feature_weight``.
 |
 |      .. note::
 |          The synthetic feature weight is subject to L1 or L2
 |          regularization as all other features.
 |          To lessen the effect of regularization on synthetic feature weight
 |          (and therefore on the intercept) `intercept_scaling` has to be increased.
 |
 |  class_weight : dict or 'balanced', default=None
 |      Weights associated with classes in the form ``{class_label: weight}``.
 |      If not given, all classes are supposed to have weight one.
 |
 |      The "balanced" mode uses the values of y to automatically adjust
 |      weights inversely proportional to class frequencies in the input data
 |      as ``n_samples / (n_classes * np.bincount(y))``.
 |
 |      Note that these weights will be multiplied with sample_weight (passed
 |      through the fit method) if sample_weight is specified.
 |
 |      .. versionadded:: 0.17
 |         *class_weight='balanced'*
 |
 |  random_state : int, RandomState instance, default=None
 |      Only used for `solver` == 'sag', 'saga' or 'liblinear' to shuffle the
 |      data. It has no effect on the other solvers.
 |      See :term:`Glossary <random_state>` for details.
 |
 |  solver : {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'},             default='lbfgs'
 |
 |      Algorithm to use in the optimization problem. Default is 'lbfgs'.
 |      To choose a solver, you might want to consider the following aspects:
 |
 |      - 'lbfgs' is a good default solver because it works reasonably well for a wide
 |        class of problems.
 |      - For :term:`multiclass` problems (`n_classes >= 3`), all solvers except
 |        'liblinear' minimize the full multinomial loss, 'liblinear' will raise an
 |        error.
 |      - 'newton-cholesky' is a good choice for
 |        `n_samples` >> `n_features * n_classes`, especially with one-hot encoded
 |        categorical features with rare categories. Be aware that the memory usage
 |        of this solver has a quadratic dependency on `n_features * n_classes`
 |        because it explicitly computes the full Hessian matrix.
 |      - For small datasets, 'liblinear' is a good choice, whereas 'sag'
 |        and 'saga' are faster for large ones;
 |      - 'liblinear' can only handle binary classification by default. To apply a
 |        one-versus-rest scheme for the multiclass setting one can wrap it with the
 |        :class:`~sklearn.multiclass.OneVsRestClassifier`.
 |
 |      .. warning::
 |         The choice of the algorithm depends on the penalty chosen (`l1_ratio=0`
 |         for L2-penalty, `l1_ratio=1` for L1-penalty and `0 < l1_ratio < 1` for
 |         Elastic-Net) and on (multinomial) multiclass support:
 |
 |         ================= ======================== ======================
 |         solver            l1_ratio                 multinomial multiclass
 |         ================= ======================== ======================
 |         'lbfgs'           l1_ratio=0               yes
 |         'liblinear'       l1_ratio=1 or l1_ratio=0 no
 |         'newton-cg'       l1_ratio=0               yes
 |         'newton-cholesky' l1_ratio=0               yes
 |         'sag'             l1_ratio=0               yes
 |         'saga'            0<=l1_ratio<=1           yes
 |         ================= ======================== ======================
 |
 |      .. note::
 |         'sag' and 'saga' fast convergence is only guaranteed on features
 |         with approximately the same scale. You can preprocess the data with
 |         a scaler from :mod:`sklearn.preprocessing`.
 |
 |      .. seealso::
 |         Refer to the :ref:`User Guide <Logistic_regression>` for more
 |         information regarding :class:`LogisticRegression` and more specifically the
 |         :ref:`Table <logistic_regression_solvers>`
 |         summarizing solver/penalty supports.
 |
 |      .. versionadded:: 0.17
 |         Stochastic Average Gradient (SAG) descent solver. Multinomial support in
 |         version 0.18.
 |      .. versionadded:: 0.19
 |         SAGA solver.
 |      .. versionchanged:: 0.22
 |         The default solver changed from 'liblinear' to 'lbfgs' in 0.22.
 |      .. versionadded:: 1.2
 |         newton-cholesky solver. Multinomial support in version 1.6.
 |
 |  max_iter : int, default=100
 |      Maximum number of iterations taken for the solvers to converge.
 |
 |  verbose : int, default=0
 |      For the liblinear and lbfgs solvers set verbose to any positive
 |      number for verbosity.
 |
 |  warm_start : bool, default=False
 |      When set to True, reuse the solution of the previous call to fit as
 |      initialization, otherwise, just erase the previous solution.
 |      Useless for liblinear solver. See :term:`the Glossary <warm_start>`.
 |
 |      .. versionadded:: 0.17
 |         *warm_start* to support *lbfgs*, *newton-cg*, *sag*, *saga* solvers.
 |
 |  n_jobs : int, default=None
 |      Does not have any effect.
 |
 |      .. deprecated:: 1.8
 |         `n_jobs` is deprecated in version 1.8 and will be removed in 1.10.
 |
 |  Attributes
 |  ----------
 |
 |  classes_ : ndarray of shape (n_classes, )
 |      A list of class labels known to the classifier.
 |
 |  coef_ : ndarray or CSR matrix of shape (1, n_features) or (n_classes, n_features)
 |      Coefficients of the features in the decision function.
 |
 |      `coef_` is of shape (1, n_features) when the given problem is binary.
 |
 |      By default, it will be created as a dense array, but can be turned to
 |      sparse (CSR format) through :meth:`sparsify` (which can be beneficial
 |      under L1 regularization when many coefficients are zero), and back to
 |      dense through :meth:`densify`.
 |
 |  intercept_ : ndarray of shape (1,) or (n_classes,)
 |      Intercept (a.k.a. bias) added to the decision function.
 |
 |      If `fit_intercept` is set to False, the intercept is set to zero.
 |      `intercept_` is of shape (1,) when the given problem is binary.
 |
 |  n_features_in_ : int
 |      Number of features seen during :term:`fit`.
 |
 |      .. versionadded:: 0.24
 |
 |  feature_names_in_ : ndarray of shape (`n_features_in_`,)
 |      Names of features seen during :term:`fit`. Defined only when `X`
 |      has feature names that are all strings.
 |
 |      .. versionadded:: 1.0
 |
 |  n_iter_ : ndarray of shape (1, )
 |      Actual number of iterations for all classes.
 |
 |      .. versionchanged:: 0.20
 |
 |          In SciPy <= 1.0.0 the number of lbfgs iterations may exceed
 |          ``max_iter``. ``n_iter_`` will now report at most ``max_iter``.
 |
 |  See Also
 |  --------
 |  SGDClassifier : Incrementally trained logistic regression (when given
 |      the parameter ``loss="log_loss"``).
 |  LogisticRegressionCV : Logistic regression with built-in cross validation.
 |
 |  Notes
 |  -----
 |  For several reasons (floating point arithmetic, random number generators, etc.)
 |  the coefficients of a fitted model might differ slightly (among machines,
 |  scikit-learn versions, etc.) for the same input data. If that happens and you
 |  want to avoid it, you can try with a smaller `tol` parameter.
 |
 |  Predict output may not match that of standalone liblinear in certain
 |  cases. See :ref:`differences from liblinear <liblinear_differences>`
 |  in the narrative documentation.
 |
 |  Examples
 |  --------
 |  >>> from sklearn.datasets import load_iris
 |  >>> from sklearn.linear_model import LogisticRegression
 |  >>> X, y = load_iris(return_X_y=True)
 |  >>> clf = LogisticRegression(random_state=0).fit(X, y)
 |  >>> clf.predict(X[:2, :])
 |  array([0, 0])
 |  >>> clf.predict_proba(X[:2, :])
 |  array([[9.82e-01, 1.82e-02, 1.44e-08],
 |         [9.72e-01, 2.82e-02, 3.02e-08]])
 |  >>> clf.score(X, y)
 |  0.97
 |
 |  For a comparison of the LogisticRegression with other classifiers see:
 |  :ref:`sphx_glr_auto_examples_classification_plot_classification_probability.py`.
 |
 |  Method resolution order:
 |      LogisticRegression
 |      sklearn.callback._callback_support.CallbackSupportMixin
 |      sklearn.linear_model._base.LinearClassifierMixin
 |      sklearn.base.ClassifierMixin
 |      sklearn.linear_model._base.SparseCoefMixin
 |      sklearn.base.BaseEstimator
 |      sklearn.utils._repr_html.base.ReprHTMLMixin
 |      sklearn.utils._repr_html.base._HTMLDocumentationLinkMixin
 |      sklearn.utils._metadata_requests._MetadataRequester
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, penalty='deprecated', *, C=1.0, l1_ratio=0.0, dual=False, tol=0.0001, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, verbose=0, warm_start=False, n_jobs=None)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __sklearn_tags__(self)
 |
 |  fit(self, X, y, sample_weight=None)
 |      Fit the model according to the given training data.
 |
 |      Parameters
 |      ----------
 |      X : {array-like, sparse matrix} of shape (n_samples, n_features)
 |          Training vector, where `n_samples` is the number of samples and
 |          `n_features` is the number of features.
 |
 |      y : array-like of shape (n_samples,)
 |          Target vector relative to X.
 |
 |      sample_weight : array-like of shape (n_samples,) default=None
 |          Array of weights that are assigned to individual samples.
 |          If not provided, then each sample is given unit weight.
 |
 |          .. versionadded:: 0.17
 |             *sample_weight* support to LogisticRegression.
 |
 |      Returns
 |      -------
 |      self
 |          Fitted estimator.
 |
 |      Notes
 |      -----
 |      The SAGA solver supports both float64 and float32 bit arrays.
 |
 |  predict_log_proba(self, X)
 |      Predict logarithm of probability estimates.
 |
 |      The returned estimates for all classes are ordered by the
 |      label of classes.
 |
 |      Parameters
 |      ----------
 |      X : array-like of shape (n_samples, n_features)
 |          Vector to be scored, where `n_samples` is the number of samples and
 |          `n_features` is the number of features.
 |
 |      Returns
 |      -------
 |      T : array-like of shape (n_samples, n_classes)
 |          Returns the log-probability of the sample for each class in the
 |          model, where classes are ordered as they are in ``self.classes_``.
 |
 |  predict_proba(self, X)
 |      Probability estimates.
 |
 |      The returned estimates for all classes are ordered by the
 |      label of classes.
 |
 |      For a multiclass / multinomial problem the softmax function is used to find
 |      the predicted probability of each class.
 |
 |      Parameters
 |      ----------
 |      X : array-like of shape (n_samples, n_features)
 |          Vector to be scored, where `n_samples` is the number of samples and
 |          `n_features` is the number of features.
 |
 |      Returns
 |      -------
 |      T : array-like of shape (n_samples, n_classes)
 |          Returns the probability of the sample for each class in the model,
 |          where classes are ordered as they are in ``self.classes_``.
 |
 |  set_callbacks(self, *callbacks)
 |      Set callbacks for the estimator.
 |
 |      Parameters
 |      ----------
 |      *callbacks : callback instances
 |          The callbacks to set.
 |
 |      Returns
 |      -------
 |      self : estimator instance
 |          The estimator instance itself.
 |
 |  set_fit_request(self: sklearn.linear_model._logistic.LogisticRegression, *, sample_weight: Union[bool, NoneType, str] = '$UNCHANGED$') -> sklearn.linear_model._logistic.LogisticRegression
 |      Configure whether metadata should be requested to be passed to the ``fit`` method.
 |
 |      Note that this method is only relevant when this estimator is used as a
 |      sub-estimator within a :term:`meta-estimator` and metadata routing is enabled
 |      with ``enable_metadata_routing=True`` (see :func:`sklearn.set_config`).
 |      Please check the :ref:`User Guide <metadata_routing>` on how the routing
 |      mechanism works.
 |
 |      The options for each parameter are:
 |
 |      - ``True``: metadata is requested, and passed to ``fit`` if provided. The request is ignored if metadata is not provided.
 |
 |      - ``False``: metadata is not requested and the meta-estimator will not pass it to ``fit``.
 |
 |      - ``None``: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
 |
 |      - ``str``: metadata should be passed to the meta-estimator with this given alias instead of the original name.
 |
 |      The default (``sklearn.utils.metadata_routing.UNCHANGED``) retains the
 |      existing request. This allows you to change the request for some
 |      parameters and not others.
 |
 |      .. versionadded:: 1.3
 |
 |      Parameters
 |      ----------
 |      sample_weight : str, True, False, or None,                     default=sklearn.utils.metadata_routing.UNCHANGED
 |          Metadata routing for ``sample_weight`` parameter in ``fit``.
 |
 |      Returns
 |      -------
 |      self : object
 |          The updated object.
 |
 |  set_score_request(self: sklearn.linear_model._logistic.LogisticRegression, *, sample_weight: Union[bool, NoneType, str] = '$UNCHANGED$') -> sklearn.linear_model._logistic.LogisticRegression
 |      Configure whether metadata should be requested to be passed to the ``score`` method.
 |
 |      Note that this method is only relevant when this estimator is used as a
 |      sub-estimator within a :term:`meta-estimator` and metadata routing is enabled
 |      with ``enable_metadata_routing=True`` (see :func:`sklearn.set_config`).
 |      Please check the :ref:`User Guide <metadata_routing>` on how the routing
 |      mechanism works.
 |
 |      The options for each parameter are:
 |
 |      - ``True``: metadata is requested, and passed to ``score`` if provided. The request is ignored if metadata is not provided.
 |
 |      - ``False``: metadata is not requested and the meta-estimator will not pass it to ``score``.
 |
 |      - ``None``: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
 |
 |      - ``str``: metadata should be passed to the meta-estimator with this given alias instead of the original name.
 |
 |      The default (``sklearn.utils.metadata_routing.UNCHANGED``) retains the
 |      existing request. This allows you to change the request for some
 |      parameters and not others.
 |
 |      .. versionadded:: 1.3
 |
 |      Parameters
 |      ----------
 |      sample_weight : str, True, False, or None,                     default=sklearn.utils.metadata_routing.UNCHANGED
 |          Metadata routing for ``sample_weight`` parameter in ``score``.
 |
 |      Returns
 |      -------
 |      self : object
 |          The updated object.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __annotations__ = {'_parameter_constraints': <class 'dict'>}
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from sklearn.callback._callback_support.CallbackSupportMixin:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.linear_model._base.LinearClassifierMixin:
 |
 |  decision_function(self, X)
 |      Predict confidence scores for samples.
 |
 |      The confidence score for a sample is proportional to the signed
 |      distance of that sample to the hyperplane.
 |
 |      Parameters
 |      ----------
 |      X : {array-like, sparse matrix} of shape (n_samples, n_features)
 |          The data matrix for which we want to get the confidence scores.
 |
 |      Returns
 |      -------
 |      scores : ndarray of shape (n_samples,) or (n_samples, n_classes)
 |          Confidence scores per `(n_samples, n_classes)` combination. In the
 |          binary case, confidence score for `self.classes_[1]` where >0 means
 |          this class would be predicted.
 |
 |  predict(self, X)
 |      Predict class labels for samples in X.
 |
 |      Parameters
 |      ----------
 |      X : {array-like, sparse matrix} of shape (n_samples, n_features)
 |          The data matrix for which we want to get the predictions.
 |
 |      Returns
 |      -------
 |      y_pred : ndarray of shape (n_samples,)
 |          Vector containing the class labels for each sample.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.base.ClassifierMixin:
 |
 |  score(self, X, y, sample_weight=None)
 |      Return :ref:`accuracy <accuracy_score>` on provided data and labels.
 |
 |      In multi-label classification, this is the subset accuracy
 |      which is a harsh metric since you require for each sample that
 |      each label set be correctly predicted.
 |
 |      Parameters
 |      ----------
 |      X : array-like of shape (n_samples, n_features)
 |          Test samples.
 |
 |      y : array-like of shape (n_samples,) or (n_samples, n_outputs)
 |          True labels for `X`.
 |
 |      sample_weight : array-like of shape (n_samples,), default=None
 |          Sample weights.
 |
 |      Returns
 |      -------
 |      score : float
 |          Mean accuracy of ``self.predict(X)`` w.r.t. `y`.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.linear_model._base.SparseCoefMixin:
 |
 |  densify(self)
 |      Convert coefficient matrix to dense array format.
 |
 |      Converts the ``coef_`` member (back) to a numpy.ndarray. This is the
 |      default format of ``coef_`` and is required for fitting, so calling
 |      this method is only required on models that have previously been
 |      sparsified; otherwise, it is a no-op.
 |
 |      Returns
 |      -------
 |      self
 |          Fitted estimator.
 |
 |  sparsify(self)
 |      Convert coefficient matrix to sparse format.
 |
 |      Converts the ``coef_`` member to a scipy.sparse matrix, which for
 |      L1-regularized models can be much more memory- and storage-efficient
 |      than the usual numpy.ndarray representation.
 |
 |      The ``intercept_`` member is not converted.
 |
 |      .. warning::
 |          This method is not supported for estimators fitted with array API
 |          inputs (i.e. when :func:`sklearn.config_context` is used with
 |          ``array_api_dispatch=True``). The call may succeed but subsequent
 |          calls to :meth:`predict` and other methods involving passing arrays
 |          may raise or return unexpected results.
 |
 |      Returns
 |      -------
 |      self
 |          Fitted estimator.
 |
 |      Notes
 |      -----
 |      For non-sparse models, i.e. when there are not many zeros in ``coef_``,
 |      this may actually *increase* memory usage, so use this method with
 |      care. A rule of thumb is that the number of zero elements, which can
 |      be computed with ``(coef_ == 0).sum()``, must be more than 50% for this
 |      to provide significant benefits.
 |
 |      After calling this method, further fitting with the partial_fit
 |      method (if any) will not work until you call densify.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.base.BaseEstimator:
 |
 |  __dir__(self)
 |      Default dir() implementation.
 |
 |  __getstate__(self)
 |      Helper for pickle.
 |
 |  __repr__(self, N_CHAR_MAX=700)
 |      Return repr(self).
 |
 |  __setstate__(self, state)
 |
 |  __sklearn_clone__(self)
 |
 |  get_params(self, deep=True)
 |      Get parameters for this estimator.
 |
 |      Parameters
 |      ----------
 |      deep : bool, default=True
 |          If True, will return the parameters for this estimator and
 |          contained subobjects that are estimators.
 |
 |      Returns
 |      -------
 |      params : dict
 |          Parameter names mapped to their values.
 |
 |  set_params(self, **params)
 |      Set the parameters of this estimator.
 |
 |      The method works on simple estimators as well as on nested objects
 |      (such as :class:`~sklearn.pipeline.Pipeline`). The latter have
 |      parameters of the form ``<component>__<parameter>`` so that it's
 |      possible to update each component of a nested object.
 |
 |      Parameters
 |      ----------
 |      **params : dict
 |          Estimator parameters.
 |
 |      Returns
 |      -------
 |      self : estimator instance
 |          Estimator instance.
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
 |  __init_subclass__(**kwargs) from builtins.type
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

## StandardScaler

### Signature
```
(*, copy=True, with_mean=True, with_std=True)
```

### help()
```
Python Library Documentation: class StandardScaler in module sklearn.preprocessing._data

class StandardScaler(sklearn.callback._callback_support.CallbackSupportMixin, sklearn.base.OneToOneFeatureMixin, sklearn.base.TransformerMixin, sklearn.base.BaseEstimator)
 |  StandardScaler(*, copy=True, with_mean=True, with_std=True)
 |
 |  Standardize features by removing the mean and scaling to unit variance.
 |
 |  The standard score of a sample `x` is calculated as:
 |
 |  .. code-block:: text
 |
 |      z = (x - u) / s
 |
 |  where `u` is the mean of the training samples or zero if `with_mean=False`,
 |  and `s` is the standard deviation of the training samples or one if
 |  `with_std=False`.
 |
 |  Centering and scaling happen independently on each feature by computing
 |  the relevant statistics on the samples in the training set. Mean and
 |  standard deviation are then stored to be used on later data using
 |  :meth:`transform`.
 |
 |  Standardization of a dataset is a common requirement for many
 |  machine learning estimators: they might behave badly if the
 |  individual features do not more or less look like standard normally
 |  distributed data (e.g. Gaussian with 0 mean and unit variance).
 |
 |  For instance many elements used in the objective function of
 |  a learning algorithm (such as the RBF kernel of Support Vector
 |  Machines or the L1 and L2 regularizers of linear models) assume that
 |  all features are centered around 0 and have variance in the same
 |  order. If a feature has a variance that is orders of magnitude larger
 |  than others, it might dominate the objective function and make the
 |  estimator unable to learn from other features correctly as expected.
 |
 |  `StandardScaler` is sensitive to outliers, and the features may scale
 |  differently from each other in the presence of outliers. For an example
 |  visualization, refer to :ref:`Compare StandardScaler with other scalers
 |  <plot_all_scaling_standard_scaler_section>`.
 |
 |  This scaler can also be applied to sparse CSR or CSC matrices by passing
 |  `with_mean=False` to avoid breaking the sparsity structure of the data.
 |
 |  Read more in the :ref:`User Guide <preprocessing_scaler>`.
 |
 |  Parameters
 |  ----------
 |  copy : bool, default=True
 |      If False, try to avoid a copy and do inplace scaling instead.
 |      This is not guaranteed to always work inplace; e.g. if the data is
 |      not a NumPy array or scipy.sparse CSR matrix, a copy may still be
 |      returned.
 |
 |  with_mean : bool, default=True
 |      If True, center the data before scaling.
 |      This does not work (and will raise an exception) when attempted on
 |      sparse matrices, because centering them entails building a dense
 |      matrix which in common use cases is likely to be too large to fit in
 |      memory.
 |
 |  with_std : bool, default=True
 |      If True, scale the data to unit variance (or equivalently,
 |      unit standard deviation).
 |
 |  Attributes
 |  ----------
 |  scale_ : ndarray of shape (n_features,) or None
 |      Per feature relative scaling of the data to achieve zero mean and unit
 |      variance. Generally this is calculated using `np.sqrt(var_)`. If a
 |      variance is zero, we can't achieve unit variance, and the data is left
 |      as-is, giving a scaling factor of 1. `scale_` is equal to `None`
 |      when `with_std=False`.
 |
 |      .. versionadded:: 0.17
 |         *scale_*
 |
 |  mean_ : ndarray of shape (n_features,) or None
 |      The mean value for each feature in the training set.
 |      Equal to ``None`` when ``with_mean=False`` and ``with_std=False``.
 |
 |  var_ : ndarray of shape (n_features,) or None
 |      The variance for each feature in the training set. Used to compute
 |      `scale_`. Equal to ``None`` when ``with_mean=False`` and
 |      ``with_std=False``.
 |
 |  n_features_in_ : int
 |      Number of features seen during :term:`fit`.
 |
 |      .. versionadded:: 0.24
 |
 |  feature_names_in_ : ndarray of shape (`n_features_in_`,)
 |      Names of features seen during :term:`fit`. Defined only when `X`
 |      has feature names that are all strings.
 |
 |      .. versionadded:: 1.0
 |
 |  n_samples_seen_ : int or ndarray of shape (n_features,)
 |      The number of samples processed by the estimator for each feature.
 |      If there are no missing samples, the ``n_samples_seen`` will be an
 |      integer, otherwise it will be an array of dtype int. If
 |      `sample_weights` are used it will be a float (if no missing data)
 |      or an array of dtype float that sums the weights seen so far.
 |      Will be reset on new calls to fit, but increments across
 |      ``partial_fit`` calls.
 |
 |  See Also
 |  --------
 |  scale : Equivalent function without the estimator API.
 |
 |  :class:`~sklearn.decomposition.PCA` : Further removes the linear
 |      correlation across features with 'whiten=True'.
 |
 |  Notes
 |  -----
 |  NaNs are treated as missing values: disregarded in fit, and maintained in
 |  transform.
 |
 |  We use a biased estimator for the standard deviation, equivalent to
 |  `numpy.std(x, ddof=0)`. Note that the choice of `ddof` is unlikely to
 |  affect model performance.
 |
 |  Examples
 |  --------
 |  >>> from sklearn.preprocessing import StandardScaler
 |  >>> data = [[0, 0], [0, 0], [1, 1], [1, 1]]
 |  >>> scaler = StandardScaler()
 |  >>> print(scaler.fit(data))
 |  StandardScaler()
 |  >>> print(scaler.mean_)
 |  [0.5 0.5]
 |  >>> print(scaler.transform(data))
 |  [[-1. -1.]
 |   [-1. -1.]
 |   [ 1.  1.]
 |   [ 1.  1.]]
 |  >>> print(scaler.transform([[2, 2]]))
 |  [[3. 3.]]
 |
 |  Method resolution order:
 |      StandardScaler
 |      sklearn.callback._callback_support.CallbackSupportMixin
 |      sklearn.base.OneToOneFeatureMixin
 |      sklearn.base.TransformerMixin
 |      sklearn.utils._set_output._SetOutputMixin
 |      sklearn.base.BaseEstimator
 |      sklearn.utils._repr_html.base.ReprHTMLMixin
 |      sklearn.utils._repr_html.base._HTMLDocumentationLinkMixin
 |      sklearn.utils._metadata_requests._MetadataRequester
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, *, copy=True, with_mean=True, with_std=True)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __sklearn_tags__(self)
 |
 |  fit(self, X, y=None, sample_weight=None)
 |      Compute the mean and std to be used for later scaling.
 |
 |      Parameters
 |      ----------
 |      X : {array-like, sparse matrix} of shape (n_samples, n_features)
 |          The data used to compute the mean and standard deviation
 |          used for later scaling along the features axis.
 |
 |      y : None
 |          Ignored.
 |
 |      sample_weight : array-like of shape (n_samples,), default=None
 |          Individual weights for each sample.
 |
 |          .. versionadded:: 0.24
 |             parameter *sample_weight* support to StandardScaler.
 |
 |      Returns
 |      -------
 |      self : object
 |          Fitted scaler.
 |
 |  inverse_transform(self, X, copy=None)
 |      Scale back the data to the original representation.
 |
 |      Parameters
 |      ----------
 |      X : {array-like, sparse matrix} of shape (n_samples, n_features)
 |          The data used to scale along the features axis.
 |
 |      copy : bool, default=None
 |          Copy the input `X` or not.
 |
 |      Returns
 |      -------
 |      X_original : {ndarray, sparse matrix} of shape (n_samples, n_features)
 |          Transformed array.
 |
 |  partial_fit(self, X, y=None, sample_weight=None)
 |      Online computation of mean and std on X for later scaling.
 |
 |      All of X is processed as a single batch. This is intended for cases
 |      when :meth:`fit` is not feasible due to very large number of
 |      `n_samples` or because X is read from a continuous stream.
 |
 |      The algorithm for incremental mean and std is given in Equation 1.5a,b
 |      in Chan, Tony F., Gene H. Golub, and Randall J. LeVeque. "Algorithms
 |      for computing the sample variance: Analysis and recommendations."
 |      The American Statistician 37.3 (1983): 242-247:
 |
 |      Parameters
 |      ----------
 |      X : {array-like, sparse matrix} of shape (n_samples, n_features)
 |          The data used to compute the mean and standard deviation
 |          used for later scaling along the features axis.
 |
 |      y : None
 |          Ignored.
 |
 |      sample_weight : array-like of shape (n_samples,), default=None
 |          Individual weights for each sample.
 |
 |          .. versionadded:: 0.24
 |             parameter *sample_weight* support to StandardScaler.
 |
 |      Returns
 |      -------
 |      self : object
 |          Fitted scaler.
 |
 |  set_fit_request(self: sklearn.preprocessing._data.StandardScaler, *, sample_weight: Union[bool, NoneType, str] = '$UNCHANGED$') -> sklearn.preprocessing._data.StandardScaler
 |      Configure whether metadata should be requested to be passed to the ``fit`` method.
 |
 |      Note that this method is only relevant when this estimator is used as a
 |      sub-estimator within a :term:`meta-estimator` and metadata routing is enabled
 |      with ``enable_metadata_routing=True`` (see :func:`sklearn.set_config`).
 |      Please check the :ref:`User Guide <metadata_routing>` on how the routing
 |      mechanism works.
 |
 |      The options for each parameter are:
 |
 |      - ``True``: metadata is requested, and passed to ``fit`` if provided. The request is ignored if metadata is not provided.
 |
 |      - ``False``: metadata is not requested and the meta-estimator will not pass it to ``fit``.
 |
 |      - ``None``: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
 |
 |      - ``str``: metadata should be passed to the meta-estimator with this given alias instead of the original name.
 |
 |      The default (``sklearn.utils.metadata_routing.UNCHANGED``) retains the
 |      existing request. This allows you to change the request for some
 |      parameters and not others.
 |
 |      .. versionadded:: 1.3
 |
 |      Parameters
 |      ----------
 |      sample_weight : str, True, False, or None,                     default=sklearn.utils.metadata_routing.UNCHANGED
 |          Metadata routing for ``sample_weight`` parameter in ``fit``.
 |
 |      Returns
 |      -------
 |      self : object
 |          The updated object.
 |
 |  set_inverse_transform_request(self: sklearn.preprocessing._data.StandardScaler, *, copy: Union[bool, NoneType, str] = '$UNCHANGED$') -> sklearn.preprocessing._data.StandardScaler
 |      Configure whether metadata should be requested to be passed to the ``inverse_transform`` method.
 |
 |      Note that this method is only relevant when this estimator is used as a
 |      sub-estimator within a :term:`meta-estimator` and metadata routing is enabled
 |      with ``enable_metadata_routing=True`` (see :func:`sklearn.set_config`).
 |      Please check the :ref:`User Guide <metadata_routing>` on how the routing
 |      mechanism works.
 |
 |      The options for each parameter are:
 |
 |      - ``True``: metadata is requested, and passed to ``inverse_transform`` if provided. The request is ignored if metadata is not provided.
 |
 |      - ``False``: metadata is not requested and the meta-estimator will not pass it to ``inverse_transform``.
 |
 |      - ``None``: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
 |
 |      - ``str``: metadata should be passed to the meta-estimator with this given alias instead of the original name.
 |
 |      The default (``sklearn.utils.metadata_routing.UNCHANGED``) retains the
 |      existing request. This allows you to change the request for some
 |      parameters and not others.
 |
 |      .. versionadded:: 1.3
 |
 |      Parameters
 |      ----------
 |      copy : str, True, False, or None,                     default=sklearn.utils.metadata_routing.UNCHANGED
 |          Metadata routing for ``copy`` parameter in ``inverse_transform``.
 |
 |      Returns
 |      -------
 |      self : object
 |          The updated object.
 |
 |  set_partial_fit_request(self: sklearn.preprocessing._data.StandardScaler, *, sample_weight: Union[bool, NoneType, str] = '$UNCHANGED$') -> sklearn.preprocessing._data.StandardScaler
 |      Configure whether metadata should be requested to be passed to the ``partial_fit`` method.
 |
 |      Note that this method is only relevant when this estimator is used as a
 |      sub-estimator within a :term:`meta-estimator` and metadata routing is enabled
 |      with ``enable_metadata_routing=True`` (see :func:`sklearn.set_config`).
 |      Please check the :ref:`User Guide <metadata_routing>` on how the routing
 |      mechanism works.
 |
 |      The options for each parameter are:
 |
 |      - ``True``: metadata is requested, and passed to ``partial_fit`` if provided. The request is ignored if metadata is not provided.
 |
 |      - ``False``: metadata is not requested and the meta-estimator will not pass it to ``partial_fit``.
 |
 |      - ``None``: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
 |
 |      - ``str``: metadata should be passed to the meta-estimator with this given alias instead of the original name.
 |
 |      The default (``sklearn.utils.metadata_routing.UNCHANGED``) retains the
 |      existing request. This allows you to change the request for some
 |      parameters and not others.
 |
 |      .. versionadded:: 1.3
 |
 |      Parameters
 |      ----------
 |      sample_weight : str, True, False, or None,                     default=sklearn.utils.metadata_routing.UNCHANGED
 |          Metadata routing for ``sample_weight`` parameter in ``partial_fit``.
 |
 |      Returns
 |      -------
 |      self : object
 |          The updated object.
 |
 |  set_transform_request(self: sklearn.preprocessing._data.StandardScaler, *, copy: Union[bool, NoneType, str] = '$UNCHANGED$') -> sklearn.preprocessing._data.StandardScaler
 |      Configure whether metadata should be requested to be passed to the ``transform`` method.
 |
 |      Note that this method is only relevant when this estimator is used as a
 |      sub-estimator within a :term:`meta-estimator` and metadata routing is enabled
 |      with ``enable_metadata_routing=True`` (see :func:`sklearn.set_config`).
 |      Please check the :ref:`User Guide <metadata_routing>` on how the routing
 |      mechanism works.
 |
 |      The options for each parameter are:
 |
 |      - ``True``: metadata is requested, and passed to ``transform`` if provided. The request is ignored if metadata is not provided.
 |
 |      - ``False``: metadata is not requested and the meta-estimator will not pass it to ``transform``.
 |
 |      - ``None``: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
 |
 |      - ``str``: metadata should be passed to the meta-estimator with this given alias instead of the original name.
 |
 |      The default (``sklearn.utils.metadata_routing.UNCHANGED``) retains the
 |      existing request. This allows you to change the request for some
 |      parameters and not others.
 |
 |      .. versionadded:: 1.3
 |
 |      Parameters
 |      ----------
 |      copy : str, True, False, or None,                     default=sklearn.utils.metadata_routing.UNCHANGED
 |          Metadata routing for ``copy`` parameter in ``transform``.
 |
 |      Returns
 |      -------
 |      self : object
 |          The updated object.
 |
 |  transform(self, X, copy=None)
 |      Perform standardization by centering and scaling.
 |
 |      Parameters
 |      ----------
 |      X : {array-like, sparse matrix of shape (n_samples, n_features)
 |          The data used to scale along the features axis.
 |      copy : bool, default=None
 |          Copy the input X or not.
 |
 |      Returns
 |      -------
 |      X_tr : {ndarray, sparse matrix} of shape (n_samples, n_features)
 |          Transformed array.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __annotations__ = {'_parameter_constraints': <class 'dict'>}
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.callback._callback_support.CallbackSupportMixin:
 |
 |  set_callbacks(self, *callbacks)
 |      Set callbacks for the estimator.
 |
 |      Parameters
 |      ----------
 |      *callbacks : callback instances
 |          The callbacks to set.
 |
 |      Returns
 |      -------
 |      self : estimator instance
 |          The estimator instance itself.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from sklearn.callback._callback_support.CallbackSupportMixin:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.base.OneToOneFeatureMixin:
 |
 |  get_feature_names_out(self, input_features=None)
 |      Get output feature names for transformation.
 |
 |      Parameters
 |      ----------
 |      input_features : array-like of str or None, default=None
 |          Input features.
 |
 |          - If `input_features` is `None`, then `feature_names_in_` is
 |            used as feature names in. If `feature_names_in_` is not defined,
 |            then the following input feature names are generated:
 |            `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
 |          - If `input_features` is an array-like, then `input_features` must
 |            match `feature_names_in_` if `feature_names_in_` is defined.
 |
 |      Returns
 |      -------
 |      feature_names_out : ndarray of str objects
 |          Same as input features.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.base.TransformerMixin:
 |
 |  fit_transform(self, X, y=None, **fit_params)
 |      Fit to data, then transform it.
 |
 |      Fits transformer to `X` and `y` with optional parameters `fit_params`
 |      and returns a transformed version of `X`.
 |
 |      Parameters
 |      ----------
 |      X : array-like of shape (n_samples, n_features)
 |          Input samples.
 |
 |      y :  array-like of shape (n_samples,) or (n_samples, n_outputs),                 default=None
 |          Target values (None for unsupervised transformations).
 |
 |      **fit_params : dict
 |          Additional fit parameters.
 |          Pass only if the estimator accepts additional params in its `fit` method.
 |
 |      Returns
 |      -------
 |      X_new : ndarray array of shape (n_samples, n_features_new)
 |          Transformed array.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.utils._set_output._SetOutputMixin:
 |
 |  set_output(self, *, transform=None)
 |      Set output container.
 |
 |      Refer to the :ref:`user guide <df_output_transform>` for more details
 |      and :ref:`sphx_glr_auto_examples_miscellaneous_plot_set_output.py` for an
 |      example on how to use the API.
 |
 |      Parameters
 |      ----------
 |      transform : {"default", "pandas", "polars"}, default=None
 |          Configure output of `transform` and `fit_transform`.
 |
 |          - `"default"`: Default output format of a transformer
 |          - `"pandas"`: DataFrame output
 |          - `"polars"`: Polars output
 |          - `None`: Transform configuration is unchanged
 |
 |          .. versionadded:: 1.4
 |              `"polars"` option was added.
 |
 |      Returns
 |      -------
 |      self : estimator instance
 |          Estimator instance.
 |
 |  ----------------------------------------------------------------------
 |  Class methods inherited from sklearn.utils._set_output._SetOutputMixin:
 |
 |  __init_subclass__(auto_wrap_output_keys=('transform',), **kwargs) from builtins.type
 |      This method is called when a class is subclassed.
 |
 |      The default implementation does nothing. It may be
 |      overridden to extend subclasses.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from sklearn.base.BaseEstimator:
 |
 |  __dir__(self)
 |      Default dir() implementation.
 |
 |  __getstate__(self)
 |      Helper for pickle.
 |
 |  __repr__(self, N_CHAR_MAX=700)
 |      Return repr(self).
 |
 |  __setstate__(self, state)
 |
 |  __sklearn_clone__(self)
 |
 |  get_params(self, deep=True)
 |      Get parameters for this estimator.
 |
 |      Parameters
 |      ----------
 |      deep : bool, default=True
 |          If True, will return the parameters for this estimator and
 |          contained subobjects that are estimators.
 |
 |      Returns
 |      -------
 |      params : dict
 |          Parameter names mapped to their values.
 |
 |  set_params(self, **params)
 |      Set the parameters of this estimator.
 |
 |      The method works on simple estimators as well as on nested objects
 |      (such as :class:`~sklearn.pipeline.Pipeline`). The latter have
 |      parameters of the form ``<component>__<parameter>`` so that it's
 |      possible to update each component of a nested object.
 |
 |      Parameters
 |      ----------
 |      **params : dict
 |          Estimator parameters.
 |
 |      Returns
 |      -------
 |      self : estimator instance
 |          Estimator instance.
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

```
