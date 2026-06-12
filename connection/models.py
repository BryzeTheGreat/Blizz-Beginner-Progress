from connection.connect import Base
from sqlalchemy import Column, Integer, String

class Account(Base):
    __tablename__ = 'accounts'

    account_id = Column(String, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)

class UploadPost(Base):
    __tablename__ = 'posts'

    post_id = Column(String, primary_key=True)   
    content = Column(String, nullable=True)
    image = Column(String, nullable=True)
    username = Column(String, nullable=False)


    