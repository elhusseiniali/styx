from .config import Config
from .utils import get_config_value


class DevConfig(Config):
    """Development environment configuration.

    Inherits from base Config class and adds development-specific settings.
    """
    
    def __init__(self, filename: str | None = None) -> None:

        super().__init__(filename=filename)

        self.SECTION = "development"

        self.FLASK_ENV: str = get_config_value(self.SECTION,
                                               "flask_env",
                                               self.config_data,
                                               "development")

        self.DEBUG: bool = get_config_value(self.SECTION,
                                            "debug",
                                            self.config_data,
                                            True)

        self.TESTING: bool = get_config_value(self.SECTION,
                                              "testing",
                                              self.config_data,
                                              False)

        self.SQLALCHEMY_DATABASE_URI: str = get_config_value(self.SECTION, 
                                                             "database_uri",
                                                             self.config_data,
                                                             "sqlite:///dev.db")

        self.TEMPLATES_AUTO_RELOAD: bool = get_config_value(self.SECTION,
                                                            "templates_auto_reload",
                                                            self.config_data,
                                                            True)

        self.PROPAGATE_EXCEPTIONS: bool = get_config_value(self.SECTION,
                                                           "propagate_exceptions",
                                                           self.config_data,
                                                           True)
