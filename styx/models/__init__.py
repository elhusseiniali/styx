from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from ..extensions import db


class BaseModel(db.Model): # type: ignore
    """Base model class that can be used by all models."""

    __abstract__ = True
    # Common columns that should be in all models
    
    # Use UUID instead of sequential ids for security issues that may arise
    # read more here: https://www.pingcap.com/article/the-benefits-of-using-uuids-for-unique-identification/.
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,  # Auto-generate UUIDs for new records.
    )

    created_on: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),  # generates the current
                                    # timestamp on insert.
    )

    updated_on: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),  # generates the current 
                                    # timestamp on insert.
        onupdate=func.now(),  # updated on row update.
    )
