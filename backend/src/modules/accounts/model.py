import uuid
from decimal import Decimal
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...shared.utils.base import table_registry

if TYPE_CHECKING:
    from ..users.model import User


class AccountType(str, Enum):
    checking = "CHECKING"
    savings = "SAVINGS"
    credit = "CREDIT"


@table_registry.mapped_as_dataclass
class Account:
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str]
    account_type: Mapped[AccountType]
    balance: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    closing_day: Mapped[int | None] = mapped_column(nullable=True)
    due_day: Mapped[int | None] = mapped_column(nullable=True)
    user: Mapped["User"] = relationship(back_populates="accounts")
    __table_args__ = (
        CheckConstraint(
            "(account_type::text = 'CREDIT' AND closing_day IS NOT NULL AND due_day "
            "IS NOT NULL) OR (account_type::text != 'CREDIT')",
            name="check_credit_card_dates",
        ),
    )
