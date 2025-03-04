from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import BaseModel
from ..relationships import muscle_group_association_table
from .exercise import Exercise

if TYPE_CHECKING:
    from .exercise import Exercise


class MuscleGroup(BaseModel):
    __tablename__: str = "muscle_group"

    name: Mapped[str] = mapped_column(String(120), unique=True)

    # many to many field with Exercise table
    exercises: Mapped[list["Exercise"] | None] = relationship(
        "Exercise",
        secondary=muscle_group_association_table,
        back_populates="muscle_groups",
        cascade="save-update, merge",
    )


    def __repr__(self) -> str:
        return f"MuscleGroup(name={self.name})"
