import secrets

from .config_loader import ConfigLoader
from .utils import get_config_value


class Config:
    """Base configuration class containing common settings."""

    def __init__(self, filename: str | None = None) -> None:
        loader: ConfigLoader = ConfigLoader(filename)
        self.config_data = loader.load()

        self.SECTION: str = "core"

        self.SECRET_KEY: str = get_config_value(self.SECTION,
                                                "secret_key",
                                                self.config_data,
                                                secrets.token_urlsafe(40))
        
        self.STATIC_FOLDER: str = get_config_value(self.SECTION,
                                                   "static_folder",
                                                   self.config_data,
                                                   "static")

        self.TEMPLATES_FOLDER: str = get_config_value(self.SECTION,
                                                      "templates_folder",
                                                      self.config_data,
                                                      "templates")

        # Security settings
        # TODO: Figure out sessions, cookies, and other security features.
        self.WTF_CSRF_ENABLED: bool = get_config_value(self.SECTION,
                                                       "wtf_csrf_enabled",
                                                       self.config_data,
                                                       True)
