from fastapi import Depends
from sqlalchemy.orm import session

from database import crud
from database.get_db import get_db
from routers import reportRouter


@reportRouter.post("/create_project")
def create_project(project, db: session = Depends(get_db)):
    db_prj = crud.Project(db).create_project(project)
    return db_prj


@reportRouter.post("/update_project")
def update_project(project, db: session = Depends(get_db)):
    db_prj = crud.Project(db).update_project(project)
    return db_prj


@reportRouter.delete("/delete_project/{prj_id}")
def delete_project(prj_id, db: session = Depends(get_db)):
    db_prj = crud.Project(db).delete_project(prj_id)
    return db_prj


@reportRouter.get("/projects")
def read_projects(db: session = Depends(get_db)):
    prj = crud.Project(db).get_projects()
    return prj


@reportRouter.get("/project/{prj_id}")
def read_project(prj_id, db: session = Depends(get_db)):
    prj = crud.Project(db).get_project(prj_id)
    return prj


@reportRouter.post("/create_element")
def create_element(element, db: session = Depends(get_db)):
    db_element = crud.Element(db).create_element(element)
    return db_element


@reportRouter.post("/update_element")
def update_element(element, db: session = Depends(get_db)):
    db_element = crud.Element(db).update_element(element)
    return db_element


@reportRouter.delete("/delete_element/{element_id}")
def delete_element(element_id, db: session = Depends(get_db)):
    db_element = crud.Element(db).delete_element(element_id)
    return db_element


@reportRouter.get("/elements")
def read_elements(db: session = Depends(get_db)):
    element = crud.Element(db).get_elements()
    return element


@reportRouter.post("/create_step")
def create_step(step, db: session = Depends(get_db)):
    db_step = crud.Step(db).create_step(step)
    return db_step


@reportRouter.post("/update_step")
def update_step(step, db: session = Depends(get_db)):
    db_step = crud.Step(db).update_step(step)
    return db_step


@reportRouter.delete("/delete_step/{step_id}")
def delete_step(step_id, db: session = Depends(get_db)):
    db_step = crud.Step(db).delete_step(step_id)
    return db_step


@reportRouter.get("/steps")
def read_steps(db: session = Depends(get_db)):
    db_step = crud.Step(db).get_steps()
    return db_step


@reportRouter.post("/create_suite")
def create_suite(suite, db: session = Depends(get_db)):
    db_data = crud.Suite(db).create_suite(suite)
    return db_data


@reportRouter.post("/update_suite")
def update_suite(suite, db: session = Depends(get_db)):
    db_data = crud.Suite(db).update_suite(suite)
    return db_data


@reportRouter.delete("/delete_suite/{suite_id}")
def delete_suite(suite_id, db: session = Depends(get_db)):
    db_data = crud.Suite(db).delete_suite(suite_id)
    return db_data


@reportRouter.get("/suites")
def read_suites(db: session = Depends(get_db)):
    db_data = crud.Suite(db).get_suites()
    for data in db_data:
        data.suite_step = data.suite_step.split(";")
    return db_data


@reportRouter.get("/options")
def read_options(db: session = Depends(get_db)):
    db_res = crud.Option(db).get_options()
    return db_res
