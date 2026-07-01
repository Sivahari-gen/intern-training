from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from sse_starlette.sse import EventSourceResponse
import asyncio


app = FastAPI()
clients = []

# Websocket
@app.websocket("/ws")
async def web(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            # echo
            # await websocket.send_text(message)
            # broadcas
            for client in clients:
                await client.send_text(message)
    except WebSocketDisconnect:
        clients.remove(websocket)

async def generator():
    count = 0
    while True:
        count+=1
        yield {
            "event": "message",
            "data": f"Counter: {count}"
        }
        await asyncio.sleep(1)

#SSe
@app.get("/events")
async def sse():
    return EventSourceResponse(generator())
