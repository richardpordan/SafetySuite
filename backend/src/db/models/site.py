"""Sites table"""

from sqlalchemy import Column, Integer, String

from src.db.models.base import Base


class Site(Base):
    __tablename__ = "sites"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )
    name = Column(String, nullable=False)
