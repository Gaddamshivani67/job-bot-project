import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def send_email_notification(job):
    if not all([SENDER_EMAIL, RECEIVER_EMAIL, SENDER_PASSWORD]):
        raise ValueError("❌ Missing environment variables. Please check your .env file.")

    # Use `.get()` to avoid KeyError
    subject = f"✅ Applied for {job.get('title', 'Unknown Title')}"
    body = f"""
Hi Shivani,

You successfully applied for:

🎯 Title: {job.get('title', 'N/A')}
🏢 Company: {job.get('company', 'N/A')}
🔗 Link: {job.get('url', 'N/A')}

Keep going!

– Your Job Bot
"""

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)

    print(f"📧 Email sent for {job.get('title', 'Unknown Title')}")

