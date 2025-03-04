from .config import Config
from .utils import get_config_value


class TestingConfig(Config):
    """Testing environment configuration.

    Inherits from base Config class and configures settings for test runs.
    """

    def __init__(self, filename: str | None = None) -> None:

        super().__init__(filename=filename)

        self.SECTION = "testing"

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
                                              True)

        self.SQLALCHEMY_DATABASE_URI: str = get_config_value(self.SECTION,
                                                             "database_uri",
                                                             self.config_data,
                                                             "sqlite:///:memory:")

        self.WTF_CSRF_ENABLED: bool = get_config_value(self.SECTION,
                                                       "wtf_csrf_enabled",
                                                       self.config_data,
                                                       False)

        self.PROPAGATE_EXCEPTIONS: bool = get_config_value(self.SECTION,
                                                           "propagate_exceptions",
                                                           self.config_data,
                                                           True)
