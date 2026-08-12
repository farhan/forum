"""
Openedx forum app.
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("forum")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
