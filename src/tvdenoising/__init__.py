import importlib.metadata

from ._tv_1d import tv_1d


try:
    __version__ = importlib.metadata.version("tvdenoising")
except ImportError:
    __version__ = "0+unknown"

__all__ = ["tv_1d"]
