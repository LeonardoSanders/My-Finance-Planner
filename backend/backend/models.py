import uuid

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    id: Mapped[uuid.UUID] = mapped_column(
        init=False, default_factory=uuid.uuid4, primary_key=True
    )
    firstname: Mapped[str]
    lastname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    google_id: str
