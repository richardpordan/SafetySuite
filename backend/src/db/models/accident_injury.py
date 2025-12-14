"""Accident-injury linking table"""

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.db.models.base import Base


class AccidentInjury(Base):
    __tablename__ = "accident_injuries"

    accident_id = Column(
        Integer,
        ForeignKey("accidents.id", ondelete="CASCADE"),
        primary_key=True,
    )
    injury_type_id = Column(
        Integer,
        ForeignKey("injury_types.id"),
        primary_key=True,
    )
    injury_type = relationship("InjuryType")
