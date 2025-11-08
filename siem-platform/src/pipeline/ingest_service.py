class IngestService:
    def __init__(self, collectors, parser_service, indexer_service):
        self.collectors = collectors
        self.parser_service = parser_service
        self.indexer_service = indexer_service

    def collect_logs(self):
        collected_logs = []
        for collector in self.collectors:
            logs = collector.collect()
            collected_logs.extend(logs)
        return collected_logs

    def ingest_logs(self):
        logs = self.collect_logs()
        parsed_logs = self.parser_service.parse_logs(logs)
        self.indexer_service.index_logs(parsed_logs)

    def run(self):
        while True:
            self.ingest_logs()