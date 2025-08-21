import asyncio
import json
from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse
from starlette import status

from app.config import settings

router = APIRouter(
    prefix=f"{settings.API_PREFIX}/health",
    tags=["Health"],
)


@router.get("/", status_code=status.HTTP_200_OK)
def get_health():
    return {"health": "healthy"}


async def datetime_stream():
    """Generate SSE stream with current datetime"""
    while True:
        current_time = datetime.now().isoformat()
        data = json.dumps({"datetime": current_time, "message": "Current server time"})
        yield f"data: {data}\n\n"
        await asyncio.sleep(1)  # Send update every second


@router.get("/stream")
async def get_health_stream():
    """SSE endpoint that streams current datetime"""
    return StreamingResponse(
        datetime_stream(),
        media_type="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "text/event-stream",
        },
    )


@router.websocket("/ws")
async def websocket_health(websocket: WebSocket):
    """WebSocket endpoint for real-time server health updates with ping/pong support"""
    await websocket.accept()
    try:
        # Create tasks for sending periodic health updates and handling incoming
        # messages
        async def send_health_updates():
            while True:
                health_data = {
                    "health": "healthy",
                    "datetime": datetime.now().isoformat(),
                    "timestamp": datetime.now().timestamp(),
                    "message": "Server health check via WebSocket",
                    "type": "health_update",
                }
                await websocket.send_json(health_data)
                await asyncio.sleep(2)  # Send update every 2 seconds

        async def handle_incoming_messages():
            while True:
                try:
                    # Wait for incoming messages with a timeout
                    message = await asyncio.wait_for(
                        websocket.receive_json(), timeout=0.1
                    )

                    # Handle ping messages
                    if message.get("type") == "ping":
                        pong_response = {
                            "type": "pong",
                            "datetime": datetime.now().isoformat(),
                            "timestamp": datetime.now().timestamp(),
                            "message": "Pong response from server",
                        }
                        if "id" in message:
                            pong_response["id"] = message["id"]
                        await websocket.send_json(pong_response)

                    if message.get("type") == "message":
                        message_response = {
                            "type": "message",
                            "datetime": datetime.now().isoformat(),
                            "timestamp": datetime.now().timestamp(),
                            "message": "Received message from client",
                        }
                        if "id" in message:
                            message_response["id"] = message["id"]
                        await websocket.send_json(message_response)

                except TimeoutError:
                    # No message received, continue
                    continue
                except Exception:
                    # Message parsing error or connection issue
                    break

        # Run both tasks concurrently
        await asyncio.gather(send_health_updates(), handle_incoming_messages())
    except WebSocketDisconnect:
        # Client disconnected, exit gracefully
        pass
