from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse
from starlette import status
import asyncio
import json
from datetime import datetime

router = APIRouter(
    prefix="/api",
    tags=["Health"],
)


@router.get("/health", status_code=status.HTTP_200_OK)
def get_health():
    return {"health": "healthy"}


async def datetime_stream():
    """Generate SSE stream with current datetime"""
    while True:
        current_time = datetime.now().isoformat()
        data = json.dumps({"datetime": current_time, "message": "Current server time"})
        yield f"data: {data}\n\n"
        await asyncio.sleep(1)  # Send update every second


@router.get("/health/stream")
async def get_health_stream():
    """SSE endpoint that streams current datetime"""
    return StreamingResponse(
        datetime_stream(),
        media_type="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "text/event-stream",
        }
    )


@router.websocket("/health/ws")
async def websocket_health(websocket: WebSocket):
    """WebSocket endpoint for real-time server health updates"""
    await websocket.accept()
    try:
        while True:
            # Send health status with current datetime
            health_data = {
                "health": "healthy",
                "datetime": datetime.now().isoformat(),
                "timestamp": datetime.now().timestamp(),
                "message": "Server health check via WebSocket"
            }
            await websocket.send_json(health_data)
            await asyncio.sleep(2)  # Send update every 2 seconds
    except WebSocketDisconnect:
        pass  # Client disconnected, exit gracefully
