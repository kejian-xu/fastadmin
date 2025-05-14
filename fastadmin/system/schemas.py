from pydantic import BaseModel, ConfigDict
from pydantic.generics import GenericModel
from typing import Generic, TypeVar, Optional
from datetime import datetime

DataT = TypeVar('DataT')

class Response(GenericModel, Generic[DataT]):
    code: int
    data: Optional[DataT]
    msg: str
    
class Captcha(BaseModel):
    key: str
    base64: str

class UsersBase(BaseModel):
    username: str

class UsersCreate(UsersBase):
    password: str

class Users(UsersBase):
    id: str
    create_time: datetime
    update_time: datetime
    
    class Config:
        orm_mode = True


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    user_name: str
    email: str



    

