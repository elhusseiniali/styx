from flask import Flask

from config import Config, DevConfig

from .extensions import bcrypt, db, migrate  # type: ignore


def create_app(config_class: type[Config] = DevConfig) -> Flask:
    """Application factory that creates and configures the Flask app.
    
    Args:
        config_class (type[Config], optional): Selects a type of 
        configuration defined in config.py (e.g. TestConfig, DevConfig...).
        Defaults to DevConfig.

    Returns:
        Flask: The configured Flask application instance
        
    """
    app: Flask = Flask(__name__)

    # Configuraion
    app.config.from_object(config_class)

    # Initialize extensions
    register_extensions(app)

    # TODO: ADD BLUEPRINT REGISTRATIONS !!!

    register_commands(app)
    
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
    """Register custom CLI commands with the Flask application."""

    @app.cli.command("create-db")
    def create_db() -> None:
        """Create all tables defined in SQLAlchemy models.

        Usage:
            $ flask create-db

        Effects:
            - Creates all tables defined in SQLAlchemy models
            - Prints confirmation message
            - Database exists only until application stops
        """
        with app.app_context():
            db.create_all()
            print("Database tables created!")

    @app.cli.command("delete-db")
    def delete_db() -> None:
        """Drop all tables defined in SQLAlchemy models.

        Usage:
            $ flask delete-db 

        Effects:
            - Drops all tables defined in SQLAlchemy models
            - Prints confirmation message
            - Irreversible operation - all data will be lost immediately
        """
        with app.app_context():
            db.drop_all()
            print("Database tables deleted!")
