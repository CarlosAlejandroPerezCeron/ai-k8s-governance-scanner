def calculate_risk(findings):
    score = len(findings)

    if score >= 6:
        return "CRITICAL"
    elif score >= 4:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    elif score >= 1:
        return "LOW"
    return "CLEAN"
