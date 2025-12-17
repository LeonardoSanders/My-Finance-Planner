from typing import Annotated

from fastapi import Depends

from ...shared.dependencies.database import Session
from ...shared.dependencies.session_user import SessionUser
from .service import UserService


def get_service(user_login: SessionUser, session: Session):
    return UserService(user_login, session)


Service = Annotated[UserService, Depends(get_service)]
