applied_jobs = set()

def already_applied(url):
    return url in applied_jobs

def log_application(job):
    applied_jobs.add(job['url'])
