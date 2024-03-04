

from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base, current_utc_time


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email=Column(String, nullable=False)


    def __repr__(self):
        return f"<User {self.username}>"