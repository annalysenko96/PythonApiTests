from pydantic import Field

from src.main.api.models.base_model import BaseModel


class DepositRequest(BaseModel):
    account_id: int = Field(alias="accountId")
    deposit: float = Field(alias="amount")

    model_config = {"populate_by_name": True}