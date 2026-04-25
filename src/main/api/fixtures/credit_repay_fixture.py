import pytest

from src.main.api.models.credit_repay_request import CreditRepayRequest


@pytest.fixture
def active_credit(request, api_manager, user_credit_login):
    amount = request.param

    acc = api_manager.account_steps(user_credit_login).create_account()
    credit = api_manager.credit_steps(user_credit_login).credit_data(
        account_id=acc.id,
        amount=amount,
        term_months=12
    )
    return acc, credit

@pytest.fixture
def repay_request (request, active_credit):
    acc, credit = active_credit
    amount = getattr(request, "param", credit.amount)

    repay_data = CreditRepayRequest(
        creditId=credit.creditId,
        accountId=acc.id,
        amount=amount
    )
    return repay_data