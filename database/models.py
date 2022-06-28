from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from database.config import Base, engine


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    telephone = Column(String(11), unique=True, index=True)
    password = Column(String(252))
    status = Column(Integer)  # 用户当前状态（0-不存在，1-存在且正常，2-存在但不正常）
    level = Column(Integer, default=1)  # 用户权限约定（0-管理员，1-普通，2-高级）


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(100), unique=True, index=True)     # 项目名称
    icon = Column(String, unique=True)                              # 项目图标
    description = Column(Text(500))                                 # 项目描述
    platform = Column(String(50))                                   # 项目类型（android，iOS，webUI，api）
    version = Column(String(8))                                     # 项目版本号
    create_user = Column(String(8))
    create_time = Column(DateTime, default=datetime.now())
    update_user = Column(String(8))
    update_time = Column(DateTime, default=datetime.now())


class Option(Base):
    __tablename__ = 'option'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)


class Element(Base):
    __tablename__ = 'element'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    element = Column(String(1000))
    locator = Column(String(50))
    project = Column(String(100))
    createuser = Column(String(8))
    createtime = Column(DateTime, default=datetime.now())
    updateuser = Column(String(8))
    updatetime = Column(DateTime, default=datetime.now())


class Step(Base):
    __tablename__ = 'step'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(500))
    project = Column(String(100))
    option = Column(String(50))
    element = Column(String(50))
    value = Column(String(100))
    # wish = Column(String(100))
    createuser = Column(String(8))
    createtime = Column(DateTime, default=datetime.now())
    updateuser = Column(String(8))
    updatetime = Column(DateTime, default=datetime.now())


class Suite(Base):
    __tablename__ = 'suite'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500))
    project = Column(String(100))
    step = Column(Text)
    createuser = Column(String(8))
    createtime = Column(DateTime, default=datetime.now())
    updateuser = Column(String(8))
    updatetime = Column(DateTime, default=datetime.now())


class Case(Base):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500))
    project = Column(String(50))
    level = Column(String(10))
    tag = Column(String(50))
    status = Column(Integer)  # 0-可执行；1-执行中
    result = Column(String(3))  # 失败；成功；未执行
    content = Column(Text)
    createuser = Column(String(8))
    createtime = Column(DateTime, default=datetime.now())
    updateuser = Column(String(8))
    updatetime = Column(DateTime, default=datetime.now())


class Result(Base):
    __tablename__ = 'result'

    id = Column(Integer, index=True, primary_key=True)
    result = Column(String(20))
    case = Column(String(500))
    schedule = Column(String(500))
    image = Column(Text)


class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(500))
    period = Column(String(20))
    createuser = Column(String(8))
    createtime = Column(DateTime, default=datetime.now())
    updateuser = Column(String(8))
    updatetime = Column(DateTime, default=datetime.now())


# 创建所有表
Base.metadata.create_all(bind=engine)
