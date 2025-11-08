class AlertDispatcher:
    def __init__(self, alert_config):
        self.alert_config = alert_config

    def send_alert(self, alert_message):
        if self.alert_config['method'] == 'email':
            self.send_email(alert_message)
        elif self.alert_config['method'] == 'telegram':
            self.send_telegram(alert_message)
        elif self.alert_config['method'] == 'slack':
            self.send_slack(alert_message)
        elif self.alert_config['method'] == 'discord':
            self.send_discord(alert_message)

    def send_email(self, alert_message):
        # Logic to send alert via email
        print(f"Sending email alert: {alert_message}")

    def send_telegram(self, alert_message):
        # Logic to send alert via Telegram
        print(f"Sending Telegram alert: {alert_message}")

    def send_slack(self, alert_message):
        # Logic to send alert via Slack
        print(f"Sending Slack alert: {alert_message}")

    def send_discord(self, alert_message):
        # Logic to send alert via Discord
        print(f"Sending Discord alert: {alert_message}")