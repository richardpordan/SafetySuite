"""Accident types API endpoint"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.api.db_utils import get_db
from src.db.models.accident_type import AccidentType
from src.schemas.response import AccidentTypeResponse

router = APIRouter()


@router.get(
    "/",
    response_model=list[AccidentTypeResponse],
    status_code=status.HTTP_200_OK,
)
def list_accident_types(db: Session = Depends(get_db)):
    return db.query(AccidentType).all()
