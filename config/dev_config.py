from .config import Config


class DevConfig(Config):
    """Development environment configuration.

    Inherits from base Config class and adds development-specific settings.
    """
    
    def __init__(self) -> None:
        super().__init__()

        self.FLASK_ENV: str = self.getValue("development", "flask_env",
                                             "development")
                                  
        self.DEBUG: bool = self.getValue("development", "debug", True)

        self.TESTING: bool = self.getValue("development", "testing", False)

        self.SQLALCHEMY_DATABASE_URI: str = self.getValue("development", 
                                                           "database_uri",
                                                           "sqlite:///dev.db")

        self.TEMPLATES_AUTO_RELOAD: bool = self.getValue("development", 
                                                          "templates_auto_reload",
                                                          True)

        self.PROPAGATE_EXCEPTIONS: bool = self.getValue("development",
                                                        "propagate_exceptions",
                                                        True)
