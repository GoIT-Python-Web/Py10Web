from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class OwnerModel(BaseModel):
    email: EmailStr


class OwnerResponse(BaseModel):
    id: int = 1
    email: EmailStr

    class Config:
        orm_mode = True


class CatModel(BaseModel):
    nick: str = Field('Barsik', min_length=3, max_length=16)
    age: int = Field(1, ge=1, le=30)
    vaccinated: Optional[bool] = False
    description: str
    owner_id: int = Field(1, gt=0)  # ge >=  gt >


class CatVaccinatedModel(BaseModel):
    vaccinated: bool = False


class CatResponse(BaseModel):
    id: int = 1
    nick: str = 'Barsik'
    age: int = 12
    vaccinated: bool = False
    description: str
    owner: OwnerResponse

    class Config:
        orm_mode = True
