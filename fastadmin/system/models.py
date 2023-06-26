 # models.py
 
from sqlalchemy import Column, String,DateTime
from fastadmin.system.database import Base
from datetime import datetime
import uuid

class Users(Base):
    __tablename__ = 'users'  # 数据库表名

    id = Column(String(255), primary_key=True, default = uuid.uuid1())
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)

