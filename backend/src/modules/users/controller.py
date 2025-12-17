from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from ...shared.security.token_jwt import get_password_hash

from ...modules.users.model import User

from ...shared.dependencies.database import Session

from ...shared.utils.exceptions import InvalidInputException
from .dependencies import Service
from .schema import UserCreateContract, UserCreateManualContract, UserResponseContract

router = APIRouter(prefix="/user", tags=["/user"])


@router.get("/me", status_code=HTTPStatus.OK, response_model=UserResponseContract)
def get_current_user(service: Service):
    return service.user


@router.patch(
    "/update_user", status_code=HTTPStatus.OK, response_model=UserCreateContract
)
async def update_user(user_data: UserCreateContract, service: Service):
    result = await service.update_user(user_data)

    return result


@router.post(
    "/create_user", status_code=HTTPStatus.CREATED, response_model=UserResponseContract
)
async def create_new_user(user_data: UserCreateManualContract, session: Session, service: Service):
    try:
        user = await service.verify_user(user_data.email)
        
        if not user:
            await service.create_user(user_data)

    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail=f"Could not create user {e}"
        )
