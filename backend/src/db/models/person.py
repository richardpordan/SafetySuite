"""Persons table"""

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship

from src.db.models.base import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)

    role_id = Column(Integer, ForeignKey("roles.id"))
    site_id = Column(Integer, ForeignKey("sites.id"))
    role = relationship("Role")
    site = relationship("Site")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
