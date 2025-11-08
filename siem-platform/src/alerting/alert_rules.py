class AlertRule:
    def __init__(self, name, description, condition, action):
        self.name = name
        self.description = description
        self.condition = condition
        self.action = action

    def evaluate(self, event):
        if self.condition(event):
            self.trigger_alert(event)

    def trigger_alert(self, event):
        print(f"Alert triggered: {self.name} - {self.description}")
        self.action(event)


def suspicious_login_condition(event):
    return event.get('event_type') == 'login' and event.get('status') == 'failed'


def send_email_alert(event):
    print(f"Sending email alert for event: {event}")


suspicious_login_rule = AlertRule(
    name="Suspicious Login Attempt",
    description="Triggers when there is a failed login attempt.",
    condition=suspicious_login_condition,
    action=send_email_alert
)