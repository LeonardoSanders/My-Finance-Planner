from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from ...shared.dependencies.database import Session
from ..users.model import User
from .model import Account
from .schema import AccountCreate, AccountPublic

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("/create", status_code=HTTPStatus.CREATED, response_model=AccountPublic)
async def create_account(account_data: AccountCreate, user: User, session: Session):
    data = account_data.model_dump()

    account = Account(**data, user_id=user.id)

    session.add(account)
    await session.commit()
    await session.refresh(account)

    return account
