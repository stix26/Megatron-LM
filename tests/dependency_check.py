import importlib
import sys

REQUIRED_PACKAGES = ["einops"]
missing = [pkg for pkg in REQUIRED_PACKAGES if importlib.util.find_spec(pkg) is None]
if missing:
    missing_list = ", ".join(missing)
    raise ImportError(f"Missing required packages: {missing_list}")
