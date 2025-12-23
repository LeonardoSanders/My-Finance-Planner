from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

OAuthForm = Annotated[OAuth2PasswordRequestForm, Depends()]
