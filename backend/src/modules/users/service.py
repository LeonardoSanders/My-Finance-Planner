from sqlalchemy import select

from ...shared.dependencies.database import Session
from ...shared.security.token_jwt import get_password_hash
from ...shared.utils.exceptions import InvalidInputException
from .model import User
from .schema import UserCreateContract, UserCreateManualContract


class UserService:
    def __init__(self, user: User, session: Session):
        self.user = user
        self.session = session

    async def verify_user(self, email):
        user = self.session.scalar(select(User).where(User.email == email))

        return user

    async def update_user(self, data: UserCreateContract) -> User:
        updated_user = data.model_dump(exclude_unset=True)

        for key, value in updated_user.items():
            setattr(self.user, key, value)

        self.session.add(self.user)
        await self.session.commit()
        await self.session.refresh(self.user)

        return self.user

    async def create_user(self, data: UserCreateManualContract) -> User:
        if await self.session.scalar(select(User).where(User.email == data.email)):
            raise InvalidInputException()

        new_user = User(
            firstname=data.firstname,
            lastname=data.lastname,
            email=data.email,
            google_id=data.google_id,
            password=get_password_hash(data.password),
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user
