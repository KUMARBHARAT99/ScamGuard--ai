# backend/email_reader.py

import os
from dotenv import load_dotenv
from imapclient import IMAPClient

load_dotenv()  #  THIS LINE IS THE FIX like used for read the message by llm

EMAIL = os.getenv("SCAMGUARD_EMAIL")
PASSWORD = os.getenv("SCAMGUARD_EMAIL_PASS")

def fetch_unread_emails():
    if not EMAIL or not PASSWORD:
        raise ValueError("Email or App Password not loaded from .env")

    server = IMAPClient("imap.gmail.com", ssl=True)
    server.login(EMAIL, PASSWORD)
    server.select_folder("INBOX")

    messages = server.search(["UNSEEN"])
    emails = []

    for uid in messages:
        raw = server.fetch(uid, ["RFC822"])
        emails.append(raw[uid][b"RFC822"])

    server.logout()
    return emails
