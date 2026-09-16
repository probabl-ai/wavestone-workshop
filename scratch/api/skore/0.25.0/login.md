# skore.login

Source: inspect: skore @ 0.25.0
Probed: 2025-09-15

## skore.login

### Signature
```
(*, mode: Literal['hub', 'local', 'mlflow'] = 'hub', **kwargs)
```

### help()
```
Python Library Documentation: function login in module skore._project.login

login(*, mode: Literal['hub', 'local', 'mlflow'] = 'hub', **kwargs)
    Log in to Skore Hub for the duration of the session (e.g. script).

    This command is only useful if you have an account on Skore Hub and wish
    to push artifacts to it.

    By default, it will open a login screen on your browser. However, this login only
    persists for the lifetime of the Python process (e.g. one run of a script, or one
    Jupyter session), so you will have to authenticate via your browser at every run.
    The recommended way to connect to Skore Hub for repeated script runs is using an
    API key; refer to the Skore Hub documentation for how to create one.

    Parameters
    ----------
    mode : {"hub", "local", "mlflow"}, default="hub"
        The mode of the storage backend to log in. If the mode is not "hub", the
        function is a no-op.

    **kwargs : dict
        Extra keyword arguments passed to the login function, depending on its mode.

        Arguments for ``mode="hub"``:

        timeout : int, default=600
            The time, in seconds, before raising an error if communication with
            Skore Hub fails.

    Returns
    -------
    None
        For ``mode="local"`` and ``mode="mlflow"``. For ``mode="hub"``, the return
        value depends on the hub login plugin.

    Examples
    --------
    >>> from skore import login
    >>> login(mode="local")

    See Also
    --------
    :class:`~skore.Project` :
        Refer to the :ref:`project` section of the user guide for more details.

```
