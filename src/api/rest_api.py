from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class LogEntry(BaseModel):
    timestamp: str
    source: str
    message: str
    severity: str

class Alert(BaseModel):
    id: int
    description: str
    severity: str
    timestamp: str

@app.post("/logs/", response_model=LogEntry)
async def create_log(log: LogEntry):
    # Logic to process and store the log entry
    return log

@app.get("/logs/", response_model=List[LogEntry])
async def read_logs():
    # Logic to retrieve logs
    return []

@app.post("/alerts/", response_model=Alert)
async def create_alert(alert: Alert):
    # Logic to process and store the alert
    return alert

@app.get("/alerts/", response_model=List[Alert])
async def read_alerts():
    # Logic to retrieve alerts
    return []