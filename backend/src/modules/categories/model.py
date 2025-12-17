import uuid
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from ...shared.utils.base import table_registry


@table_registry.mapped_as_dataclass
class Category:
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str]
    budget_percentage: Mapped[Decimal] = mapped_column(Numeric(5, 2))
    color: Mapped[str]
