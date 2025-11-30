from typing import Annotated

from fastapi import Depends

from backend.config.database.postgres import AsyncSession, get_session

Session = Annotated[AsyncSession, Depends(get_session)]
