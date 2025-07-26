import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

# Load .env from one folder up
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(dotenv_path)


def login_linkedin(driver, email, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
    time.sleep(3)

def fetch_linkedin_jobs(query="python intern", location="remote", max_jobs=5):
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")

    if not email or not password:
        raise ValueError("Set LINKEDIN_EMAIL and LINKEDIN_PASSWORD in your .env")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    jobs = []

    try:
        login_linkedin(driver, email, password)

        search_url = f"https://www.linkedin.com/jobs/search/?keywords={query}&location={location}&f_TPR=r86400&f_WT=2"
        driver.get(search_url)
        time.sleep(5)

        job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")

        for card in job_cards[:max_jobs]:
            try:
                title = card.find_element(By.CLASS_NAME, "job-card-list__title").text
                company = card.find_element(By.CLASS_NAME, "job-card-container__company-name").text
                job_url = card.find_element(By.CLASS_NAME, "job-card-list__title").get_attribute("href")
                location = card.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text

                jobs.append({
                    "title": title,
                    "company": company,
                    "url": job_url,
                    "location": location,
                    "platform": "LinkedIn"
                })

            except Exception as e:
                print("Error reading a job card:", e)

        return jobs

    finally:
        driver.quit()
print("Scraper started...")

if __name__ == "__main__":
    print("Running scraper.py")

    # Example call
    # jobs = scrape_linkedin_jobs("python intern", location="India")
    # print(jobs)
