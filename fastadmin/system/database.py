 # database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 代表哪一台计算机，ip地址是多少
HOSTNAME = '127.0.0.1'
# 端口号
PORT = '3306'
# 数据库的名字，连接那个数据库
DATABASE = 'user'
# 数据库的账号和密码
USERNAME = 'root'
PASSWORD = 'xukejian'
# 按照要求组织成一定的字符串
DB_URI = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8'\
    .format(username =USERNAME,pwd = PASSWORD,host = HOSTNAME,port=PORT,db = DATABASE)

engine = create_engine(
    DB_URI, pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
