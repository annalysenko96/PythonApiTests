from sqlalchemy.orm import Session

from src.main.api.db.models.transaction_table import Transaction

class TransactionCrudDb:
    @staticmethod
    def get_transaction_by_account_id(db:Session, account_id:int) -> list[Transaction]:
        return db.query(Transaction).filter_by(from_account_id= account_id).all()

    @staticmethod
    def get_transaction_last_by_account_id(db:Session, account_id:int) -> Transaction | None:
        return db.query(Transaction).filter_by(from_account_id= account_id).order_by(Transaction.id.desc()).first()