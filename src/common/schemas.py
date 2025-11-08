from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class LogEntry(BaseModel):
    timestamp: datetime
    source: str
    log_level: str
    message: str
    additional_info: Optional[dict] = None

class Alert(BaseModel):
    alert_id: str
    timestamp: datetime
    severity: str
    description: str
    related_logs: List[LogEntry]
    status: str

class Configuration(BaseModel):
    collectors: List[str]
    parsers: List[str]
    storage: str
    alerting: dict
    enrichment: List[str]