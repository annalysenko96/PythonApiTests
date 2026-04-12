from main.api.models.base_model import BaseModel
from main.api.models.transfer_account_request import TransferAccountRequest


class TransferRequestData(BaseModel):
    request_data:TransferAccountRequest
    initial_balance: float = 9000.0

    model_config = {"populate_by_name": True}
