import pytest
from sqlalchemy.orm import Session

from main.api.classes.api_manager import ApiManager
from main.api.db.crud.deposit_crud import DepositCrud
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction

@pytest.mark.api
class TestTransfer:
    @pytest.mark.parametrize("amount", [500, 500.1, 9999.9, 10000])
    def test_transfer_account_valid(self,db_session: Session, api_manager: ApiManager,user_login:dict, amount:float):
        acc_from = api_manager.account_steps(user_login).create_account()
        acc_to = api_manager.account_steps(user_login).create_account()
        for _ in range(2):
            api_manager.account_steps(user_login).create_account_deposit(
            DepositAccountRequest(accountId=acc_from.id, amount=9000),
            ResponseSpecs.request_ok()
            )
        transfer_data = TransferAccountRequest(fromAccountId=acc_from.id, toAccountId=acc_to.id, amount=amount)
        result = api_manager.account_steps(user_login).transfer_account(
            transfer_data,
            ResponseSpecs.request_ok()
        )
        assert result.fromAccountIdBalance == (18000 - amount)

        last_from_db = Transaction.get_transaction_last_by_account_id(db_session,acc_from.id)
        assert last_from_db.amount == amount
        assert last_from_db.from_account_id == acc_from.id
        assert last_from_db.to_account_id == acc_to.id

        acc_to_db = DepositCrud.get_deposit_by_account_id(db_session,acc_to.id)
        acc_from_db = DepositCrud.get_deposit_by_account_id(db_session,acc_from.id)
        assert acc_from_db.balance == 18000 - amount
        assert acc_to_db.balance == amount


    @pytest.mark.parametrize("amount", [-10, 0, 499.9, 10000.1])
    def test_transfer_account_invalid(self,db_session: Session, api_manager: ApiManager,user_login:dict, amount:float):
        acc_from = api_manager.account_steps(user_login).create_account()
        acc_to = api_manager.account_steps(user_login).create_account()
        for _ in range(2):
            api_manager.account_steps(user_login).create_account_deposit(
                DepositAccountRequest(accountId=acc_from.id, amount=9000),
                ResponseSpecs.request_ok()
            )
        transfer_data = TransferAccountRequest(fromAccountId=acc_from.id, toAccountId=acc_to.id, amount=amount)
        api_manager.account_steps(user_login).transfer_account(
            transfer_data,
            ResponseSpecs.request_bad()
        )
        acc_to_db = DepositCrud.get_deposit_by_account_id(db_session, acc_to.id)
        acc_from_db = DepositCrud.get_deposit_by_account_id(db_session, acc_from.id)
        assert acc_from_db.balance == 18000, f'Со счета списалось {amount} руб.'
        assert acc_to_db.balance == 0, f'Счет пополненен на {amount} руб.'












