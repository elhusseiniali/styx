from pathlib import Path
from typing import Any
from warnings import warn

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

    def _find_config_file(self) -> Path | None:
        """Recursively search for the config file in the project directory.

        Returns:
            Path | None: the path to the file or none if it couldn't find it.

        """
        if self.filename is None:
            return None

        # Search through all directories and files
        for path in self.BASE_DIR.rglob(self.filename):
            # Return the first matching file
            return path
        
        return None

    def load(self) -> dict[str, Any]:
        """Load a toml file."""
        config_path: Path | None = self._find_config_file()

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
