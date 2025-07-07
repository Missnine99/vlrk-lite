from vlrk.scoring import calculate_score

def test_score():
    config = {'threshold': 5, 'weights': {'fraud_warning': 3}}
    issues = {'fraud_warning': 2}
    assert calculate_score(issues, config) == 6
