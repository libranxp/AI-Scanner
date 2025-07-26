import os
from datetime import datetime, timedelta

class AlertScheduler:
    def __init__(self):
        self.peak_start_time = datetime.strptime(os.environ['PEAK_START_TIME'], "%H:%M").time()
        self.peak_end_time = datetime.strptime(os.environ['PEAK_END_TIME'], "%H:%M").time()

        self.alert_interval_penny_peak = int(os.environ['ALERT_INTERVAL_PENNY_PEAK'])
        self.alert_interval_penny_off = int(os.environ['ALERT_INTERVAL_PENNY_OFF'])
        self.alert_interval_crypto = int(os.environ['ALERT_INTERVAL_CRYPTO'])

        self.last_alert_penny = datetime.utcnow() - timedelta(minutes=10)
        self.last_alert_stock = datetime.utcnow() - timedelta(minutes=10)
        self.last_alert_crypto = datetime.utcnow() - timedelta(minutes=10)

    def is_peak_hours(self, current_time):
        return self.peak_start_time <= current_time.time() <= self.peak_end_time

    def should_alert_penny(self):
        now = datetime.utcnow()
        interval = self.alert_interval_penny_peak if self.is_peak_hours(now) else self.alert_interval_penny_off
        if (now - self.last_alert_penny).total_seconds() >= interval:
            self.last_alert_penny = now
            return True
        return False

    def should_alert_stock(self):
        now = datetime.utcnow()
        if (now - self.last_alert_stock).total_seconds() >= self.alert_interval_penny_peak:
            self.last_alert_stock = now
            return True
        return False

    def should_alert_crypto(self):
        now = datetime.utcnow()
        if (now - self.last_alert_crypto).total_seconds() >= self.alert_interval_crypto:
            self.last_alert_crypto = now
            return True
        return False
