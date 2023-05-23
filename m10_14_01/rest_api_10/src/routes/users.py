from fastapi import APIRouter, Depends, status, UploadFile, File, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User
from src.repository import users as repository_users
from src.services.auth import auth_service
from src.services.upload_avatar import UploadService
from src.schemas import UserResponse

router = APIRouter(prefix="/users", tags=["users"])
templates = Jinja2Templates(directory='templates')


@router.get("/me/", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(auth_service.get_current_user)):
    return current_user


@router.get("/profile", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('test_form.html', {"request": request, "email": None, "text": None})


@router.post("/profile", response_class=HTMLResponse)
async def root(request: Request, email=Form(), text=Form()):
    print(email, text)
    return templates.TemplateResponse('test_form.html', {"request": request, "email": email, "text": text})


@router.patch('/avatar', response_model=UserResponse)
async def update_avatar_user(avatar: UploadFile = File(), current_user: User = Depends(auth_service.get_current_user),
                             db: Session = Depends(get_db)):
    """
    The update_avatar_user function updates the avatar of a user.

    :param avatar: UploadFile: Receive the file from the client
    :param current_user: User: Get the current user
    :param db: Session: Access the database
    :return: The updated user
    """
    public_id = UploadService.create_name_avatar(current_user.email, 'web10')

    r = UploadService.upload(avatar.file, public_id)

    src_url = UploadService.get_url_avatar(public_id, r.get('version'))
    user = await repository_users.update_avatar(current_user.email, src_url, db)
    return user
