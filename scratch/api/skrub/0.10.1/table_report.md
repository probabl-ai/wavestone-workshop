# skrub.TableReport

Source: inspect: skrub.TableReport @ skrub 0.10.1

## Signature
```
(dataframe, n_rows=None, order_by=None, title=None, column_filters=None, verbose=None, plot_distributions='auto', compute_associations='auto', open_tab='table', max_plot_columns=None, max_association_columns=None)
```

## help()
```
Python Library Documentation: class TableReport in module skrub._reporting._table_report

class TableReport(builtins.object)
 |  TableReport(dataframe, n_rows=None, order_by=None, title=None, column_filters=None, verbose=None, plot_distributions='auto', compute_associations='auto', open_tab='table', max_plot_columns=None, max_association_columns=None)
 |
 |  Summarize the contents of a dataframe.
 |
 |  This class summarizes a dataframe or numpy array, providing information such as
 |  the type and summary statistics (mean, number of missing values, etc.) for each
 |  column. Numpy arrays are converted to pandas DataFrame or Series. The computed
 |  statistics can be accessed interactively in a Jupyter notebook or web browser.
 |  Alternatively, it can be saved or exported in JSON, Markdown, or HTML format
 |  for programmatic access or for inclusion in documents.
 |
 |  Parameters
 |  ----------
 |  dataframe : pandas or polars Series or DataFrame
 |      The dataframe or series to summarize.
 |  n_rows : int, default=None
 |      Maximum number of rows to show in the sample table. Half will be taken
 |      from the beginning (head) of the dataframe and half from the end
 |      (tail). Note this is only for display. Summary statistics, histograms
 |      etc. are computed using the whole dataframe.
 |
 |      The default value ``None`` uses the global configuration (see
 |      :func:`set_config`), which then defaults to 10.
 |
 |  order_by : str, deprecated
 |      Deprecated. Column name to use for sorting. Other numerical columns
 |      will be plotted as function of the sorting column. Must be of
 |      numerical or datetime type.
 |
 |      .. deprecated:: 0.10.0
 |
 |  title : str
 |      Title for the report.
 |
 |  column_filters : dict
 |      A dict for adding custom entries to the column filter dropdown menu.
 |      Each key is the filter named to be displayed in the dropdown menu
 |      (e.g. ``"first_10"``), and the value is the desired filter. Filters
 |      may be specified as a list of column names, a list of column indices,
 |      or a :ref:`skrub selectors <user_guide_selectors>` object.
 |      See the end of the "Examples" section below for details.
 |
 |  verbose : int, default = None
 |      Whether to print progress information while the report is being generated.
 |
 |      * verbose = ``None`` uses the global configuration (see :func:`set_config`),
 |        which then defaults to 1.
 |      * verbose = 1 prints how many columns have been processed so far.
 |      * verbose = 0 silences the output.
 |
 |  plot_distributions : bool or "auto", default="auto"
 |      Whether to plot the distributions of the columns.
 |
 |      - ``True``: always generate plots, regardless of column count.
 |      - ``False``: never generate plots.
 |      - ``"auto"`` (default): generate plots only when the number of columns
 |        does not exceed the configured ``table_report_plots_threshold``
 |        (see :func:`set_config`).
 |
 |  compute_associations : bool or "auto", default="auto"
 |      Whether to compute associations between columns.
 |
 |      - ``True``: always compute associations, regardless of column count.
 |      - ``False``: never compute associations.
 |      - ``"auto"`` (default): compute associations only when the number of
 |        columns does not exceed the configured ``table_report_associations_threshold``
 |        (see :func:`set_config`).
 |
 |  max_plot_columns : int or "all", deprecated
 |      Deprecated in favor of ``plot_distributions``. This parameter overrides
 |      the value chosen for ``plot_distributions`` when it is not None.
 |
 |      .. deprecated:: 0.9.0
 |
 |  max_association_columns : int or "all", deprecated
 |      Deprecated in favor of ``compute_associations``. This parameter overrides
 |      the value chosen for ``compute_associations`` when it is not None.
 |
 |      .. deprecated:: 0.9.0
 |
 |  open_tab : str, default="table"
 |      The tab that will 
```

# skrub.TableReport.write_html

Source: inspect: skrub.TableReport.write_html @ skrub 0.10.1

## Signature
```
(self, file)
```

## help()
```
Python Library Documentation: function write_html in module skrub._reporting._table_report

write_html(self, file)
    Store the report into an HTML file.

    Parameters
    ----------
    file : str, pathlib.Path or file object
        The file object or path of the file to store the HTML output.

```

