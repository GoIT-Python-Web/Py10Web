from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import Owner, User, Role
from src.schemas import OwnerResponse, OwnerModel
from src.repository import owners as repository_owners
from src.services.auth import auth_service
from src.services.roles import RolesAccess

router = APIRouter(prefix="/owners", tags=["owners"])

access_get = RolesAccess([Role.admin, Role.moderator, Role.user])
access_create = RolesAccess([Role.admin, Role.moderator])
access_update = RolesAccess([Role.admin, Role.moderator])
access_delete = RolesAccess([Role.admin])


@router.get("/", response_model=List[OwnerResponse], dependencies=[Depends(access_get)])
async def get_owners(db: Session = Depends(get_db), _: User = Depends(auth_service.get_current_user)):
    owners = await repository_owners.get_owners(db)
    return owners


@router.get("/{owner_id}", response_model=OwnerResponse, dependencies=[Depends(access_get)])
async def get_owner(owner_id: int = Path(ge=1), db: Session = Depends(get_db),
                    _: User = Depends(auth_service.get_current_user)):
    owner = await repository_owners.get_owner_by_id(owner_id, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return owner


@router.post("/", response_model=OwnerResponse, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(access_create)])
async def create_owner(body: OwnerModel, db: Session = Depends(get_db),
                       _: User = Depends(auth_service.get_current_user)):
    owner = await repository_owners.get_owner_by_email(body.email, db)
    if owner:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is exists!")
    owner = await repository_owners.create(body, db)
    return owner


@router.put("/{owner_id}", response_model=OwnerResponse, dependencies=[Depends(access_update)])
async def update_owner(body: OwnerModel, owner_id: int = Path(ge=1), db: Session = Depends(get_db),
                       _: User = Depends(auth_service.get_current_user)):
    owner = await repository_owners.update(owner_id, body, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return owner


@router.delete("/{owner_id}", response_model=OwnerResponse, dependencies=[Depends(access_delete)])
async def delete_owner(owner_id: int = Path(ge=1), db: Session = Depends(get_db),
                       _: User = Depends(auth_service.get_current_user)):
    owner = await repository_owners.remove(owner_id, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return owner
