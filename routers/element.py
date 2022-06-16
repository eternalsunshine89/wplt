from fastapi import Depends
from sqlalchemy.orm import session

from database import crud
from database.get_db import get_db
from routers import eleRouter


@eleRouter.post("/add")
def create_element(element, db: session = Depends(get_db)):
    data = crud.Element(db).create_element(element)
    return {'code': 200, 'data': data, 'msg': 'success'}


@eleRouter.post("/update")
def update_element(element, db: session = Depends(get_db)):
    data = crud.Element(db).update_element(element)
    return {'code': 200, 'data': data, 'msg': 'success'}


@eleRouter.delete("/del/{ele_id}")
def delete_element(ele_id, db: session = Depends(get_db)):
    data = crud.Element(db).delete_element(ele_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@eleRouter.get("/get/{id}")
def read_element(ele_id, db: session = Depends(get_db)):
    data = crud.Element(db).get_element(ele_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@eleRouter.get("/get")
def read_elements(db: session = Depends(get_db)):
    data = crud.Element(db).get_elements()
    return {'code': 200, 'data': data, 'msg': 'success'}
