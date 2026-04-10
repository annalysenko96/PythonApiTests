import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.specs.response_specs import ResponseSpecs
from main.api.db.crud.deposit_crud import DepositCrud



@pytest.mark.api
class TestAccountDeposit:
    @pytest.mark.parametrize ("amount", [1000,1000.1,5555,8999.9,9000])
    def test_deposit_account_valid(self,db_session:Session, api_manager:ApiManager, user_login:dict, amount:float):
        account = api_manager.account_steps(user_login).create_account()
        deposit_data = DepositAccountRequest(accountId=account.id, amount=amount)
        result = api_manager.account_steps(user_login).create_account_deposit(
            deposit_data,
            ResponseSpecs.request_ok()
        )
        deposit_from_db = DepositCrud.get_deposit_by_account_id(db_session,account.id)

        assert result.balance == amount
        assert deposit_from_db.balance == amount
        assert deposit_from_db is not None, "Транзакция не найдена в базе"


    @pytest.mark.parametrize("amount", [-10, 0, 999.9, 9000.1])
    def test_deposit_account_invalid(self,db_session:Session, api_manager:ApiManager, user_login:dict, amount:float):
        account = api_manager.account_steps(user_login).create_account()
        deposit_data = DepositAccountRequest(accountId=account.id, amount=amount)
        result = api_manager.account_steps(user_login).create_account_deposit(
            deposit_data,
            ResponseSpecs.request_bad()
        )
        deposit_from_db = DepositCrud.get_deposit_by_account_id(db_session,account.id)
        assert deposit_from_db.balance == 0, f"Баланс изменился на {deposit_from_db.balance}"








