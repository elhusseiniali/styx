from .config import Config


class TestingConfig(Config):
    """Testing environment configuration.

    Inherits from base Config class and configures settings for test runs.
    """

    def __init__(self) -> None:
        super().__init__()

        self.FLASK_ENV: str = self.getValue("testing",
                                            "flask_env",
                                            "development")

        self.DEBUG: bool = self.getValue("testing", "debug", True)

        self.TESTING: bool = self.getValue("testing", "testing", True)

        self.SQLALCHEMY_DATABASE_URI: str = self.getValue("testing",
                                                      "database_uri",
                                                      "sqlite:///:memory:")

        self.WTF_CSRF_ENABLED: bool = self.getValue("testing",
                                               "wtf_csrf_enabled",
                                               False)

        self.PROPAGATE_EXCEPTIONS: bool = self.getValue("testing",
                                                        "propagate_exceptions",
                                                        True)