# skrub.TableReport.json

Source: inspect: skrub.TableReport.json @ skrub 0.10.1

## Signature
```
(self)
```

## help()
```
Python Library Documentation: function json in module skrub._reporting._table_report

json(self)
    Get the report data in JSON format.

    By default, the JSON output includes the plots in SVG format, which can
    be quite verbose. Plots can be disabled by setting
    ``plot_distributions=False`` when generating the report.

    The schema of the JSON data is reported in :ref:`table_report_json_schema`.


    Returns
    -------
    str :
        The JSON data.

```

# skrub.column_associations

Source: inspect: skrub.column_associations @ skrub 0.10.1

## Signature
```
(df, *, compute_pearson=True)
```

## help()
```
Python Library Documentation: function column_associations in module skrub._column_associations

column_associations(df, *, compute_pearson=True)
    Get measures of statistical associations between all pairs of columns.

    Reported metrics include Cramer's V statistic and Pearson's Correlation
    Coefficient. The result is returned as a dataframe that contains the column
    name and idx for the left and right table and the requested associations;
    results are sorted in descending order by Cramer's V association.

    Parameters
    ----------
    df : dataframe
        The dataframe whose columns will be compared to each other.
    compute_pearson : bool, default=True
        Whether to compute Pearson's Correlation Coefficient. Currently, computing Pearson correlations for polars DataFrames requires PyArrow to be installed and internally converts the dataframe to pandas.

    Returns
    -------
    dataframe
        The computed associations.

    Notes
    -----
    The result is returned as a dataframe with columns:

    ``['left_column_name', 'left_column_idx', 'right_column_name',
    'right_column_idx', 'cramer_v', 'pearson_corr']``.

    When ``compute_pearson=False``, the ``'pearson_corr'`` column is omitted.

    As the function is commutative, each pair of columns appears only once
    (either ``col_1``, ``col_2`` or ``col_2``, ``col_1`` but not both).
    The results are sorted from most associated to least associated.

    To compute the Cramer's V statistic, all columns are discretized. Numeric
    columns are binned with 10 bins. For categorical columns, only the 10 most
    frequent categories are considered. In both cases, nulls are treated as a
    separate category, ie a separate row in the contingency table. Thus,
    associations between the values of 2 columns or between their missingness
    patterns may be captured.
    Cramér's V is a measure of association between two nominal variables,
    giving a value between 0 and +1 (inclusive).

    * `Cramer's V <https://en.wikipedia.org/wiki/Cramér%27s_V>`_

    To compute the Pearson's Correlation Coefficient, only numeric columns are
    considered. The correlation is computed using the Pearson method used in
    pandas or polars, depending on the dataframe. In both cases, lines containing NaNs
    are dropped.
    Pearson's Correlation Coefficient is a measure of the linear correlation
    between two variables, giving a value between -1 and +1 (inclusive).

    * `Pearson's Correlation Coefficient
      <https://en.wikipedia.org/wiki/Pearson_correlation_coefficient>`_

    * `pandas.DataFrame.corr
      <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html>`_

    Examples
    --------
    >>> import numpy as np
    >>> import pandas as pd
    >>> import skrub
    >>> pd.set_option('display.width', 200)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.precision', 4)
    >>> rng = np.random.default_rng(33)
    >>> df = pd.DataFrame({f"c_{i}": rng.random(size=20)*10 for i in range(5)})
    >>> df["c_str"] = [f"val {i}" for i in range(df.shape[0])]
    >>> df.shape
    (20, 6)
    >>> df.head()
          c_0     c_1     c_2     c_3     c_4  c_str
    0  4.4364  4.0114  6.9271  7.0970  4.8913  val 0
    1  5.6849  0.7192  7.6430  4.6441  2.5116  val 1
    2  9.0810  9.4011  1.9257  5.7429  6.2358  val 2
    3  2.5425  2.9678  9.7801  9.9879  6.0709  val 3
    4  5.8878  9.3223  5.3840  7.2006  2.1494  val 4
    >>> # Compute the associations
    >>> associations = skrub.column_associations(df)
    >>> associations # doctest: +SKIP
       left_column_name  left_column_idx right_column_name  right_column_idx  cramer_v  pearson_corr
    0              c_1                1               c_4                 4    0.8215        0.1597
    1              c_0                0               c_1                 1    0.8215        0.1123
    2              c_0                0               c_3                 3  
```
