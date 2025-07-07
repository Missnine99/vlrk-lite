import yaml
from vlrk.scoring import calculate_score
from vlrk.alert import trigger_alert

class VLRKMonitor:
    def __init__(self, config_path):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
        self.issues = {}

    def record_issue(self, issue_type):
        if issue_type not in self.issues:
            self.issues[issue_type] = 0
        self.issues[issue_type] += 1
        print(f"Issue recorded: {issue_type} ({self.issues[issue_type]})")

    def check_anomalies(self):
        score = calculate_score(self.issues, self.config)
        if score >= self.config['threshold']:
            trigger_alert(score)
