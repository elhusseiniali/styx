from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from styx.config import BaseConfig


db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


#   Below import is necessary, even if the linter complains about it.
#   This is because the linter cannot distinguish between imports in a script
#   and imports in a package. The order of the imports is also important.
#   These two imports *had* to happen after initializing db.
from styx.models import User, MuscleGroup, ExerciseType, Video, Exercise

from flask_admin import Admin
from styx.admin_views import UserView
from styx.admin_views import MuscleGroupView, ExerciseTypeView, \
    VideoView, ExerciseView


admin = Admin(name='Styx Admin', template_mode='bootstrap3')
# Add administrative views here
admin.add_view(UserView(User, db.session))
admin.add_view(MuscleGroupView(MuscleGroup, db.session))
admin.add_view(ExerciseTypeView(ExerciseType, db.session))
admin.add_view(VideoView(Video, db.session))
admin.add_view(ExerciseView(Exercise, db.session))


# Image dimensions
MAX_HEIGHT = 400
MAX_WIDTH = 400


def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    from styx.core.users.views import users
    from styx.core.main.routes import main

    from styx.core.errors.handlers import errors

    from styx.core import blueprint as api
    app.register_blueprint(api, url_prefix='/api/1')

    app.register_blueprint(main)
    app.register_blueprint(errors)

    app.register_blueprint(users)

    return app
