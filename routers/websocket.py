import json
from fastapi import WebSocket, WebSocketDisconnect
from typing import List

from routers import websocketRouter


class ConnectionManager:
    def __init__(self):
        # 存放激活的ws连接对象
        self.active_connections: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove(ws)

    async def send_personal_message(self, message: str, ws: WebSocket):
        # 发送个人消息
        await ws.send_text(message)

    async def send_json_message(self, message: json, ws: WebSocket):
        # 发送个人消息
        await ws.send_json(message)

    async def broadcast(self, message: str):
        # 广播消息
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@websocketRouter.websocket("/{user}")
async def websocket_endpoint(websocket: WebSocket, user: str):
    try:
        await manager.connect(websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{user} - websocket连接失败")
