from boilerplate.models import User
from boilerplate import db


class UserDAO():
    """Class to handle all database operations
    for models.User class.
    """
    __instance__ = None

    def __init__(self):
        if UserDAO.__instance__ is None:
            UserDAO.__instance__ = self
        else:
            raise Exception("You cannot create another UserDAO class")

    @staticmethod
    def get_instance():
        if not UserDAO.__instance__:
            UserDAO()
        return UserDAO.__instance__

    def add(self, user):
        db.session.add(user)
        db.session.commit()

    def get_all(self):
        return db.session.query(User).all()

    def get_by_id(self, user_id):
        return db.session.query(User).get(user_id)

    def get_by_username(self, username):
        return db.session.query(User).filter_by(username=username).first()

    def get_by_email(self, email):
        return db.session.query(User).filter_by(email=email).first()

    def delete_user_by_id(self, user_id):
        db.session.query(User).filter_by(id=user_id).delete()
        db.session.commit()


user_dao = UserDAO.get_instance()
