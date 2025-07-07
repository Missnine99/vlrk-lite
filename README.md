# VLRK-Lite: Advanced QA and Anomaly Detection Framework

**VLRK-Lite** is a modular, real-time framework designed to monitor QA failures, detect anomalies, and simulate fraud triggers in high-risk, high-regulation environments such as sports betting and streaming platforms.

## Features
- Real-time issue tracking and categorization
- Configurable issue weights and thresholds
- Scoring system for anomaly detection
- Mock alert system
- YAML-based configuration for easy reuse

## Install
Clone this repo and run:
```
pip install -e .
```

## Basic Usage
```python
from vlrk.core import VLRKMonitor

monitor = VLRKMonitor(config_path="config/default_config.yml")
monitor.record_issue("login_timeout")
monitor.record_issue("login_timeout")
monitor.record_issue("fraud_warning")
monitor.check_anomalies()
```

MIT License. Created by Anna Deviatko.
