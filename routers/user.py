from fastapi import Depends
from sqlalchemy.orm import session

from database import crud
from database.get_db import get_db
from routers import userRouter


@userRouter.post("/login")
def user_login(login_data, db: session = Depends(get_db)):
    data = crud.User(db).get_user_by_name(login_data.get('username'))
    if login_data.get('password') == data.password:
        return {'code': 200, 'data': data, 'msg': 'success'}
    return {'code': 400, 'data': {}, 'msg': '账户名或密码填写错误'}


@userRouter.post("/add")
def create_user(user, db: session = Depends(get_db)):
    data = crud.User(db).create_user(user)
    return {'code': 200, 'data': data, 'msg': 'success'}


@userRouter.post("/update")
def update_user(user, db: session = Depends(get_db)):
    data = crud.User(db).update_user(user)
    return {'code': 200, 'data': data, 'msg': 'success'}


@userRouter.get("/get/{id}")
def read_user(ele_id, db: session = Depends(get_db)):
    data = crud.User(db).get_user(ele_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@userRouter.get("/get")
def read_users(db: session = Depends(get_db)):
    data = crud.User(db).get_users()
    return {'code': 200, 'data': data, 'msg': 'success'}
