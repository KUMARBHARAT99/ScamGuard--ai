"""
Generates explainable output for users.
"""

def generate_explanation(indicators: list, risk: int) -> str:
    result = ""

    if risk >= 80:
        result += "🚨 HIGH RISK SCAM DETECTED\n\n"
    elif risk >= 40:
        result += "⚠️ SUSPICIOUS MESSAGE\n\n"
    else:
        result += "✅ LIKELY SAFE MESSAGE\n\n"

    result += "Why this decision was made:\n"

    if indicators:
        for item in indicators:
            result += f"- {item}\n"
    else:
        result += "- No scam indicators found\n"

    result += f"\nRisk Score: {risk}/100\n\n"

    if risk >= 80:
        result += (
            "Recommended Action:\n"
            "- Do NOT click links\n"
            "- Do NOT reply to sender\n"
            "- Report this message immediately\n"
        )
    elif risk >= 40:
        result += (
            "Recommended Action:\n"
            "- Verify through official website\n"
            "- Do not share personal information\n"
        )
    else:
        result += (
            "Recommended Action:\n"
            "- Message appears safe\n"
            "- Stay cautious and alert\n"
        )

    return result

