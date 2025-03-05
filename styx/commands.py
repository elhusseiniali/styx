from flask.cli import AppGroup

from .extensions import db

# Create AppGroup for database commands
db_cli = AppGroup("db", help="Database management commands")


@db_cli.command("create")
def create_db():
    """Create all database tables."""
    db.create_all()
    print("Database tables created!")


@db_cli.command("delete")
def delete_db():
    """Drop all database tables.

    Warning:
        This is an irreversible operation.

    """
    db.drop_all()
    print("Database tables deleted!")


@db_cli.command("reset")
def reset_db():
    """Reset the database by dropping and recreating all tables.

    Warning:
        This operation will delete all existing data.

    """
    db.drop_all()
    db.create_all()
    print("Database tables reset!")
