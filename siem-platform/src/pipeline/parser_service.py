class ParserService:
    def __init__(self):
        pass

    def parse_syslog(self, syslog_data):
        # Appeler la fonction de parsing Syslog
        from src.parsers.syslog_parser import parse_syslog
        return parse_syslog(syslog_data)

    def parse_evtx(self, evtx_data):
        # Appeler la fonction de parsing EVTX
        from src.parsers.evtx_parser import parse_evtx
        return parse_evtx(evtx_data)

    def parse_json_log(self, json_log_data):
        # Appeler la fonction de parsing JSON
        from src.parsers.json_log_parser import parse_json_log
        return parse_json_log(json_log_data)