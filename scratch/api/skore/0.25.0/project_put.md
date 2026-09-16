# skore Project: init, put, summarize, get

Source: inspect: skore @ 0.25.0
Probed: 2025-09-15

## Project

### Signature
```
(name: 'str', *, mode: 'ProjectMode' = 'local', **kwargs)
```

### help()
```
Python Library Documentation: class Project in module skore._project.project

class Project(builtins.object)
 |  Project(name: 'str', *, mode: 'ProjectMode' = 'local', **kwargs)
 |
 |  API to manage a collection of key-report pairs.
 |
 |  Its constructor initializes a project by creating a new project or by loading an
 |  existing one.
 |
 |  The class main methods are :func:`~skore.Project.put`,
 |  :func:`~skore.Project.summarize`, :func:`~skore.Project.get`, and
 |  :func:`~skore.Project.sync`, respectively to insert a key-report pair into the
 |  project, obtain the metadata/metrics of the inserted reports, get a specific report
 |  by its id, and synchronize reports between projects.
 |
 |  Three mutually exclusive modes are available and can be configured using the
 |  ``mode`` parameter of the constructor:
 |
 |  .. rubric:: Hub mode
 |
 |  The project is configured to communicate with ``skore hub``.
 |
 |  In this mode, ``workspace`` is a ``skore hub`` concept that must be configured on
 |  the ``skore hub`` interface. It represents an isolated entity managing users,
 |  projects, and resources. It can be a company, organization, or team that operates
 |  independently within the system.
 |
 |  Note: Using Project in ``hub`` mode requires an account on ``skore hub``, with
 |  access rights to the specified workspace. Authentication to ``skore hub`` is done by
 |  running ``skore.login()`` before instantiating the Project.
 |
 |  .. rubric:: Local mode
 |
 |  Otherwise, the project is configured to the ``local`` mode to be persisted on
 |  the user machine in a directory called a ``workspace``.
 |
 |  | The workspace can be set using kwargs or the environment variable
 |    ``SKORE_WORKSPACE``.
 |  | If not, it will be set to a default location:
 |
 |      - we search the current working directory and its parents for a
 |        skore workspace: a directory named 'skore' containing a file named
 |        '.SKORE_WORKSPACE'. If found, use that.
 |      - otherwise if we are in a Git repository, create 'skore' at the root
 |          of the repository.
 |      - otherwise create 'skore' in the current working directory.
 |
 |  .. rubric:: MLflow mode
 |
 |  In this mode, ``name`` is used as the MLflow experiment name. Reports are persisted
 |  as MLflow model artifacts in runs created under this experiment.
 |
 |  Refer to the :ref:`project` section of the user guide for more details.
 |
 |  Parameters
 |  ----------
 |  name : str
 |      The name of the project.
 |  mode : {"hub", "local", "mlflow"}
 |      The mode of the project.
 |  **kwargs : dict
 |      Extra keyword arguments passed to the project, depending on its mode.
 |
 |      workspace : str or Path-like, optional
 |
 |          - If ``mode="hub"``, the Hub workspace name (required);
 |          - If ``mode="local"``, the local persistence directory (optional);
 |          - If ``mode="mlflow"``, ignored.
 |
 |      tracking_uri : str, mode:mlflow only.
 |          The URI of the MLflow tracking server.
 |
 |  Attributes
 |  ----------
 |  name : str
 |      The name of the project.
 |  mode : {"hub", "local", "mlflow"}
 |      The mode of the project.
 |  workspace : Path or str or None
 |      The workspace for ``local`` (``Path``) and ``hub`` (``str``) modes; ``None``
 |      otherwise.
 |  tracking_uri : str or None
 |      The MLflow tracking URI for ``mlflow`` mode; ``None`` otherwise.
 |  ml_task : MLTask
 |      The ML task of the project; unset until a first report is put.
 |
 |  Examples
 |  --------
 |  Construct reports.
 |
 |  >>> from sklearn.datasets import make_regression
 |  >>> from sklearn.linear_model import LinearRegression
 |  >>> from skore import evaluate
 |  >>>
 |  >>> X, y = make_regression(random_state=42)
 |  >>> regressor = LinearRegression()
 |  >>> regressor_report = evaluate(regressor, X, y, splitter=0.2)
 |
 |  Construct the project in local mode, persisted in a temporary directory.
 |
 |  >>> from pathlib import Path
 |  >>> from tempfile import TemporaryDirectory
 |  >>> from skore import Project
 |  >>>
 |  >>> tmpdir = TemporaryDirectory().name
 |  >>> local_project = Project(name="my-xp", mode="local", workspace=Path(tmpdir))
 |
 |  Put reports in the project.
 |
 |  >>> local_project.put("my-simple-regression", regressor_report)
 |
 |  Investigate metadata/metrics to filter the best reports.
 |
 |  >>> summary = local_project.summarize()
 |  >>> summary = summary.query("rmse < 67")
 |  >>> reports = summary.compare()
 |
 |  See Also
 |  --------
 |  :class:`~skore.Summary` :
 |      Tabular view of metadata and metrics for persisted reports.
 |  :func:`~skore.compare` :
 |      Compare reports side by side.
 |  :meth:`Project.summarize` :
 |      Create a summary view to investigate persisted reports' metadata/metrics.
 |
 |  Methods defined here:
 |
 |  __init__(self, name: 'str', *, mode: 'ProjectMode' = 'local', **kwargs)
 |      Initialize a project.
 |
 |      Parameters
 |      ----------
 |      name : str
 |          The name of the project.
 |          For mode:mlflow, this name will be used as the experiment name.
 |      mode : {"hub", "local", "mlflow"}, default "local"
 |          The mode of the project.
 |      **kwargs : dict
 |          Extra keyword arguments passed to the project, depending on its mode.
 |
 |          workspace : str or Path-like, optional
 |              Hub workspace name when ``mode="hub"`` (required). Local persistence
 |              directory when ``mode="local"`` (optional). Ignored when
 |              ``mode="mlflow"``.
 |
 |              For ``mode="local"``:
 |
 |              | The workspace can be shared between all the projects.
 |              | The workspace can be set using kwargs or the environment variable
 |                ``SKORE_WORKSPACE``.
 |              | If not provided, a workspace is found or created according to those
 |                rules (see find_workspace() in this module):
 |
 |                    - if the SKORE_WORKSPACE environment variable is set, use that.
 |                    - otherwise look in the current working directory and its
 |                      parent for a skore workspace: a directory named
 |                      'skore' containing a file named
 |                      '.SKORE_WORKSPACE'. If found, use that.
 |                    - otherwise if we are in a Git repository, create
 |                      'skore' at the root of the repository.
 |                    - otherwise create 'skore' in the current working directory.
 |
 |          tracking_uri : str, mode:mlflow only.
 |              The URI of the MLflow tracking server.
 |
 |      Examples
 |      --------
 |      >>> from pathlib import Path
 |      >>> from tempfile import TemporaryDirectory
 |      >>> from skore import Project
 |      >>> tmpdir = TemporaryDirectory()
 |      >>> project = Project(name="my-xp", mode="local", workspace=Path(tmpdir.name))
 |      >>> project.name
 |      'my-xp'
 |      >>> project.mode
 |      'local'
 |      >>> tmpdir.cleanup()
 |
 |  __repr__(self) -> 'str'
 |      Return repr(self).
 |
 |  get(self, id: 'str') -> 'EstimatorReport | CrossValidationReport'
 |      Get a persisted report by its id.
 |
 |      Report IDs can be found via :meth:`skore.Project.summarize`, which is also the
 |      preferred method of interacting with a ``skore.Project``. The ``id`` passed here
 |      must match the ``id`` column returned by :meth:`Project.summarize`.
 |
 |      Parameters
 |      ----------
 |      id : str
 |          The id of a report already put in the ``project``.
 |
 |      Returns
 |      -------
 |      report : EstimatorReport or CrossValidationReport
 |          The report associated with ``id``.
 |
 |      Examples
 |      --------
 |      >>> from sklearn.datasets import make_regression
 |      >>> from sklearn.linear_model import LinearRegression
 |      >>> from pathlib import Path
 |      >>> from tempfile import TemporaryDirectory
 |      >>> from skore import Project, evaluate
 |      >>> X, y = make_regression(random_state=42)
 |      >>> report = evaluate(LinearRegression(), X, y, splitter=0.2)
 |      >>> tmpdir = TemporaryDirectory()
 |      >>> project = Project(name="my-xp", mode="local", workspace=Path(tmpdir.name))
 |      >>> project.put("my-regression", report)
 |      >>> summary = project.summarize()
 |      >>> report_id = summary.frame().index.get_level_values("id")[0]
 |      >>> retrieved = project.get(report_id)
 |      >>> type(retrieved).__name__
 |      'EstimatorReport'
 |      >>> tmpdir.cleanup()
 |
 |  put(self, key: 'str', report: 'EstimatorReport | CrossValidationReport')
 |      Put a key-report pair to the project.
 |
 |      If the key already exists, its last report is modified to point to this new
 |      report, while keeping track of the report history.
 |
 |      Parameters
 |      ----------
 |      key : str
 |          The key to associate with ``report`` in the project.
 |          Name of the run for mode:mlflow
 |      report : EstimatorReport | CrossValidationReport
 |          The report to associate with ``key`` in the project.
 |
 |      Returns
 |      -------
 |      None
 |          The report is persisted in the project backend.
 |
 |      Examples
 |      --------
 |      >>> from sklearn.datasets import make_regression
 |      >>> from sklearn.linear_model import LinearRegression
 |      >>> from pathlib import Path
 |      >>> from tempfile import TemporaryDirectory
 |      >>> from skore import Project, evaluate
 |      >>> X, y = make_regression(random_state=42)
 |      >>> report = evaluate(LinearRegression(), X, y, splitter=0.2)
 |      >>> tmpdir = TemporaryDirectory()
 |      >>> project = Project(name="my-xp", mode="local", workspace=Path(tmpdir.name))
 |      >>> project.put("my-regression", report)
 |      >>> tmpdir.cleanup()
 |
 |  summarize(self) -> 'Summary'
 |      Obtain metadata/metrics for all persisted reports.
 |
 |      Reports are returned in ascending order of their ``date`` field.
 |
 |      Returns
 |      -------
 |      summary : Summary
 |          Metadata and metrics for every report persisted in the project.
 |
 |      See Also
 |      --------
 |      :class:`~skore.Summary` :
 |          Tabular view with interactive filtering in Jupyter.
 |      :func:`~skore.compare` :
 |          Compare selected reports side by side.
 |
 |  sync(self, other: 'Project | ProjectMode', *, bidirectional: 'bool' = False, dry_run: 'bool' = False, **kwargs: 'Any') -> 'DataFrame'
 |      Copy missing reports to another project.
 |
 |      Reports are matched using the ``report_id`` column returned by
 |      ``Project.summarize().frame()``. Set ``bidirectional=True`` to copy missing
 |      reports in both directions.
 |
 |      Parameters
 |      ----------
 |      other : Project or {"hub", "local", "mlflow"}
 |          Destination project. When a mode is given, build the destination with this
 |          project's name and the mode-specific keyword arguments.
 |      bidirectional : bool, default=False
 |          If ``False``, transfer reports from this project to ``other``. If ``True``,
 |          also transfer reports missing from this project.
 |      dry_run : bool, default=False
 |          Return the planned operations without loading or storing reports.
 |      **kwargs : dict
 |          Mode-specific arguments used to build the destination when ``other`` is a
 |          mode string. For example, pass ``workspace`` for ``"hub"`` or
 |          ``tracking_uri`` for ``"mlflow"``.
 |
 |      Returns
 |      -------
 |      result : pandas.DataFrame
 |          Synchronization status indexed by ``report_id``. The ``direction`` column
 |          is ``"outbound"`` from this project to ``other``, ``"inbound"`` from
 |          ``other`` to this project, or missing for skipped reports. The ``status``
 |          column is ``"planned"``, ``"transferred"``, or ``"skipped"``.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  delete(name: 'str', *, mode: 'ProjectMode' = 'local', **kwargs)
 |      Delete a project.
 |
 |      Parameters
 |      ----------
 |      name : str
 |          The name of the project.
 |      mode : {"hub", "local", "mlflow"}, default "local"
 |          The mode of the project.
 |      **kwargs : dict
 |          Extra keyword arguments passed to the project, depending on its mode.
 |
 |          workspace : str or Path-like, optional
 |              See the :class:`Project` class docstring for details.
 |
 |          tracking_uri : str, mode:mlflow only.
 |              The URI of the MLflow tracking server.
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties defined here:
 |
 |  mode
 |      The mode of the project.
 |
 |  name
 |      The name of the project.
 |
 |  tracking_uri
 |      The MLflow tracking URI for mlflow mode; ``None`` otherwise.
 |
 |  workspace
 |      The workspace for local and hub modes; ``None`` otherwise.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

```

