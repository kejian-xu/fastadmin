from sqlalchemy.orm import Session
from fastadmin.system import schemas, models
import hashlib

def db_create_user(db: Session, user: schemas.UsersCreate):
    db_user = models.Users(username=user.username, password=make_password(user.password))
    db.add(db_user)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_user)  # 刷新
    return db_user

def make_password(password):
    # md5
    md5 = hashlib.md5()
    # 转码
    sign_utf8 = str(password).encode(encoding="utf-8")
    # 加密
    md5.update(sign_utf8)
    # 返回密文
    return md5.hexdigest()