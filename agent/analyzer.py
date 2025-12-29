"""
Scam message analysis module.
Detects common scam indicators using rule-based NLP.
"""

def analyze_message(text: str) -> dict:
    text = text.lower()
    indicators = []

    urgency = [
        "urgent", "immediately", "act now", "limited time",
        "24 hours", "expires", "today only"
    ]

    authority = [
        "bank", "government", "irs", "income tax",
        "police", "security team", "official"
    ]

    threat = [
        "account locked", "suspended", "blocked",
        "compromised", "frozen", "legal action"
    ]

    links = [
        "http", "https", "www", "bit.ly", "tinyurl"
    ]

    if any(word in text for word in urgency):
        indicators.append("Urgency pressure detected")

    if any(word in text for word in authority):
        indicators.append("Authority impersonation detected")

    if any(word in text for word in threat):
        indicators.append("Threat-based manipulation detected")

    if any(word in text for word in links):
        indicators.append("Suspicious link present")

    return {
        "indicators": indicators,
        "count": len(indicators)
    }
