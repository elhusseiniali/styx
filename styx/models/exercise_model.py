from sqlalchemy import List, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import BaseModel
from .exercise_type_model import ExerciseType
from .muscle_group_model import MuscleGroup
from .relationships import (
    exercise_type_association_table,
    muscle_group_association_table,
)


class Exercise(BaseModel): 
    __tablename__: str = "exercise"

    name: Mapped[str] = mapped_column(String(120), unique=True)

    # many to many relationship with Exercise Type table
    exercise_types: Mapped[List["ExerciseType"]] = relationship(
        "ExerciseType",
        secondary=exercise_type_association_table,
        back_populates="exercises",
    )

    # many to many relationship with Muscle Group table
    muscle_groups: Mapped[List["MuscleGroup"]] = relationship(
        "MuscleGroup",
        secondary=muscle_group_association_table,
        back_populates="exercises",
    )


    def __repr__(self) -> str:
        return f"Exercise( \
                            name={self.name}, \
                            types={self.exercise_types}, \
                            muscle_groups={self.muscle_groups} \
                         )"
