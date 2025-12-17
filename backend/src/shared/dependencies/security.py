from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]
