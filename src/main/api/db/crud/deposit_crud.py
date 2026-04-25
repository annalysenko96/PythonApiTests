from sqlalchemy.orm import Session

from src.main.api.db.models.account_table import Account


class DepositCrud:
    @staticmethod
    def get_deposit_by_account_id(db: Session, account_id: int) -> Account | None:
        return db.query(Account).filter(Account.id == account_id).first()
