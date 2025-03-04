from sqlalchemy import String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column

from styx.extensions import bcrypt
from styx.models.base import BaseModel


class User(BaseModel): #type: ignore
    __tablename__: str = "user"

    username: Mapped[str] = mapped_column(String(120), unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    _password: Mapped[str] = mapped_column(String(128))

    @hybrid_property
    def password(self) -> str:
        return self._password

    @password.setter  # type: ignore
    def password(self, password: str) -> None:
        self._password = bcrypt.generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self._password, password)

    def __repr__(self) -> str:
        return f"User(username={self.username}, email={self.email})"
