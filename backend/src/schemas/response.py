"""Data validation schemas for responses"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class AccidentTypeResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class InjuryTypeResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class AccidentInjuryResponse(BaseModel):
    accident_id: int
    injury_type_id: int

    model_config = ConfigDict(from_attributes=True)


class RoleResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class SiteResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class PersonResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str | None
    phone: str | None
    role: RoleResponse
    site: SiteResponse
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class AccidentResponse(BaseModel):
    id: int
    person: PersonResponse
    site: SiteResponse
    accident_type: AccidentTypeResponse
    injuries: list[AccidentInjuryResponse]
    description: str
    date_occurred: date
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
