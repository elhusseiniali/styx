from styx import db, login_manager, bcrypt
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from flask_validator import ValidateEmail


@login_manager.user_loader
def load_user(user_id):
    """Get the current logged-in User object.

    Parameters
    ----------
    user_id : [int]
        User ID.

    Returns
    -------
    [User]
        A User object (see boilerplate.models).
    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """[User]
    Parameters
    ----------
    username: [string]
        Unique username.
    email: [email]
        Unique email.
    image_file: [string]
        File path for the chosen profile picture.
        Default image is default.jpg.
    _password: [string]
        Hashed password.
        Extra functions are there to hash the password then store it.

    Relationships
    -------------
    None.
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    image_file = db.Column(db.String(30),
                           nullable=False,
                           default='default.jpg')

    _password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return (f"User('{self.username}': '{self.email}')")

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.generate_password_hash(password)

    def verify_password(self, password):
        return bcrypt.check_password_hash(self._password, password)

    @classmethod
    def __declare_last__(cls):
        # check_deliverability can be set to True
        # after the developer updated the release on PyPI.
        # https://github.com/xeBuz/Flask-Validator/issues/79
        ValidateEmail(User.email,
                      allow_smtputf8=True,
                      check_deliverability=True,
                      throw_exception=True,
                      message="The e-mail is invalid.")


class MuscleGroup(db.Model):
    """[MuscleGroup]
    Parameters
    ----------
    name: [string]
        Name of muscle group.

    Relationships
    -------------
    exercise: [Exercise]
    """
    __tablename__ = "musclegroup"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(50), unique=False, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return (f"MuscleGroup('{self.name}')")


ExerciseAndType = db.Table(
    "ExerciseAndType", db.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('exercise_type_id', db.Integer,
              db.ForeignKey('exercisetype.id')),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'))
)


class ExerciseType(db.Model):
    """[ExerciseType]
    Parameters
    ----------
    name: [string]
        Type of the exercise (compound, isolation, push, pull).

    Relationships
    -------------
    exercise: [Exercise]
    """
    __tablename__ = "exercisetype"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(50), unique=False, nullable=False)

    exercises = db.relationship("Exercise", secondary=ExerciseAndType,
                                back_populates="exercise_type")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return (f"ExerciseType('{self.name}')")


ExerciseVideo = db.Table(
    "ExerciseVideo", db.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('video_id', db.Integer, db.ForeignKey('video.id')),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'))
)


class Video(db.Model):
    """[Videp]
    Table that stores instructional videos for different exercises.

    Parameters
    ----------
    url : [str]
        URL to the video.
    """
    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    url = db.Column(db.String(50), unique=False, nullable=False)

    exercise = db.relationship("Exercise", secondary=ExerciseVideo,
                               back_populates="videos")

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return f"Video(URL: {self.url})"


class Exercise(db.Model):
    """[Exercise]
    Parameters
    ----------
    name: [string]
        Exercise name.

    Relationships
    -------------
    exercise_type: [ExerciseType]
        Many to many
    videos: [Video]
        Many to many
        -   The reason behind this is that some exercises are
            similar enough for the videos to be overlapping (e.g.
            Lateral Raises and Full ROM Lateral Raises)
    """
    __tablename__ = "exercise"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(50), unique=False, nullable=False)

    exercise_type = db.relationship("ExerciseType", secondary=ExerciseAndType,
                                    back_populates="exercises")

    videos = db.relationship("Video", secondary=ExerciseVideo,
                             back_populates="exercise")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return (f"Exercise('{self.name}')")
