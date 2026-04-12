import pytest

from main.api.models.deposit_account_request import DepositAccountRequest
from main.api.models.transfer_account_request import TransferAccountRequest
from main.api.models.transfer_request import TransferRequestData
from main.api.specs.response_specs import ResponseSpecs


@pytest.fixture
def transfer_data(request,api_manager,user_login):
    acc_from = api_manager.account_steps(user_login).create_account()
    acc_to = api_manager.account_steps(user_login).create_account()
    api_manager.account_steps(user_login).create_account_deposit(
        DepositAccountRequest(accountId=acc_from.id, amount=9000),
        ResponseSpecs.request_ok()
    )
    api_manager.account_steps(user_login).create_account_deposit(
        DepositAccountRequest(accountId=acc_from.id, amount=9000),
        ResponseSpecs.request_ok()
    )
    api_payload = TransferAccountRequest(
        from_account_id=acc_from.id,
        to_account_id=acc_to.id,
        amount=request.param
    )

    test_data = TransferRequestData(
        request_data=api_payload,
        initial_balance=18000.0
    )
    return test_data