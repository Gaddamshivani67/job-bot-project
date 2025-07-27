import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from .env file
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")      
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

def send_email_notification(job):
    try:
        subject = f"Job Alert: {job['title']} at {job['company']}"
        body = f"New job found!\n\nTitle: {job['title']}\nCompany: {job['company']}\nLink: {job['url']}"

        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

        print("✅ Email notification sent successfully!")

    except Exception as e:
        print("❌ Error sending email:", e)
