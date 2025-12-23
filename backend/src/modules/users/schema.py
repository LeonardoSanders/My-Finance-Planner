from pydantic import BaseModel, EmailStr


class UserCreateContract(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    google_id: str


class UserCreateManualContract(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    google_id: str
    password: str


class UserResponseContract(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    google_id: str


class UserUpdateContract(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    google_id: str
    password: str
