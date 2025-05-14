 # models.py
 
from sqlalchemy import Column, String, DateTime, Integer
from fastadmin.system.database import Base
from datetime import datetime

import uuid

class Users(Base):
    __tablename__ = 'sys_user'  # 数据库表名

    user_id = Column(Integer, primary_key=True, default = uuid.uuid1())
    dept_id = Column(Integer)
    user_name = Column(String(30))
    nick_name = Column(String(30))
    user_type = Column(String(2))
    email = Column(String(50))
    phonenumber = Column(String(11))
    sex = Column(String(1))
    avatar = Column(String(100))
    password = Column(String(100))
    status = Column(String(1))
    del_flag = Column(String(1))
    login_ip = Column(String(128))
    login_date = Column(DateTime)
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    remark = Column(String(500))

