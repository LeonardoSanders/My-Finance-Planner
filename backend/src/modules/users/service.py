from sqlalchemy import select

from ...shared.dependencies.database import Session
from ...shared.security.token_jwt import get_password_hash
from ...shared.utils.exceptions import UnauthorizedException
from .model import User
from .schema import UserCreateManualContract, UserUpdateContract


class UserService:
    def __init__(self, session: Session):
        self.session = session

    async def verify_user_by_email(self, email):
        user = self.session.scalar(select(User).where(User.email == email))

        return user

    async def update_user(self, user: User, data: UserUpdateContract):
        updated_user = data.model_dump(exclude_unset=True)

        if user.email != data.email:
            if self.verify_user_by_email(data.email):
                raise UnauthorizedException()

        for key, value in updated_user.items():
            if key == "password":
                value = get_password_hash(value)
            setattr(user, key, value)

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def create_user(self, data: UserCreateManualContract) -> User:
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
