import asyncio
from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(
    prefix="/ws",
    tags=["MIDAS"],
)


# Connection manager for handling multiple clients
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/logs")
async def websocket_logs_endpoint(websocket: WebSocket):
    """WebSocket endpoint that broadcasts messages to all connected clients and sends logs every 5 seconds"""

    await manager.connect(websocket)

    # Create task to send logs every 5 seconds
    async def send_logs():
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await manager.broadcast(f"[{timestamp}] [INFO] Migration in progress...")
            await asyncio.sleep(5)

    log_task = asyncio.create_task(send_logs())

    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        log_task.cancel()  # Cancel the periodic log task when client disconnects
