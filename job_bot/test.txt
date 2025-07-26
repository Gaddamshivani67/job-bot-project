from utils.email_notifier import send_email_notification

# Dummy job data to simulate an application
dummy_job = {
    "title": "Test Python Developer",
    "company": "OpenAI",
    "url": "https://example.com/job"
}

# Call the email sending function
send_email_notification(dummy_job)
