from typing import Annotated

from fastapi import Depends

from ...shared.dependencies.database import Session
from .service import UserService


def get_service(session: Session):
    return UserService(session)


Service = Annotated[UserService, Depends(get_service)]
