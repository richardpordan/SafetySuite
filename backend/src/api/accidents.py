"""Accidents API endpoint"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from src.api.db_utils import get_db
from src.db.models.accident import Accident
from src.db.models.accident_injury import AccidentInjury
from src.schemas.create import AccidentCreate
from src.schemas.response import AccidentResponse

router = APIRouter()


@router.get(
    "/",
    response_model=list[AccidentResponse],
    status_code=status.HTTP_200_OK,
)
def list_accidents(db: Session = Depends(get_db)):
    return db.query(Accident).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_accident(accident: AccidentCreate, db: Session = Depends(get_db)):
    record = Accident(
        person_id=accident.person_id,
        site_id=accident.site_id,
        accident_type_id=accident.accident_type_id,
        description=accident.description,
        date_occurred=accident.date_occurred,
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    # add injuries
    for injury_id in accident.injury_type_ids:
        db.add(
            AccidentInjury(
                accident_id=record.id,
                injury_type_id=injury_id,
            )
        )

    db.commit()

    return {"status": "ok", "accident_id": record.id}


@router.delete("/{accident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_accident(accident_id: int, db: Session = Depends(get_db)):
    record = db.query(Accident).filter(Accident.id == accident_id).first()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Accident with id {accident_id} not found",
        )

    db.delete(record)
    db.commit()

    return {"status": "ok", "accident_id": record.id}
