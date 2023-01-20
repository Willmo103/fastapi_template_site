from app import models, utils
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status, HTTPException, Depends, APIRouter, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.oauth2 import get_current_user
from pathlib import Path

router = APIRouter(
    prefix='/users',
    tags=['users']
)

BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / 'templates'))

@router.get('/', response_class=HTMLResponse)
def get_user(
        req: Request,
        db: Session = Depends(get_db),
        current_user: int = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if user is None:
       return templates.TemplateResponse("404.html", {"request": req})
    return templates.TemplateResponse("user.html", {"request": req, "user": user })


@router.put('/{id}', response_class=HTMLResponse)
def update_user(req: Request,
                id: int,
                db: Session = Depends(get_db),
                current_user: int = Depends(get_current_user)
                ):

    user_data = req.form()
    # TODO: get form data into a user object

    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()

    if user is None:
        return templates.TemplateResponse("404.html", {"request": req})

    if id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Unauthorized to update user other than current user')

    duplicate_check = db.query(models.User).filter(models.User.email == user_data.email).first()

    if duplicate_check is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'User with email {user_data.email} already exists')


    new_password = utils.password_hash(user_data.password)
    user_data['password'] = new_password
    user_query.update(user_data.dict(), synchronize_session=False)
    db.commit()

    return templates.TemplateResponse("update.html", {"request": req})


@router.post('/', status_code=status.HTTP_201_CREATED, response_class=HTMLResponse)
def create_new_user(req: Request, db: Session = Depends(get_db)):
    user = req.form()
    # TODO: get form data into a user object
    # check first if the user exists
    exists = db.query(models.User).filter(models.User.email == user.email).first()

    if exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Account already exists.'
        )

    # create a hashed version of the user's password before saving it.
    hashed_password = utils.password_hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.delete('/')
def delete_user(
        req: Request,
        db: Session = Depends(get_db),
        current_user: int = Depends(get_current_user)):
    user_query = db.query(models.User).filter(models.User.id == current_user.id)
    user = user_query.first()

    if user is None:
         return templates.TemplateResponse("404.html", {"request": req})

    user_query.delete(synchronize_session=False)
    db.commit()

    return templates.TemplateResponse("deleted.html", {"request", req})
