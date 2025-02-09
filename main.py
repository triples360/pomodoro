from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hello, Welcome to a simple pomodoro app!"


@app.post("/start")
async def start_timer():
    
