from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from ...shared.dependencies.session_user import SessionUser
from ...shared.utils.exceptions import UnauthorizedException
from .dependencies import Service
from .schema import UserCreateManualContract, UserResponseContract, UserUpdateContract

router = APIRouter(prefix="/user", tags=["/user"])


@router.get("/me", status_code=HTTPStatus.OK, response_model=UserResponseContract)
def get_current_user(session_user: SessionUser):
    return session_user


@router.patch(
    "/update-user", status_code=HTTPStatus.OK, response_model=UserResponseContract
)
async def update_user(
    user_data: UserUpdateContract, service: Service, session_user: SessionUser
):
    try:
        result = await service.update_user(session_user, user_data)

        return result

    except UnauthorizedException:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail="Cannot modify other user"
        )

    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail=f"Could not update user {e}"
        )


@router.post(
    "/create-user", status_code=HTTPStatus.CREATED, response_model=UserResponseContract
)
async def create_new_user(user_data: UserCreateManualContract, service: Service):
    try:
        user = await service.verify_user_by_email(user_data.email)

        if not user:
            created_user = await service.create_user(user_data)

            return created_user

    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail=f"Could not create user {e}"
        )
