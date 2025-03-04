from os import getenv
from pathlib import Path
from typing import Any
from warnings import warn


def get_config_value(section: str,
                     key: str,
                     config_data,
                     default: Any) -> Any:
        """Get a configuration value with fallback."""
        # 1. Environment variables (first priority).
        env_key: str = key.upper()
        value: Any = getenv(env_key)

        if value is not None:
            warn(f"Using environment variable {env_key}"
                 f" for {section}.{key}")
            return value

        # 2. Try user config. next (second priority).
        user_section: dict[str, Any] = config_data.get(section, {})
        
        if key in user_section:
            return user_section[key]

        # Return a hardcoded default (no config.toml 
        # or env variable being used).
        warn(f"Using hardcoded default for {section}.{key}")
        return default


def find_config_file(base_dir, filename) -> (Path | None):
    """Recursively search for the config file in the project directory.

    Returns:
        Path | None: the path to the file or none if it couldn't find it.

    """
    if filename is None:
        return None

    # Search through all directories and files
    for path in base_dir.rglob(filename):
        # Return the first matching file
        return path

    return None
