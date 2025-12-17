import uuid
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...shared.utils.base import table_registry

if TYPE_CHECKING:
    from ..accounts.model import Account


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        init=False, default_factory=uuid.uuid4, primary_key=True
    )
    firstname: Mapped[str]
    lastname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    google_id: Mapped[str | None] = mapped_column(nullable=True)
    password: Mapped[str | None] = mapped_column(nullable=True, default=None)
    accounts: Mapped[list["Account"]] = relationship(back_populates="user", init=False)
