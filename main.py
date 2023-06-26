# import uvicorn
from fastapi import FastAPI

# from fastadmin.utils.captcha import EasyCaptcha
# from fastadmin.system.schemas import Response, Captcha
# from fastadmin.utils.mysql_util import Mysqldb
# from fastadmin.utils.json_response import DetailResponse
from fastadmin.system.router import users
from fastadmin.system.database import Base,engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get('/')
async def root():
    return {"msg": 'Hello World'}

# @app.get('/getCaptcha', response_model = Response[Captcha])
# async def getCaptcha():
#     captcha = EasyCaptcha(120, 35, is_blur=False)
#     base64Image = captcha.get_base64_image()
#     key = captcha.get_key_code()
#     return DetailResponse({'base64': base64Image,'key':key})

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8080)