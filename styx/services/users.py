from styx.dao.users import user_dao, User, db


class UserService():
    __instance__ = None

    def __init__(self):
        if UserService.__instance__ is None:
            UserService.__instance__ = self
        else:
            raise Exception("You cannot create another UserService class")

    @staticmethod
    def get_instance():
        if not UserService.__instance__:
            UserService()
        return UserService.__instance__

    def create_user(self, username, email, password):
        if (username is None) or (email is None) \
           or (password is None):
            return None

        user = user_dao.get_by_username(username=username)
        if user is None:
            user = User(username=username,
                        email=email.casefold(),
                        password=password)
            user_dao.add(user)
            return user
        return None

    def update_user(self, user_id, username=None, email=None,
                    image_file=None):
        if (user_id is None):
            return False

        if (username is None) and (email is None) and (image_file is None):
            return False

        try:
            user = user_dao.get_by_id(user_id=user_id)

            if username:
                user.username = username
            if email:
                user.email = email
            if image_file:
                user.image_file = image_file

            db.session.commit()

            return True

        except Exception:
            return False

    def delete_user(self, user_id):
        if user_id is None:
            return False

        try:
            user = user_dao.get_by_id(user_id=int(user_id))
            if user:
                user_dao.delete_user_by_id(user_id)
                return True
            else:
                return False

        except Exception:
            return False


user_service = UserService.get_instance()
