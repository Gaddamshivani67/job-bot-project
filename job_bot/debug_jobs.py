from job_scraper.internshala import fetch_internshala_jobs

jobs = fetch_internshala_jobs("python developer")

print("🔍 Found", len(jobs), "jobs.")
print("\n🧾 First job details:\n")
print(jobs[0])
