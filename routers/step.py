from fastapi import Depends
from sqlalchemy.orm import session

from database import crud
from database.get_db import get_db
from routers import stepRouter


@stepRouter.post("/add")
def create_step(step, db: session = Depends(get_db)):
    data = crud.Step(db).create_step(step)
    return {'code': 200, 'data': data, 'msg': 'success'}


@stepRouter.post("/update")
def update_step(step, db: session = Depends(get_db)):
    data = crud.Step(db).update_step(step)
    return {'code': 200, 'data': data, 'msg': 'success'}


@stepRouter.delete("/del/{step_id}")
def delete_step(step_id, db: session = Depends(get_db)):
    data = crud.Step(db).delete_step(step_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@stepRouter.get("/get/{step_id}")
def read_step(step_id, db: session = Depends(get_db)):
    data = crud.Step(db).get_step(step_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@stepRouter.get("/get")
def read_steps(db: session = Depends(get_db)):
    data = crud.Step(db).get_steps()
    return {'code': 200, 'data': data, 'msg': 'success'}
