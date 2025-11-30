import uuid

from pydantic import BaseModel


class UserContract(BaseModel):
    id: uuid.UUID | None = None
    firstname: str | None = None
    lastname: str | None = None
    email: str | None = None
    google_id: str | None = None
