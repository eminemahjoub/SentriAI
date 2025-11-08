import pytest
from src.pipeline.ingest_service import IngestService
from src.pipeline.parser_service import ParserService
from src.storage.elastic.es_client import ESClient

@pytest.fixture
def setup_services():
    es_client = ESClient()
    ingest_service = IngestService(es_client)
    parser_service = ParserService()
    return ingest_service, parser_service

def test_ingest_and_parse_logs(setup_services):
    ingest_service, parser_service = setup_services

    # Simulate log ingestion
    sample_log = {
        "source": "syslog",
        "message": "Test log message",
        "timestamp": "2023-10-01T12:00:00Z"
    }
    ingest_service.ingest(sample_log)

    # Simulate log parsing
    parsed_log = parser_service.parse(sample_log)

    assert parsed_log is not None
    assert parsed_log['source'] == "syslog"
    assert parsed_log['message'] == "Test log message"
    assert 'parsed_timestamp' in parsed_log

def test_elasticsearch_integration(setup_services):
    ingest_service, _ = setup_services

    sample_log = {
        "source": "cloud",
        "message": "Cloud log message",
        "timestamp": "2023-10-01T12:00:00Z"
    }
    ingest_service.ingest(sample_log)

    # Verify that the log is stored in Elasticsearch
    logs = ingest_service.get_logs()
    assert len(logs) > 0
    assert logs[0]['source'] == "cloud"