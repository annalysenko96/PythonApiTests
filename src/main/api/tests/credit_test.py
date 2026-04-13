import pytest
from sqlalchemy.orm import Session
from main.api.classes.api_manager import ApiManager
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.db.crud.credit_crud import  CreditCrudDb as Credit


class TestCreditUser:
    @pytest.mark.parametrize("amount", [5000, 5000.1, 7500, 14999.9, 15000])
    def test_credit_user_valid(self,db_session: Session, api_manager: ApiManager, user_credit_login:dict, amount:float):
        account_response = api_manager.account_steps(user_credit_login).create_account()
        result = api_manager.credit_steps(user_credit_login).credit_data(
            account_id = account_response.id,
            amount=amount,
            term_months = 12,
        )
        credit_from_db = Credit.get_credit_by_id(db_session, result.creditId)
        assert credit_from_db.id == result.creditId
        assert credit_from_db.amount == result.amount
        assert result.amount == amount


    @pytest.mark.parametrize("amount", [-1, 0, 4999.9, 15000.1])
    def test_credit_user_invalid(self,db_session: Session, api_manager: ApiManager, user_credit_login:dict, amount:float):
        account_response = api_manager.account_steps(user_credit_login).create_account()
        result = api_manager.credit_steps(user_credit_login).credit_data_indalid(
            account_id=account_response.id,
            amount=amount,
            term_months=12,
        )

        assert account_response.balance ==0






