import importlib.metadata


try:
    __version__ = importlib.metadata.version("trendfilter")
except ImportError:
    __version__ = "0+unknown"
