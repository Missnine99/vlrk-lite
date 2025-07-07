def calculate_score(issues, config):
    score = 0
    for issue_type, count in issues.items():
        weight = config['weights'].get(issue_type, 1)
        score += count * weight
    print(f"Anomaly score: {score}")
    return score
