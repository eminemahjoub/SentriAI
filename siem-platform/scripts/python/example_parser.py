# example_parser.py

import json

def parse_syslog(log_entry):
    # Simulate parsing a syslog entry
    parsed_entry = {
        "timestamp": log_entry.get("timestamp"),
        "host": log_entry.get("host"),
        "message": log_entry.get("message"),
        "severity": log_entry.get("severity"),
    }
    return parsed_entry

def parse_evtx(evtx_entry):
    # Simulate parsing an EVTX entry
    parsed_entry = {
        "event_id": evtx_entry.get("event_id"),
        "timestamp": evtx_entry.get("timestamp"),
        "source": evtx_entry.get("source"),
        "message": evtx_entry.get("message"),
    }
    return parsed_entry

def parse_json_log(json_log):
    # Simulate parsing a JSON log entry
    return json_log

if __name__ == "__main__":
    # Example log entries for testing
    syslog_entry = {
        "timestamp": "2023-10-01T12:00:00Z",
        "host": "localhost",
        "message": "This is a test syslog message.",
        "severity": "INFO"
    }

    evtx_entry = {
        "event_id": 4624,
        "timestamp": "2023-10-01T12:01:00Z",
        "source": "Security",
        "message": "An account was successfully logged on."
    }

    json_log_entry = {
        "timestamp": "2023-10-01T12:02:00Z",
        "host": "localhost",
        "message": "This is a test JSON log message."
    }

    print("Parsed Syslog Entry:", json.dumps(parse_syslog(syslog_entry), indent=2))
    print("Parsed EVTX Entry:", json.dumps(parse_evtx(evtx_entry), indent=2))
    print("Parsed JSON Log Entry:", json.dumps(parse_json_log(json_log_entry), indent=2))