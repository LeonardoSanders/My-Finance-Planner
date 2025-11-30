from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select

from backend.dependencies import Session
from backend.models import User
from backend.schemas import UserCreateContract, UserRespondeContract

router = APIRouter(prefix="/login", tags=["login"])


@router.post(
    "/signin", status_code=HTTPStatus.CREATED, response_model=UserRespondeContract
)
async def login(user: UserCreateContract, session: Session):
    user_db = await session.scalar(
        select(User).where(User.firstname == user.firstname)
    )
    if not user_db:
        user_db = await _create_user(user, session)

    return user_db


async def _create_user(user, session: Session):
    user_creation = User(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        google_id=user.google_id,
    )

    session.add(user_creation)
    await session.commit()
    await session.refresh(user_creation)

    return user_creation
