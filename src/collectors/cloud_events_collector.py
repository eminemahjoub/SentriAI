class CloudEventsCollector:
    def __init__(self, source):
        self.source = source

    def collect(self):
        # Logique pour collecter les événements des services cloud
        # Cela pourrait impliquer des appels API aux services cloud
        # et la récupération des logs
        pass

    def normalize(self, raw_event):
        # Logique pour normaliser les événements collectés en format JSON
        normalized_event = {
            "event_type": raw_event.get("eventType"),
            "timestamp": raw_event.get("timestamp"),
            "source": self.source,
            "data": raw_event.get("data"),
        }
        return normalized_event

    def run(self):
        # Méthode principale pour exécuter le collecteur
        raw_events = self.collect()
        normalized_events = [self.normalize(event) for event in raw_events]
        return normalized_events