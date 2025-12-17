import os
from http import HTTPStatus
from typing import Annotated, Any

from fastapi import Depends, HTTPException
from google.auth.transport import requests
from google.oauth2 import id_token

from .security import security

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


def get_google_user_data(auth: security) -> dict[str, Any]:

    try:
        id_info = id_token.verify_oauth2_token(
            auth.credentials, requests.Request(), GOOGLE_CLIENT_ID
        )
        return id_info
    except:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail="Not authenticated"
        )


GoogleUserClaims = Annotated[dict, Depends(get_google_user_data)]
