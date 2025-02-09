# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 00:34:31 2025

@author: shubh
"""
"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio

app = FastAPI()

@app.websocket("/ws/timer")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        for seconds in range(1, 11):  # 10-second timer
            await websocket.send_text(f"Timer: {seconds} seconds")
            await asyncio.sleep(1)
        await websocket.send_text("Timer completed!")
    except WebSocketDisconnect:
        print("Client disconnected")
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio

app = FastAPI()

@app.websocket("/ws/timer")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    timer = 1  # Start from 1 second
    running = True  # Control the timer state

    try:
        while timer <= 10:
            if running:
                await websocket.send_text(f"Timer: {timer} seconds")
                await asyncio.sleep(1)
                timer += 1
            else:
                data = await websocket.receive_text()
                if data.lower() == "resume":
                    running = True
                elif data.lower() == "exit":
                    await websocket.send_text("Exiting...")
                    break

        await websocket.send_text("Timer completed!")
    
    except WebSocketDisconnect:
        print("Client disconnected")
