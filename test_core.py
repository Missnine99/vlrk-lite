from vlrk.core import VLRKMonitor

def test_basic_flow():
    monitor = VLRKMonitor(config_path="config/default_config.yml")
    monitor.record_issue("login_timeout")
    monitor.record_issue("login_timeout")
    monitor.record_issue("fraud_warning")
    monitor.check_anomalies()
