import pytest
from sqlalchemy.orm import Session
from main.api.classes.api_manager import ApiManager
from main.api.db.models.credit_table import Credit
from main.api.specs.response_specs import ResponseSpecs
from main.api.models.credit_repay_request import CreditRepayRequest



class TestCreditRepay:
    @pytest.mark.parametrize("active_credit", [5000, 5000.1, 7500, 14999.9, 15000], indirect=True)
    def test_credit_user_valid(self,db_session: Session, api_manager: ApiManager, user_credit_login:dict,active_credit:tuple):
        acc, credit = active_credit

        repay_data = CreditRepayRequest(
            creditId=credit.creditId,
            accountId=acc.id,
            amount=credit.amount
        )
        result = api_manager.credit_repay_steps(user_credit_login).credit_repay(
            repay_data,
            ResponseSpecs.request_ok()
        )
        credit_from_db = db_session.query(Credit).filter(Credit.id == credit.creditId).first()

        assert result.amountDeposited == credit.amount
        assert result.creditId == credit.creditId
        assert credit_from_db.balance == 0



    @pytest.mark.parametrize("repay_amount", [-10, 0])
    @pytest.mark.parametrize("active_credit", [15000], indirect=True)
    def test_credit_repay_invalid(self,db_session: Session, api_manager: ApiManager, user_credit_login:dict, repay_amount: float, active_credit:tuple):
        acc, credit = active_credit
        repay_data = CreditRepayRequest(
            creditId=credit.creditId,
            accountId=acc.id,
            amount=repay_amount
        )
        result = api_manager.credit_repay_steps(user_credit_login).credit_repay(
            repay_data,
            ResponseSpecs.request_bad()
        )
        credit_from_db = db_session.query(Credit).filter(Credit.id == credit.creditId).first()

        assert credit_from_db.balance == -15000


    @pytest.mark.parametrize("repay_amount", [4999.9, 15000.1])
    @pytest.mark.parametrize("active_credit", [15000], indirect=True)
    def test_credit_repay_invalid(self, db_session: Session, api_manager: ApiManager, user_credit_login: dict, repay_amount: float, active_credit: tuple):
        acc, credit = active_credit
        repay_data = CreditRepayRequest(
            creditId=credit.creditId,
            accountId=acc.id,
            amount=repay_amount
        )
        result = api_manager.credit_repay_steps(user_credit_login).credit_repay(
            repay_data,
            ResponseSpecs.request_unprocessable_entity()
        )
        credit_from_db = db_session.query(Credit).filter(Credit.id == credit.creditId).first()

        assert credit_from_db.balance == -15000










