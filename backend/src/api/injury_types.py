"""Injury types API endpoint"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.api.db_utils import get_db
from src.db.models.injury_type import InjuryType
from src.schemas.response import InjuryTypeResponse

router = APIRouter()


@router.get(
    "/",
    response_model=list[InjuryTypeResponse],
    status_code=status.HTTP_200_OK,
)
def list_injury_types(db: Session = Depends(get_db)):
    return db.query(InjuryType).all()
