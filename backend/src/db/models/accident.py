"""Accidents table"""

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship

from src.db.models.base import Base


class Accident(Base):
    __tablename__ = "accidents"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )

    person_id = Column(Integer, ForeignKey("persons.id"))
    site_id = Column(Integer, ForeignKey("sites.id"))
    accident_type_id = Column(Integer, ForeignKey("accident_types.id"))
    person = relationship("Person")
    site = relationship("Site")
    accident_type = relationship("AccidentType")
    injuries = relationship("AccidentInjury", cascade="all, delete-orphan")

    description = Column(String)
    date_occurred = Column(Date, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
