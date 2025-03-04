from flask import Flask

from config import Config, DevConfig

from .commands import db_cli
from .extensions import bcrypt, db, migrate  # type: ignore


def create_app(config_class: type[Config] = DevConfig,
               filename: str | None = None) -> Flask:
    """Application factory that creates and configures the Flask app.
    
    Args:
        config_class (type[Config], optional): Selects a type of 
        configuration defined in config.py (e.g. TestConfig, DevConfig...).
        Defaults to DevConfig.

        filename (str, optional): Selects a TOML file to take 
        configuration data from. Default to None.

    Returns:
        Flask: The configured Flask application instance
        
    """
    # Initialize core Flask application
    app: Flask = Flask(__name__)

    # Apply configuration
    app_config: Config = config_class(filename=filename)
    app.config.from_object(app_config)

    # Set up extensions
    register_extensions(app)

    # Add CLI commands
    register_commands(app)

    # TODO: ADD BLUEPRINT REGISTRATIONS

    return app


def register_extensions(app: Flask) -> None:
    """Register extensions with the Flask application.

    Extensions registered: SQLAlchemy, Flask-Migrate, and
    Flask-Bcrypt.

    Args:
        app (Flask): Flask application instance.

    """
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)


def register_commands(app: Flask) -> None:
    """Register cli commands with the Flask application.

    Args:
        app (Flask): Flask application instance.

    """
    app.cli.add_command(db_cli)
