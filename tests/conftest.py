import os
import sys

# Ensure project root is on sys.path for test imports
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Verify required test dependencies are installed
from tests.dependency_check import *  # noqa: F401,F403
