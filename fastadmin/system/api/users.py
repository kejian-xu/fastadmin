from sqlalchemy.orm import Session
from fastadmin.system import schemas
from fastadmin.system.models import Users
import hashlib

def db_create_user(db: Session, user: schemas.UsersCreate):
    db_user = Users(username=user.username, password=make_password(user.password))
    db.add(db_user)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_user)  # 刷新
    return db_user

def db_query_user_by_username(db:Session, username: str):
    db_user = db.query(Users).filter(Users.username == username).first()
    return db_user

def db_delete_user_by_id(db:Session, id:str):
    db_user = db.query(Users).filter(Users.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    else: 
        return False
    
def db_update_pwd(db:Session, user_pwd: schemas.UsersPassword):
    db_user = db.query(Users).filter(Users.id == user_pwd.id).first()
    if db_user.password == make_password(user_pwd.old_password):
        db_user.password = make_password(user_pwd.new_password)
        db.commit()
        return True
    else: 
        return False

def make_password(password):
    # md5
    md5 = hashlib.md5()
    # 转码
    sign_utf8 = str(password).encode(encoding="utf-8")
    # 加密
    md5.update(sign_utf8)
    # 返回密文
    return md5.hexdigest()