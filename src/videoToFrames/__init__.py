# __init__.py

import pathlib
from importlib import resources

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# Load config file
_cfg = tomllib.loads(resources.read_text("videoToFrames", "config.toml"))

# Version of the video to frames package
__version__ = _cfg["version"]["version"]