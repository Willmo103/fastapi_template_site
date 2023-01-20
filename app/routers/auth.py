from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app import database, schemas, models, utils, oauth2

router = APIRouter(
    prefix='/login',
    tags=['authentication']
)


@router.post('/', response_model=schemas.Token)
def login(user_credentials: schemas.UserLogin,
          db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(
        models.User.email == user_credentials.email).first()
    # print(user)

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='invalid Credentials')

    if not utils.password_verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='invalid Credentials')

    access_token = oauth2.create_access_token(data={'user_id': user.id})

    return {'access_token': access_token, 'token_type': 'bearer'}
