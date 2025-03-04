from uuid import UUID

from sqlalchemy import CheckConstraint, ForeignKey, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    validates,
)

from styx.models.core.set_type import SetType

from ..base import BaseModel


class PlannedSet(BaseModel):
    __tablename__ = "planned_set"

    # Foreign Key
    set_type_id: Mapped[UUID] = mapped_column(ForeignKey("set_type.id"))

    min_rep_range: Mapped[int] = mapped_column(Integer)
    max_rep_range: Mapped[int] = mapped_column(Integer)

    # No need to reference and create a field in Set Type.
    # It can stay unidirectional for now (no need for backpopulates). 
    set_type: Mapped["SetType"] = relationship()

    # Note: defining validators in the database layer (using CheckConstraint), 
    # and in the application layer (@validates decorator) is a bit redundant, 
    # but for now it is fine.
    __table_args__ = (
        CheckConstraint("min_rep_range > 0", name="check_min_rep_positive"),
        CheckConstraint("max_rep_range > 0", name="check_max_rep_positive"),
        CheckConstraint("max_rep_range >= min_rep_range",
                        name="check_max_greater_than_min_rep")
    )
    

    # For reference check: https://docs.sqlalchemy.org/en/20/orm/mapped_attributes.html#simple-validators
    @validates("min_rep_range")
    def validate_min_rep_range(self, key, range):
        if (range < 0):
            raise ValueError("minimum range can't be negative.")
        if self.max_rep_range is not None and range > self.max_rep_range:
            raise ValueError("minimum range can't be " + \
                             "greater than maximum range.")

        return range

    @validates("max_rep_range")
    def validate_max_rep_range(self, key, range):
        if (range < 0):
            raise ValueError("maximum range can't be negative.")
        if self.min_rep_range is not None and range < self.min_rep_range:
            raise ValueError("maximum range can't be less than minimum range.")

        return range
    

    def __repr__(self) -> str:
        """Return a string representation of the PlannedSet instance.

        Returns:
            str: A string showing the set type's name, minimum and maximum
                    repetition range.

        """
        return (
            f"PlannedSet(set_type={self.set_type.name}, "
            f"min_rep_range={self.min_rep_range}, "
            f"max_rep_range={self.max_rep_range})"
        )
