# example_collector.py

import json
import logging
from src.collectors.syslog_collector import SyslogCollector
from src.collectors.windows_event_collector import WindowsEventCollector
from src.collectors.cloud_events_collector import CloudEventsCollector

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Initialize collectors
    syslog_collector = SyslogCollector()
    windows_event_collector = WindowsEventCollector()
    cloud_events_collector = CloudEventsCollector()
    
    # Collect logs
    syslog_logs = syslog_collector.collect()
    windows_event_logs = windows_event_collector.collect()
    cloud_logs = cloud_events_collector.collect()
    
    # Combine logs
    all_logs = syslog_logs + windows_event_logs + cloud_logs
    
    # Output logs in JSON format
    print(json.dumps(all_logs, indent=4))

if __name__ == "__main__":
    main()