import secrets
from os import getenv
from typing import Any
from warnings import warn

from .config_loader import ConfigLoader


class Config:
    """Base configuration class containing common settings."""

    def __init__(self, 
                 config_data: dict[str, Any] | None = None, 
                 filename: str = "config.toml") -> None:

        if config_data is None:
            loader: ConfigLoader = ConfigLoader()
            self.config_data = loader.load(filename)
        else:
            self.config_data = config_data
        
        # Core Flask settings
        self.SECRET_KEY: str = self.getValue("core",
                                              "secret_key",
                                              secrets.token_urlsafe(40))

        self.STATIC_FOLDER: str = self.getValue("core", 
                                                 "static_folder",
                                                 "static")
        
        self.TEMPLATES_FOLDER: str = self.getValue("core",
                                         "templates_folder",
                                         "templates")

        
        # Security settings
        # TODO: Figure out sessions, cookies, and other security features.
        self.WTF_CSRF_ENABLED: bool = self.getValue("security", 
                                               "wtf_csrf_enabled", True)
    
    def getValue(self, section: str, key: str, 
                  hardcoded_default: Any = None) -> Any:
        """Get a configuration value with fallback."""
        # 1. Environment variables (first priority).
        env_key: str = key.upper()
        value: Any = getenv(env_key)
        
        if value is not None:
            warn(f"Using environment variable {env_key}"
                 f" for {section}.{key}")
            return value

        # 2. Try user config. next (second priority).
        user_section: dict[str, Any] = self.config_data.get(section, {})
        
        if key in user_section:
            return user_section[key]
        
        # Return a hardcoded default (no config.toml 
        # or env variable being used).
        warn(f"Using hardcoded default for {section}.{key}")
        return hardcoded_default
