from sqlalchemy import List, Optional, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import BaseModel
from .exercise_model import Exercise
from .relationships import exercise_type_association_table


class ExerciseType(BaseModel):
    __tablename__: str = "exercise_type"

    name: Mapped[str] = mapped_column(String(120), unique=True)

    # many to many field with Exercise table
    exercises: Mapped[Optional[List[Exercise]]] = relationship(
        "Exercise",
        secondary=exercise_type_association_table,
        back_populates="exercise_types",
        cascade="save-update, merge",
    )


    def __repr__(self) -> str:
        return f"ExerciseType(name={self.name})"
    