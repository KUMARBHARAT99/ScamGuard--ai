from email import message_from_bytes
from email.utils import parseaddr

from agent.analyzer import analyze_message
from agent.risk_score import calculate_risk
from agent.explanation import generate_explanation
from backend.email_reply import send_auto_reply


def process_email(raw_email: bytes):
    # 1️⃣ Parse raw email properly
    msg = message_from_bytes(raw_email)

    # 2️⃣ Extract sender email
    from_name, from_email = parseaddr(msg.get("From"))

    # 3️⃣ Extract subject
    subject = msg.get("Subject", "")

    # 4️⃣ Extract body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode(errors="ignore")
                break
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")

    full_message = subject + "\n" + body

    # 5️⃣ Analyze message
    analysis = analyze_message(full_message)
    risk = calculate_risk(analysis["count"])
    explanation = generate_explanation(
        analysis["indicators"], risk
    )

    print(f"📨 From: {from_email}")
    print(f"⚠️ Risk Score: {risk}")

    # 6️⃣ Send auto reply to ORIGINAL SENDER
    send_auto_reply(
        to_email=from_email,
        risk_score=risk,
        explanation=explanation,
    )

    print("✅ Auto-reply sent\n")


