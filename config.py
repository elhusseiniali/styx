"""Flask application configuration settings.

This module defines configuration classes for different environments
(development, and  testing). It handles environment variables
and sets default values for Flask application settings.
"""
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Base configuration class containing common settings.
    
    Attributes:
        SECRET_KEY (str): Secret key for securing sessions and tokens.
        STATIC_FOLDER (str): Path to static assets directory.
        TEMPLATES_FOLDER (str): Path to templates directory.
        WTF_CSRF_ENABLED (bool): Enable CSRF protection for Flask-WTF forms.

    """
    
    # Core Flask settings
    SECRET_KEY = environ.get("SECRET_KEY")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # Security settings
    # TODO: Figure out sesssions, cookies, and other security features
    WTF_CSRF_ENABLED = True


class DevConfig(Config):
    """Development environment configuration.

    Inherits from base Config class and adds development-specific settings.

    Attributes:
        FLASK_ENV (str): Application environment ('development')
        DEBUG (bool): Enable debug mode with detailed error pages
        TESTING (bool): Disable testing mode
        SQLALCHEMY_DATABASE_URI (str): Database connection URI
        TEMPLATES_AUTO_RELOAD (bool): Auto-reload templates during development

    """

    FLASK_ENV = "development"
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")

    # Disable caching for development
    TEMPLATES_AUTO_RELOAD = True


class TestConfig(Config):
    """Testing environment configuration.

    Inherits from base Config class and configures settings for test runs.

    Attributes:
        FLASK_ENV (str): Application environment ('development')
        DEBUG (bool): Enable debug mode
        TESTING (bool): Enable testing mode
        SQLALCHEMY_DATABASE_URI (str): In-memory SQLite database URI
        WTF_CSRF_ENABLED (bool): Disable CSRF protection for
        easier form testing

    """

    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI =  "sqlite:///:memory:"  # keeps database in
                                                     # memory for testing 
                                                     # (sqlite specific)
    WTF_CSRF_ENABLED = False
