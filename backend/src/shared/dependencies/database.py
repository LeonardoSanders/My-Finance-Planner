from typing import Annotated

from fastapi import Depends

from src.config.database.postgres import AsyncSession, get_session

Session = Annotated[AsyncSession, Depends(get_session)]
