from fastapi import Depends
from sqlalchemy.orm import session
from database import crud
from database.get_db import get_db
from routers import optRouter


@optRouter.get("/get")
def read_options(db: session = Depends(get_db)):
    data = crud.Option(db).get_options()
    return {'code': 200, 'data': data, 'msg': 'success'}
