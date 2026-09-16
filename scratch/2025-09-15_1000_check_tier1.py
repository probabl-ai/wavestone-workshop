"""Tier 1 import check: sklearn, skrub, skore — report versions."""
import sklearn
import skore
import skrub

print("sklearn", sklearn.__version__)
print("skrub", skrub.__version__)
print("skore", skore.__version__)
