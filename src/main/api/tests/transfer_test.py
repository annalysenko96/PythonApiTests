import pytest
from sqlalchemy.orm import Session

from main.api.classes.api_manager import ApiManager
from main.api.db.crud.deposit_crud import DepositCrud
from main.api.fixtures.u_login_fixture import user_login
from main.api.models.transfer_request import TransferRequestData
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction

@pytest.mark.api
class TestTransfer:
    @pytest.mark.parametrize("transfer_data", [500, 500.1, 9999.9, 10000],indirect=True)
    def test_transfer_account_valid(self,
    db_session:Session,
    api_manager: ApiManager,
    user_login:dict,
    transfer_data: TransferRequestData):
        result = api_manager.account_steps(user_login).transfer_account(
            transfer_data.request_data,

        )

        last_from_db = Transaction.get_transaction_last_by_account_id(db_session, transfer_data.request_data.fromAccountId)
        acc_to_db = DepositCrud.get_deposit_by_account_id(db_session, transfer_data.request_data.fromAccountId)
        assert acc_to_db.balance == result.fromAccountIdBalance
        assert acc_to_db.id == transfer_data.request_data.fromAccountId
        assert last_from_db.amount == transfer_data.request_data.amount, "Сумма транзакции в БД неверна"




    @pytest.mark.parametrize("transfer_data", [-10, 0, 499.9, 10000.1],indirect=True)
    def test_transfer_account_invalid(self,
    db_session:Session,
    api_manager: ApiManager,
    user_login:dict,
    transfer_data: TransferRequestData):
        result = api_manager.account_steps(user_login).transfer_account_invalid(
            transfer_data.request_data,
        )
        acc_from_db = DepositCrud.get_deposit_by_account_id(db_session, transfer_data.request_data.fromAccountId)
        acc_to_db = DepositCrud.get_deposit_by_account_id(db_session, transfer_data.request_data.toAccountId)
        assert acc_to_db.balance == 0, f"Баланс получателя изменился, хотя перевод был невалидным!"
        assert acc_from_db.balance == 18000
        assert acc_to_db.balance == 0











