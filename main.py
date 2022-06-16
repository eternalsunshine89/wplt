import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers.option import optRouter
from routers.element import eleRouter
from routers.project import prjRouter
from routers.step import stepRouter
from routers.suite import suiteRouter
from routers.case import caseRouter
from routers.report import reportRouter
from routers.websocket import websocketRouter
from routers.user import userRouter

app = FastAPI()
app.include_router(websocketRouter, prefix='/ws')
app.include_router(userRouter, prefix='')
app.include_router(prjRouter, prefix='/project')
app.include_router(optRouter, prefix='/option')
app.include_router(eleRouter, prefix='/element')
app.include_router(stepRouter, prefix='/step')
app.include_router(suiteRouter, prefix='/suite')
app.include_router(caseRouter, prefix='/case')
app.include_router(reportRouter, prefix='/report')
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://192.168.2.119:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=9000, log_level='info', reload=True)
