from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from src.database.models import Role


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


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=12)
    email: EmailStr
    password: str = Field(min_length=6, max_length=8)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    avatar: str
    role: Role

    class Config:
        orm_mode = True


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
