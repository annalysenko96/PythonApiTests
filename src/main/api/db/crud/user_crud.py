from sqlalchemy.orm import Session
from src.main.api.db.models.user_table import User

class UserCrudDb:
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> User | None:
        return db.query(User).filter_by(username=username).first()


    # пригодиться для будущих тестов
    # @staticmethod
    #def create_user(db: Session, user: str, password: str, role: str) -> User:
        user = User(
            username=user,
            password=password,
            role=role
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
