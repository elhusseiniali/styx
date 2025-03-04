from sqlalchemy import Column, ForeignKey, Table

from .base import BaseModel

# Association Table for many to many relationship
# between Exercise and Exercise type
exercise_type_association_table = Table(
    "exercise_type_association_table",
    BaseModel.metadata,
    Column("exercise_id", ForeignKey("exercise.id"), primary_key=True),
    Column("exercise_type_id", ForeignKey("exercise_type.id"),
    primary_key=True)
)

# Association Table for many to many relationship
# between Exercise and Muscle Group
muscle_group_association_table = Table(
    "muscle_group_association_table",
    BaseModel.metadata,
    Column("exercise_id", ForeignKey("exercise.id"), primary_key=True),
    Column("muscle_group_id", ForeignKey("muscle_group.id"), primary_key=True)
)
