"""API core components"""

from src.db.session import Session


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
