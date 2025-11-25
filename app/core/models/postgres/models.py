"""
Sql alchemy entities module.
"""

from uuid import UUID
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import DateTime, Boolean, text


class Base(DeclarativeBase):
    id_: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuidv7()"),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('UTC', now())"),
    )
    # Add triggers on update updated_at for each entity.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('UTC', now())"),
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_dict(self) -> dict: ...
