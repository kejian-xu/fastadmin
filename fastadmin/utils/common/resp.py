# resp.py
from fastapi import status
from fastapi.responses import JSONResponse  # , ORJSONResponse
from pydantic import BaseModel
from typing import Union, Optional, Any, List
 
from fastadmin.utils.common.error_code import ErrorBase
 
 
class respJsonBase(BaseModel):
    code: int
    msg: str
    data: Union[dict, List, Any]
 
 
def respSuccessJson(data: Union[List, dict, str, Any] = None, msg: str = "Success"):
    """ 接口成功返回 """
    return respJsonBase(
        code = status.HTTP_200_OK,
        msg = msg,
        data = data
    )
 
 
def respErrorJson(error: ErrorBase, *, msg: Optional[str] = None, msg_append: str = "",
                  data: Union[List, dict, str] = None, status_code: int = status.HTTP_200_OK):
    """ 错误接口返回 """
    return JSONResponse(
        status_code=status_code,
        content={
            'code': error.code,
            'msg': (msg or error.msg) + msg_append,
            'data': data or {}
        }
    )