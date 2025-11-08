class CorrelationEngine:
    def __init__(self, alert_rules, anomaly_detection_model):
        self.alert_rules = alert_rules
        self.anomaly_detection_model = anomaly_detection_model

    def apply_rules(self, events):
        alerts = []
        for rule in self.alert_rules:
            alerts.extend(rule.evaluate(events))
        return alerts

    def detect_anomalies(self, events):
        anomalies = self.anomaly_detection_model.predict(events)
        return anomalies

    def run(self, events):
        alerts = self.apply_rules(events)
        anomalies = self.detect_anomalies(events)
        return alerts, anomalies