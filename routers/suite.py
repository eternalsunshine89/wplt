from fastapi import Depends
from sqlalchemy.orm import session

from database import crud
from database.get_db import get_db
from routers import suiteRouter


@suiteRouter.post("/add")
def create_suite(suite, db: session = Depends(get_db)):
    data = crud.Suite(db).create_suite(suite)
    return {'code': 200, 'data': data, 'msg': 'success'}


@suiteRouter.post("/update")
def update_suite(suite, db: session = Depends(get_db)):
    data = crud.Suite(db).update_suite(suite)
    return {'code': 200, 'data': data, 'msg': 'success'}


@suiteRouter.delete("/del/{suite_id}")
def delete_suite(suite_id, db: session = Depends(get_db)):
    data = crud.Suite(db).delete_suite(suite_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@suiteRouter.get("/get/{suite_id}")
def read_suite(suite_id, db: session = Depends(get_db)):
    data = crud.Suite(db).get_suite(suite_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@suiteRouter.get("/get")
def read_suites(db: session = Depends(get_db)):
    data = crud.Suite(db).get_suites()
    return {'code': 200, 'data': data, 'msg': 'success'}
