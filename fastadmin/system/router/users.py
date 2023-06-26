from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastadmin.system.api import users
from fastadmin.system.schemas import Response,UsersCreate,Users
from fastadmin.system.database import SessionLocal
from fastadmin.utils.common.resp import respSuccessJson

# Dependency
def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

router = APIRouter(
    prefix="/users",  # 前缀只在这个模块中使用
    tags=["users"],
)

@router.post("/create",response_model = Response[Users])
async def create_user(user: UsersCreate, db: Session = Depends(get_db)):
    return respSuccessJson(users.db_create_user(db,user))

@router.get("/users/me")
async def read_user_me():
    return {"username": "zhangsan"}