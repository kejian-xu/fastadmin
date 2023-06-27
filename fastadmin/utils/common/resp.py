# resp.py
from fastapi import status
from fastapi.responses import JSONResponse  # , ORJSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Union, Optional
 
from fastadmin.utils.common.error_code import ErrorBase
 
 
class respJsonBase(BaseModel):
    code: int
    msg: str
    data: Union[dict, list]
 
 
def respSuccessJson(data: Union[list, dict, str] = None, msg: str = "Success"):
    """ 接口成功返回 """
    json_data = jsonable_encoder(data)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'msg': msg,
            'data': json_data or {}
        }
    )
 
 
def respErrorJson(error: ErrorBase, *, msg: Optional[str] = None, msg_append: str = "",
                  data: Union[list, dict, str] = None, status_code: int = status.HTTP_200_OK):
    """ 错误接口返回 """
    return JSONResponse(
        status_code=status_code,
        content={
            'code': error.code,
            'msg': (msg or error.msg) + msg_append,
            'data': data or {}
        }
    )