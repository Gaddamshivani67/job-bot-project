import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()  # Load from .env

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


def fetch_internshala_jobs():
    # Dummy job data to simulate real scraping
    jobs = [
        {"title": "Data Science Intern", "company": "ABC Corp", "url": "https://internshala.com/job1"},
        {"title": "Software Intern", "company": "XYZ Ltd", "url": "https://internshala.com/job2"}
    ]
    print(f"🔍 Found {len(jobs)} jobs.")
    return jobs


def apply_to_job(job):
    print(f"Applying to {job['title']} at {job['company']}")
    print("DEBUG JOB STRUCTURE:", job)
    # Simulated application logic (e.g., using Selenium or form submission)
    # You can add actual logic later if needed


def send_email_notification(job):
    subject = f"Applied to {job['title']} at {job['company']}"
    body = f"You applied to {job['title']} at {job['company']}\nJob URL: {job['url']}"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
            print("✅ Email sent successfully")
    except Exception as e:
        print(f"❌ Error sending email: {e}")


def main():
    print("🚀 Job bot started...")
    jobs = fetch_internshala_jobs()

    for job in jobs:
        apply_to_job(job)
        send_email_notification(job)


if __name__ == "__main__":
    main()
