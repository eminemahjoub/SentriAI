from datetime import datetime
import json
import re

def parse_syslog(log):
    """
    Parse a syslog message into a structured JSON format.

    Args:
        log (str): A single syslog message.

    Returns:
        dict: A dictionary containing the parsed log information.
    """
    # Regex pattern to match syslog format
    pattern = r'^(?P<timestamp>\w{3} +\d{1,2} \d{2}:\d{2}:\d{2}) (?P<hostname>\S+) (?P<app>\S+): (?P<message>.*)$'
    match = re.match(pattern, log)

    if match:
        timestamp_str = match.group('timestamp')
        timestamp = datetime.strptime(timestamp_str, '%b %d %H:%M:%S')
        return {
            'timestamp': timestamp.isoformat(),
            'hostname': match.group('hostname'),
            'application': match.group('app'),
            'message': match.group('message')
        }
    else:
        return {
            'error': 'Invalid syslog format',
            'original_log': log
        }