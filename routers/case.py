import asyncio

from fastapi import Depends
from sqlalchemy.orm import session

from database.get_db import get_db
from runner.webRunner import web_case_runner
from routers import caseRouter
from database import crud


@caseRouter.post("/add")
def create_case(case, db: session = Depends(get_db)):
    data = crud.Case(db).create_case(case)
    return {'code': 200, 'data': data, 'msg': 'success'}


@caseRouter.post("/update")
def update_case(case, db: session = Depends(get_db)):
    data = crud.Case(db).update_case(case)
    return {'code': 200, 'data': data, 'msg': 'success'}


@caseRouter.post("/updateResult")
def update_case_result(case, db: session = Depends(get_db)):
    data = crud.Case(db).update_case_result(case)
    return {'code': 200, 'data': data, 'msg': 'success'}


@caseRouter.delete("/del/{case_id}")
def delete_case(case_id, db: session = Depends(get_db)):
    data = crud.Case(db).delete_case(case_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@caseRouter.get("/get/{case_id}")
def read_case(case_id, db: session = Depends(get_db)):
    data = crud.Case(db).get_case(case_id)
    return {'code': 200, 'data': data, 'msg': 'success'}


@caseRouter.get("/get")
def read_cases(db: session = Depends(get_db)):
    data = crud.Case(db).get_cases()
    return {'code': 200, 'data': data, 'msg': 'success'}


@caseRouter.post("/run")
async def run_case(req_data):
    url = "https://dp-xng9o9wjy2rpx.gw002.oneitfarm.com/"
    asyncio.create_task(web_case_runner())
