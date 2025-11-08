import unittest
from src.parsers.syslog_parser import parse_syslog
from src.parsers.evtx_parser import parse_evtx
from src.parsers.json_log_parser import parse_json_log

class TestParsers(unittest.TestCase):

    def test_parse_syslog(self):
        raw_log = "<34>1 2023-10-01T12:00:00Z hostname appname 1234 - - This is a test syslog message"
        expected_output = {
            "priority": 34,
            "version": 1,
            "timestamp": "2023-10-01T12:00:00Z",
            "hostname": "hostname",
            "appname": "appname",
            "procid": "1234",
            "msg": "This is a test syslog message"
        }
        self.assertEqual(parse_syslog(raw_log), expected_output)

    def test_parse_evtx(self):
        raw_evtx = "Sample EVTX data"
        expected_output = {
            "event_id": 1234,
            "timestamp": "2023-10-01T12:00:00Z",
            "message": "This is a test EVTX message"
        }
        self.assertEqual(parse_evtx(raw_evtx), expected_output)

    def test_parse_json_log(self):
        raw_json_log = '{"key": "value", "timestamp": "2023-10-01T12:00:00Z"}'
        expected_output = {
            "key": "value",
            "timestamp": "2023-10-01T12:00:00Z"
        }
        self.assertEqual(parse_json_log(raw_json_log), expected_output)

if __name__ == '__main__':
    unittest.main()