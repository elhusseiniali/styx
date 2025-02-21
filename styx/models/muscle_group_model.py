from sqlalchemy import List, Optional, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import BaseModel
from .exercise_model import Exercise
from .relationships import muscle_group_association_table


class MuscleGroup(BaseModel):
    __tablename__: str = "muscle_group"

    name: Mapped[str] = mapped_column(String(120), unique=True)

    # many to many field with Exercise table
    exercises: Mapped[Optional[List[Exercise]]] = relationship(
        "Exercise",
        secondary=muscle_group_association_table,
        back_populates="muscle_groups",
        cascade="save-update, merge",
    )


    def __repr__(self) -> str:
        return f"MuscleGroup(name={self.name})"
