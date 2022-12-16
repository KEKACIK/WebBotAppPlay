import datetime

from sqlalchemy import Column, Integer, DateTime, Boolean, String

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True)

    username = Column(String)
    is_admin = Column(Boolean, default=False)

    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
