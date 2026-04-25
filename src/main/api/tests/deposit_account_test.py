import pytest
from sqlalchemy.orm import Session


from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.db.crud.deposit_crud import DepositCrud



@pytest.mark.api
class TestAccountDeposit:
    @pytest.mark.parametrize ("prepared_deposit", [1000,1000.1,5555,8999.9,9000],indirect=True)
    def test_deposit_account_valid(self,
        db_session:Session,
        api_manager:ApiManager,
        user_login:dict,
        prepared_deposit:DepositRequest):
        result = api_manager.account_steps(user_login).create_account_deposit(
            prepared_deposit,
        )

        deposit_from_db = DepositCrud.get_deposit_by_account_id(db_session,prepared_deposit.account_id)

        assert result.balance == prepared_deposit.deposit
        assert deposit_from_db.balance == prepared_deposit.deposit
        assert deposit_from_db is not None, "Транзакция не найдена в базе"


    @pytest.mark.parametrize("prepared_deposit", [-10, 0, 999.9, 9000.1],indirect=True)
    def test_deposit_account_invalid(self,db_session:Session,
        api_manager:ApiManager,
        user_login:dict,
        prepared_deposit:DepositRequest):
        result = api_manager.account_steps(user_login).create_account_deposit_invalid(
            prepared_deposit,
        )
        deposit_from_db = DepositCrud.get_deposit_by_account_id(db_session, prepared_deposit.account_id)

        assert deposit_from_db.balance == 0, f"Баланс изменился на {deposit_from_db.balance}"








