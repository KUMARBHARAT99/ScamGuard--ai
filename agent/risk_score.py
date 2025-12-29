"""
Risk scoring logic (0–100).
"""

def calculate_risk(indicator_count: int) -> int:
    if indicator_count >= 4:
        return 90
    if indicator_count == 3:
        return 75
    if indicator_count == 2:
        return 55
    if indicator_count == 1:
        return 30
    return 10
