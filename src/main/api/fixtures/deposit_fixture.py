import pytest

from main.api.models.deposit_request import DepositRequest


@pytest.fixture
def  prepared_deposit(request, api_manager, user_login):
    account = api_manager.account_steps(user_login).create_account()
    amount = request.param

    return DepositRequest(
        account_id=account.id,
        deposit=amount
    )

