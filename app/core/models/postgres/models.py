"""
Sql alchemy entities module.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id_: ...

    def to_dict(self) -> dict: ...
