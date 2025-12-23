from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from ...shared.dependencies.database import Session
from ...shared.dependencies.google_auth import GoogleUserClaims
from ...shared.security.schema import Token
from ...shared.security.token_jwt import create_access_token, verify_password
from ..users.model import User
from .dependencies import OAuthForm

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/google-login", status_code=HTTPStatus.OK, response_model=Token)
async def google_login(google_data: GoogleUserClaims, session: Session):
    email = google_data["email"]

    user = await session.scalar(select(User).where(User.email == email))

    if not user:
        user = await _create_user_from_token(google_data, session)

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "Bearer"}


async def _create_user_from_token(token_data, session: Session):
    user = User(
        firstname=token_data["given_name"],
        lastname=token_data.get("family_name", ""),
        email=token_data["email"],
        google_id=token_data.get("sub"),
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


@router.post("/token-login", status_code=HTTPStatus.OK, response_model=Token)
async def login_for_access_token(form_data: OAuthForm, session: Session):
    try:
        user_db = await session.scalar(
            select(User).where(User.email == form_data.username)
        )

        if user_db and user_db.password:
            if verify_password(form_data.password, user_db.password):
                access_token = create_access_token(data={"sub": user_db.email})

                return {"access_token": access_token, "token_type": "Bearer"}
    except:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail="Could not validate credentials"
        )
