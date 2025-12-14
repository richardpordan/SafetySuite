"""Persons API endpoint"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from src.api.db_utils import get_db
from src.db.models.person import Person
from src.schemas.create import PersonCreate
from src.schemas.response import PersonResponse

router = APIRouter()


@router.get(
    "/",
    response_model=list[PersonResponse],
    status_code=status.HTTP_200_OK,
)
def list_persons(db: Session = Depends(get_db)):
    return db.query(Person).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    record = Person(
        first_name=person.first_name,
        last_name=person.last_name,
        email=person.email,
        phone=person.phone,
        role_id=person.role_id,
        site_id=person.site_id,
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {"status": "ok", "person_id": record.id}


@router.delete("/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(person_id: int, db: Session = Depends(get_db)):
    record = db.query(Person).filter(Person.id == person_id).first()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id {person_id} not found",
        )

    db.delete(record)
    db.commit()

    return {"status": "ok", "person_id": record.id}
