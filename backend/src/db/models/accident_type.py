"""Accident types table"""

from sqlalchemy import Column, Integer, String

from src.db.models.base import Base


class AccidentType(Base):
    __tablename__ = "accident_types"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )

    name = Column(String, nullable=False)
