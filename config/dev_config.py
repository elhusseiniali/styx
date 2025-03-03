from .config import Config


class DevConfig(Config):
    """Development environment configuration.

    Inherits from base Config class and adds development-specific settings.
    """
    
    def __init__(self, filename: str | None = None) -> None:

        super().__init__(filename=filename)

        self.SECTION = "development"
        
        self.FLASK_ENV: str = self.getValue(self.SECTION, "flask_env",
                                            "development")
                                  
        self.DEBUG: bool = self.getValue(self.SECTION, "debug", True)

        self.TESTING: bool = self.getValue(self.SECTION, "testing", False)

        self.SQLALCHEMY_DATABASE_URI: str = self.getValue(self.SECTION, 
                                                           "database_uri",
                                                           "sqlite:///dev.db")

        self.TEMPLATES_AUTO_RELOAD: bool = self.getValue(self.SECTION, 
                                                          "templates_auto_reload",
                                                          True)

        self.PROPAGATE_EXCEPTIONS: bool = self.getValue(self.SECTION,
                                                        "propagate_exceptions",
                                                        True)
