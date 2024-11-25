from sqlalchemy import Column, String, Integer, BigInteger
from database.sessions import Base

class User(Base):
    __tablename__= 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    age = Column(Integer, index=True)
    email = Column(String, index=True)
    phone = Column(BigInteger, index=True)
    address = Column(String, index=True)
    username = Column(String, index=True)
    role = Column(String, index=True)
    password = Column(String, index=True)

    def __repr__(self) -> str:
        return f"<User(id = {self.id}, name = {self.name}, last_name = {self.last_name}, email = {self.email}, phone = {self.phone}, address = {self.address})>"