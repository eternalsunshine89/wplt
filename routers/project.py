from fastapi import Depends
from sqlalchemy.orm import session

from database import crud
from database.get_db import get_db
from routers import prjRouter


@prjRouter.post("/add")
def create_project(prj, db: session = Depends(get_db)):
    data = crud.Project(db).create_project(prj)
    return {'code': 200, 'data': data, 'msg': 'success'}


@prjRouter.post("/update")
def update_project(prj, db: session = Depends(get_db)):
    data = crud.Project(db).update_project(prj)
    return {'code': 200, 'data': data, 'msg': 'success'}


@prjRouter.delete("/del/{prj_id}")
def delete_project(prj_id, db: session = Depends(get_db)):
    data = crud.Project(db).delete_project(prj_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@prjRouter.get("/get/{prj_id}")
def read_project(prj_id, db: session = Depends(get_db)):
    data = crud.Project(db).get_project(prj_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@prjRouter.get("/get")
def read_projects(db: session = Depends(get_db)):
    return {'code': 200, 'data': crud.Project(db).get_projects(), 'msg': 'success'}
