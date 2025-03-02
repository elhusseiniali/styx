import warnings
from pathlib import Path
from typing import Any

try:
    import tomllib
except ImportError:
    # Python < 3.11 doesn't have the stdlib tomllib (ref: https://docs.python.org/3/library/tomllib.html).
    # Importing tomli because we test with older python versions.

    # Using tomli instead of toml lib. because it seems 
    # that toml isn't maintained anymore, and that
    # the community uses tomli instead.
    import tomli as tomllib  # type: ignore


class ConfigLoader:
    """Class to load a toml configuration file."""

    def __init__(self) -> None:
        self.BASE_DIR: Path = Path(__file__).resolve().parent


    def load(self, filename: str) -> dict[str, Any]:
        """Load a toml file."""
        config_path: Path = self.BASE_DIR.joinpath(filename)

        # checking if the file exists.
        if not config_path.exists():
            # TODO: capture warnings into logging easily later. e.g. 
            # logging.captureWarnings(True).
            warnings.warn(f"Configuration file not found: "
                          f"{config_path.as_posix()}")
            
            # If the configuration file does not
            # exist we can fallback to default values.
            return {}
        
        # loading the toml file.
        try:
            with config_path.open("rb") as f:
                return tomllib.load(f)
        except Exception as e:
            # If the configuration file is not
            # parsed properly we also fallback to default values.
            warnings.warn(f"Error loading {filename}: {str(e)}")
            return {}
