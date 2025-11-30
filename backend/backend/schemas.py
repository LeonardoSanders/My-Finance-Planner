import uuid

from pydantic import BaseModel


class UserCreateContract(BaseModel):
    firstname: str | None = None
    lastname: str | None = None
    email: str | None = None
    google_id: str | None = None


class UserRespondeContract(BaseModel):
    id: uuid.UUID | None = None
    firstname: str | None = None
    lastname: str | None = None
    email: str | None = None
    google_id: str | None = None
