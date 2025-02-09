# pomodoro_app.py

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import time
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import threading
import asyncio

app = FastAPI()

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# This will serve the main HTML page
@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("templates/index.html", "r") as file:
        content = file.read()
    return content

# Timer state
class PomodoroTimer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.is_running = False
        self.duration = 0

    def start(self, duration_minutes: int):
        self.start_time = time.time()
        self.duration = duration_minutes * 60  # convert to seconds
        self.duration = 2
        self.end_time = self.start_time + self.duration
        self.is_running = True

    def stop(self):
        self.is_running = False

    def get_remaining_time(self):
        if self.is_running:
            print(f"HELLO!!! {self.end_time - time.time()}")
            return max(0, self.end_time - time.time())
        return 0

# Initialize Pomodoro timer
pomodoro_timer = PomodoroTimer()

# WebSocket for real-time updates
@app.websocket("/ws/timer")
async def websocket_timer(websocket: WebSocket):
    await websocket.accept()

    while True:
        if pomodoro_timer.is_running:
            remaining_time = pomodoro_timer.get_remaining_time()
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            await websocket.send_text(f"{minutes:02d}:{seconds:02d}")
            if(minutes == 0 and seconds == 0):
                pomodoro_timer.stop()
        await asyncio.sleep(1)

@app.get("/start_timer/{duration}")
async def start_timer(duration: int):
    pomodoro_timer.start(duration)
    return {"status": "Pomodoro started", "duration": duration}

@app.get("/stop_timer")
async def stop_timer():
    pomodoro_timer.stop()
    return {"status": "Pomodoro stopped"}

@app.get("/v1/resources/finish_audio/user")
def get_audio():
    return FileResponse("resources/avicii_levels.mp3", media_type="audio/mpeg")
