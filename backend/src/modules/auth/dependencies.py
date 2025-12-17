from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import Depends

OAuthForm = Annotated[ OAuth2PasswordRequestForm, Depends()]
