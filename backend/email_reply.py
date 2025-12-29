import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = os.getenv("SCAMGUARD_EMAIL")
PASSWORD = os.getenv("SCAMGUARD_EMAIL_PASS")


def send_auto_reply(to_email, risk_score, explanation):
    """
    Send automatic reply based on risk score
    """

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = to_email

    # -------- SUBJECT --------
    if risk_score >= 70:
        msg["Subject"] = "[SCAM] 🚨 ScamGuard Alert: High Risk Email"
        verdict = "🚨 HIGH RISK SCAM DETECTED"
    elif risk_score >= 40:
        msg["Subject"] = "[WARNING] ⚠️ ScamGuard Alert: Suspicious Email"
        verdict = "⚠️ SUSPICIOUS MESSAGE"
    else:
        msg["Subject"] = "[SAFE] ✅ ScamGuard Result: Message Looks Safe"
        verdict = "✅ LIKELY SAFE MESSAGE"

    # -------- BODY --------
    body = f"""
Hello,

ScamGuard AI has analyzed the email you forwarded.

Result:
{verdict}

Risk Score: {risk_score}/100

Explanation:
{explanation}

Safety Tips:
- Do NOT click unknown links
- Do NOT share OTPs or passwords
- Verify sender from official website
- Report suspicious emails

Stay Safe,
🛡 ScamGuard AI
"""

    msg.attach(MIMEText(body, "plain"))

    # -------- SEND EMAIL --------
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        print("📤 Auto-reply sent successfully")

    except Exception as e:
        print("❌ Failed to send auto-reply:", e)
