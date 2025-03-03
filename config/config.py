import secrets
from os import getenv
from typing import Any
from warnings import warn

from .config_loader import ConfigLoader


class Config:
    """Base configuration class containing common settings."""
    
    def __init__(self, filename: str | None = None) -> None:
        loader: ConfigLoader = ConfigLoader(filename)
        self.config_data = loader.load()
        
        self.SECTION = "core"
        
        # Core Flask settings
        self.SECRET_KEY: str = self.getValue(self.SECTION,
                                              "secret_key",
                                              secrets.token_urlsafe(40))

        self.STATIC_FOLDER: str = self.getValue(self.SECTION,
                                                 "static_folder",
                                                 "static")
        
        self.TEMPLATES_FOLDER: str = self.getValue(self.SECTION,
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