## Project.put

### Signature
```
(self, key: 'str', report: 'EstimatorReport | CrossValidationReport')
```

### help()
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

## Project.summarize

### Signature
```
(self) -> 'Summary'
```

### help()
```
Python Library Documentation: function summarize in module skore._project.project

summarize(self) -> 'Summary'
    Obtain metadata/metrics for all persisted reports.

    Reports are returned in ascending order of their ``date`` field.

    Returns
    -------
    summary : Summary
        Metadata and metrics for every report persisted in the project.

    See Also
    --------
    :class:`~skore.Summary` :
        Tabular view with interactive filtering in Jupyter.
    :func:`~skore.compare` :
        Compare selected reports side by side.

```

## Project.get

### Signature
```
(self, id: 'str') -> 'EstimatorReport | CrossValidationReport'
```

### help()
```
Python Library Documentation: function get in module skore._project.project

get(self, id: 'str') -> 'EstimatorReport | CrossValidationReport'
    Get a persisted report by its id.

    Report IDs can be found via :meth:`skore.Project.summarize`, which is also the
    preferred method of interacting with a ``skore.Project``. The ``id`` passed here
    must match the ``id`` column returned by :meth:`Project.summarize`.

    Parameters
    ----------
    id : str
        The id of a report already put in the ``project``.

    Returns
    -------
    report : EstimatorReport or CrossValidationReport
        The report associated with ``id``.

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
    >>> summary = project.summarize()
    >>> report_id = summary.frame().index.get_level_values("id")[0]
    >>> retrieved = project.get(report_id)
    >>> type(retrieved).__name__
    'EstimatorReport'
    >>> tmpdir.cleanup()

```
