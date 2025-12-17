import datetime
import uuid
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...shared.utils.base import table_registry

if TYPE_CHECKING:
    from ..accounts.model import Account
    from ..categories.model import Category
    from ..users.model import User


@table_registry.mapped_as_dataclass
class Transaction:
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    description: Mapped[str] = mapped_column(String(100))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    date: Mapped[datetime.date] = mapped_column(Date)
    transaction_group_id: Mapped[uuid.UUID | None] = mapped_column(nullable=True)
    installment_number: Mapped[int] = mapped_column(default=1)
    total_installments: Mapped[int] = mapped_column(default=1)
    paid: Mapped[bool] = mapped_column(default=True)
    user: Mapped["User"] = relationship(init=False)
    account: Mapped["Account"] = relationship(init=False)
    category: Mapped["Category"] = relationship(init=False)
