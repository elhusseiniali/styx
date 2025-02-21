from flask_bcrypt import Bcrypt  # type: ignore
from flask_migrate import Migrate  # type: ignore
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
bcrypt: Bcrypt = Bcrypt()
