import decimal

from pydantic import BaseModel, ConfigDict, model_validator

from src.modules.accounts.model import AccountType


class AccountCreate(BaseModel):
    name: str
    account_type: AccountType
    balance: decimal.Decimal
    closing_day: int | None = None
    due_day: int | None = None

    @model_validator(mode="after")
    def validate_credit(self):
        if self.account_type is None:
            return self

        if self.account_type == AccountType.credit and (
            self.closing_day is None or self.due_day is None
        ):
            raise ValueError("Credit must have either closing day and due day!")

        return self


class AccountPublic(BaseModel):
    id: int
    name: str
    account_type: AccountType
    balance: decimal.Decimal

    model_config = ConfigDict(from_attributes=True)
