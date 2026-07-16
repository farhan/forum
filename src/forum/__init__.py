"""
Openedx forum app.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("openedx-forum")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"
