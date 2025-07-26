# job_bot/job_scraper/internshala.py

def fetch_internshala_jobs(query):
    jobs = []

    # Simulated jobs with added company field
    job1 = {
        "title": "Data Science Intern",
        "company": "ABC Corp",
        "url": "https://internshala.com/job1"
    }

    job2 = {
        "title": "Software Intern",
        "company": "XYZ Ltd",
        "url": "https://internshala.com/job2"
    }

    jobs.extend([job1, job2])
    return jobs
