from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastadmin.system.api import users
from fastadmin.system.schemas import Response,UsersCreate,Users, UsersPassword
from fastadmin.system.database import SessionLocal
from fastadmin.utils.common.resp import respSuccessJson, respErrorJson
from fastadmin.utils.common import error_code
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
    db_user = users.db_query_user_by_username(db, user.username)
    if db_user :
        return respErrorJson(error_code.ERROR_USER_ACCOUNT_EXISTS)
    result = users.db_create_user(db,user)
    print(Users(**result))
    return respSuccessJson(result)

@router.post("/delete",response_model = Response)
async def delete_user(id: str, db: Session = Depends(get_db)):
    result = users.db_delete_user_by_id(db, id)
    if not result:
        return respErrorJson(error_code.ERROR_USER_NOT_FOUND)
    return respSuccessJson()

@router.post("/updatePwd",response_model = Response)
async def update_pwd(user_pwd: UsersPassword, db: Session = Depends(get_db)):
    result = users.db_update_pwd(db, user_pwd)
    if not result:
        return respErrorJson(error_code.ERROR_USER_PASSWORD_ERROR)
    return respSuccessJson()

@router.get("/me",response_model= Response[Users])
async def read_user_me(username: str, db: Session = Depends(get_db)):
    db_user = users.db_query_user_by_username(db,username)
    if not db_user:
        return respErrorJson(error_code.ERROR_USER_NOT_FOUND)
    return respSuccessJson(db_user)

@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}