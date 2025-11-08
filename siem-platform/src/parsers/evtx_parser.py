from evtx import Evtx
import json

def parse_evtx(file_path):
    events = []
    with Evtx(file_path) as log:
        for record in log.records():
            event = record.json()
            events.append(event)
    return json.dumps(events, indent=4)