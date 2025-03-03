from .config import Config


class TestingConfig(Config):
    """Testing environment configuration.

    Inherits from base Config class and configures settings for test runs.
    """

    def __init__(self, filename: str | None = None) -> None:

        super().__init__(filename=filename)

        self.SECTION = "testing"

        self.FLASK_ENV: str = self.getValue(self.SECTION,
                                            "flask_env",
                                            "development")

        self.DEBUG: bool = self.getValue(self.SECTION, "debug", True)

        self.TESTING: bool = self.getValue(self.SECTION, "testing", True)

        self.SQLALCHEMY_DATABASE_URI: str = self.getValue(self.SECTION,
                                                      "database_uri",
                                                      "sqlite:///:memory:")

        self.WTF_CSRF_ENABLED: bool = self.getValue(self.SECTION,
                                               "wtf_csrf_enabled",
                                               False)

        self.PROPAGATE_EXCEPTIONS: bool = self.getValue(self.SECTION,
                                                        "propagate_exceptions",
                                                        True)
