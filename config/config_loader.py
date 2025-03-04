from pathlib import Path
from typing import Any
from warnings import warn

from .utils import find_config_file

try:
    import tomllib
except ImportError:
    # Python < 3.11 doesn't have the stdlib tomllib.
    # Importing tomli because we test with older python versions.

    # Using tomli instead of toml lib. because it seems 
    # that toml isn't maintained anymore, and that
    # the community uses tomli instead.
    import tomli as tomllib  # type: ignore


class ConfigLoader:
    """Class to load a toml configuration file."""

    def __init__(self, filename: str | None = None) -> None:
        # If no filename is provided, explicitly set to config.toml
        self.filename = filename if filename is not None else "config.toml"
        self.BASE_DIR = Path(__file__).resolve().parent.parent

    def load(self) -> dict[str, Any]:
        """Load a toml file."""
        config_path: (Path | None) = find_config_file(base_dir=self.BASE_DIR,
                                                      filename=self.filename)

        if config_path is None:
            warn(f"Configuration file '{self.filename}'"
                 f" not found in project directory")
            return {}
         
        # loading the toml file.
        try:
            with config_path.open("rb") as f:
                return tomllib.load(f)
        except Exception as e:
            # If the configuration file is not
            # parsed properly we fallback to default values.
            warn(f"Error loading {self.filename}: {str(e)}")
            return {}
