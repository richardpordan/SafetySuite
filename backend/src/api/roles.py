"""Roles API endpoint"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from src.api.db_utils import get_db
from src.db.models.role import Role
from src.schemas.create import RoleCreate
from src.schemas.response import RoleResponse

router = APIRouter()


@router.get(
    "/",
    response_model=list[RoleResponse],
    status_code=status.HTTP_200_OK,
)
def list_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    record = Role(name=role.name)

    db.add(record)
    db.commit()
    db.refresh(record)

    return {"status": "ok", "role_id": record.id}


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    record = db.query(Role).filter(Role.id == role_id).first()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Record with id {role_id} not found",
        )

    db.delete(record)
    db.commit()

    return {"status": "ok", "role_id": record.id}
