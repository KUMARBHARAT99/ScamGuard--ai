# backend/runner.py

import time
from backend.email_reader import fetch_unread_emails
from backend.email_worker import process_email

print("📡 ScamGuard Email Listener started...")

while True:
    emails = fetch_unread_emails()

    for raw_email in emails:
        process_email(raw_email)

    time.sleep(30)
    print("⏱ Waiting for new emails...")