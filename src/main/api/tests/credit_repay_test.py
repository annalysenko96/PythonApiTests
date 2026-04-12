import pytest
from sqlalchemy.orm import Session
from main.api.classes.api_manager import ApiManager
from main.api.db.crud.credit_crud import CreditCrudDb as Credit
from main.api.specs.response_specs import ResponseSpecs
from main.api.models.credit_repay_request import CreditRepayRequest




class TestCreditRepay:
    @pytest.mark.parametrize("active_credit", [5000, 5000.1, 7500, 14999.9, 15000], indirect=True)
    def test_credit_user_valid(self,
            db_session: Session,
            api_manager: ApiManager,
            user_credit_login:dict,
            active_credit:float,
            repay_request:CreditRepayRequest):
        result = api_manager.credit_repay_steps(user_credit_login).credit_repay(
            repay_request,ResponseSpecs.request_ok()
        )
        credit_from_db = Credit.get_credit_by_id(db_session, repay_request.creditId)
        assert credit_from_db.id == result.creditId
        assert credit_from_db.balance == 0
        assert result.amountDeposited == repay_request.amount



    @pytest.mark.parametrize("repay_request", [-10, 0],indirect=True)
    @pytest.mark.parametrize("active_credit", [15000], indirect=True)
    def test_credit_repay_invalid(self,
            db_session: Session,
            api_manager: ApiManager,
            user_credit_login:dict,
            active_credit:float,
            repay_request:CreditRepayRequest):
        result = api_manager.credit_repay_steps(user_credit_login).credit_repay(
            repay_request,ResponseSpecs.request_bad()
        )
        credit_from_db = Credit.get_credit_by_id(db_session, repay_request.creditId)
        assert credit_from_db.balance == -15000



    @pytest.mark.parametrize("repay_request", [4999.9, 15000.1],indirect=True)
    @pytest.mark.parametrize("active_credit", [15000], indirect=True)
    def test_credit_repay_invalid_r(self,
            db_session: Session,
            api_manager: ApiManager,
            user_credit_login:dict,
            active_credit:float,
            repay_request:CreditRepayRequest):
        result = api_manager.credit_repay_steps(user_credit_login).credit_repay(
            repay_request,ResponseSpecs.request_unprocessable_entity()
        )
        credit_from_db = Credit.get_credit_by_id(db_session, repay_request.creditId)
        assert credit_from_db.balance == -15000










