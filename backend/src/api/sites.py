"""Accidents API endpoint"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from src.api.db_utils import get_db
from src.db.models.site import Site
from src.schemas.create import SiteCreate
from src.schemas.response import SiteResponse

router = APIRouter()


@router.get(
    "/",
    response_model=list[SiteResponse],
    status_code=status.HTTP_200_OK,
)
def list_sites(db: Session = Depends(get_db)):
    return db.query(Site).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_role(site: SiteCreate, db: Session = Depends(get_db)):
    record = Site(name=site.name)

    db.add(record)
    db.commit()
    db.refresh(record)

    return {"status": "ok", "site_id": record.id}


@router.delete("/{site_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(site_id: int, db: Session = Depends(get_db)):
    record = db.query(Site).filter(Site.id == site_id).first()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Record with id {site_id} not found",
        )

    db.delete(record)
    db.commit()

    return {"status": "ok", "site_id": record.id}
