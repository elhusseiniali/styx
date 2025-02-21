from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from . import BaseModel


class SetType(BaseModel):
    __tablename__ = "set_type"
    
    name: Mapped[str] = mapped_column(String(120), unique=True)


    def __repr__(self) -> str:
        """Return a string representation of the SetType instance.

        Returns:
            str: A string showing the set type's name.

        """
        return f"SetType(name={self.name})"
