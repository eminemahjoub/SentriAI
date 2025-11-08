from unittest import TestCase
from src.alerting.alert_dispatcher import AlertDispatcher
from src.alerting.alert_rules import AlertRule

class TestAlertFlow(TestCase):
    def setUp(self):
        self.alert_dispatcher = AlertDispatcher()
        self.alert_rule = AlertRule()

    def test_alert_creation(self):
        # Simulate an event that triggers an alert
        event = {
            'event_type': 'suspicious_login',
            'user': 'malicious_user',
            'timestamp': '2023-10-01T12:00:00Z'
        }
        alert = self.alert_rule.evaluate(event)
        self.assertIsNotNone(alert)
        self.assertEqual(alert['event_type'], 'suspicious_login')

    def test_alert_dispatch(self):
        # Create a sample alert
        alert = {
            'event_type': 'suspicious_login',
            'user': 'malicious_user',
            'timestamp': '2023-10-01T12:00:00Z',
            'severity': 'high'
        }
        result = self.alert_dispatcher.dispatch(alert)
        self.assertTrue(result)  # Assuming dispatch returns True on success

    def test_multiple_alerts_dispatch(self):
        alerts = [
            {
                'event_type': 'suspicious_login',
                'user': 'malicious_user',
                'timestamp': '2023-10-01T12:00:00Z',
                'severity': 'high'
            },
            {
                'event_type': 'lateral_movement',
                'user': 'malicious_user',
                'timestamp': '2023-10-01T12:05:00Z',
                'severity': 'critical'
            }
        ]
        results = [self.alert_dispatcher.dispatch(alert) for alert in alerts]
        self.assertTrue(all(results))  # All alerts should be dispatched successfully

if __name__ == '__main__':
    unittest.main()