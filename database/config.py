from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
sqlalchemy连接数据库方式：
database(使用的数据库) + driver(使用的数据库驱动)://username:passwor@host:port/database
"""
DB_CONFIG = {
    'HOST': 'localhost',
    'PORT': 3306,
    'USERNAME': 'root',
    'PASSWORD': '111111',
    'DB': 'test_platform'
}
DB_URL = f"mysql+pymysql://{DB_CONFIG['USERNAME']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['HOST']}:{DB_CONFIG['PORT']}/{DB_CONFIG['DB']}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
