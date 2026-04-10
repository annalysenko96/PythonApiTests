from sqlalchemy import Column,Integer,String,DateTime
from src.main.api.db.base import  Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,autoincrement=True) #autoincrement - значения будут автоматически увеличиваться при добавлении новой строки
    username = Column(String,unique=True,nullable=False) #unique - значит что значения должны быть уникальными, nullable - поле обязательно для заполнения
    password = Column(String,nullable=False)
    role = Column(Integer,nullable=False)
    deleted_at = Column(DateTime)

def __repr__(self):
    return f'<User(id={self.id},username={self.username}, role={self.role}, deleted_at={self.deleted_at})>'