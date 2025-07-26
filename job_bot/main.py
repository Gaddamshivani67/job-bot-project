import sys
import os

# Add parent directory to path for proper imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from job_scraper.internshala import fetch_internshala_jobs
from utils.cover_letter_generator import generate_cover_letter
from auto_apply.form_filler import auto_apply_to_job
from auto_apply.tracker import log_application, already_applied
from utils.email_notifier import send_email_notification

def main():
    print("🚀 Job bot started...")

    # Fetch jobs (modify query as needed)
    jobs = fetch_internshala_jobs("python developer")
    print(f"🔍 Found {len(jobs)} jobs.")

    # Define your skills
    skills = ["Python", "Data Analysis", "Machine Learning"]

    for job in jobs:
        if already_applied(job["url"]):
            print(f"⏩ Already applied to {job['title']}")
            continue

        print(f"Applying to {job['title']}")
        
        # Generate a cover letter
        cover_letter = generate_cover_letter(job, skills)

        # Try to auto-apply
        applied = auto_apply_to_job(job, cover_letter)
        if applied:
            log_application(job)  # Log this application
            print("DEBUG JOB STRUCTURE:", job)

            send_email_notification(job)  # Notify via email

if __name__ == "__main__":
    main()
