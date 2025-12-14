"""Data validation schemas for inserts"""

from datetime import date

from pydantic import BaseModel


class AccidentCreate(BaseModel):
    person_id: int
    site_id: int
    accident_type_id: int
    injury_type_ids: list[int]
    description: str
    date_occurred: date


class PersonCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    role_id: int
    site_id: int


class RoleCreate(BaseModel):
    name: str


class SiteCreate(BaseModel):
    name: str
