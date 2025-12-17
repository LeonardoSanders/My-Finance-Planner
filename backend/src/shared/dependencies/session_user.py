from http import HTTPStatus
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select

from ...modules.users.model import User
from ..security.environments import ALGORITHM, SECRET_KEY
from .database import Session

oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/token-login")

OAuth2 = Annotated[str, Depends(oauth2_schema)]

credentials_exception = HTTPException(
    status_code=HTTPStatus.UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


async def get_session_user(
    token: OAuth2,
    session: Session,
):
    user_email = get_token_credentials(token)

    user = await session.scalar(select(User).where(User.email == user_email))

    if not user:
        raise credentials_exception

    return user


def get_token_credentials(token: OAuth2):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        subject_email = payload.get("sub")
        if not subject_email:
            raise credentials_exception

    except jwt.DecodeError:
        raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise credentials_exception

    return subject_email


SessionUser = Annotated[User, Depends(get_session_user)]
