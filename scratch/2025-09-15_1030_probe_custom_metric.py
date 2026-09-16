"""Shape 2/1 probe: does skore 0.25 support custom metrics on reports / evaluate?"""

import inspect

import skore

print("evaluate:", inspect.signature(skore.evaluate))

# Look for custom-metric plumbing on the report metrics namespace
from sklearn.linear_model import LogisticRegression

rep_args = inspect.signature(skore.EstimatorReport.__init__)
print("EstimatorReport:", rep_args)

import skore.metrics as m  # noqa

print("skore.metrics:", [n for n in dir(m) if not n.startswith("_")])
