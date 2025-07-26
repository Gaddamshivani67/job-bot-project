import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load credentials from .env
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")
RESUME_PATH = os.path.abspath("resume.pdf")  # Ensure this is correct

print(f"✅ Resume path: {RESUME_PATH}")

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")

# Start WebDriver
driver = webdriver.Chrome(options=options)

# -------------------- STEP 1: LOGIN --------------------
driver.get("https://www.linkedin.com/login")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

print("🔐 Logged in successfully.")
time.sleep(3)

# -------------------- STEP 2: OPEN JOB PAGE --------------------
# Example job URL (replace with actual LinkedIn Easy Apply job URL)
job_url =  "https://www.linkedin.com/jobs/view/4265138246"
 # Replace this!
driver.get(job_url)
print("🔍 Opened job posting...")
time.sleep(3)

# -------------------- STEP 3: CLICK EASY APPLY --------------------
try:
    easy_apply_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Easy Apply")]'))
    )
    easy_apply_btn.click()
    print("✅ Easy Apply button clicked.")
except Exception as e:
    print("❌ Could not find Easy Apply button:", e)
    driver.quit()
    exit()

time.sleep(3)

# -------------------- STEP 4: UPLOAD RESUME --------------------
try:
    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
    )
    upload_input.send_keys(RESUME_PATH)
    print("📄 Resume uploaded successfully.")
except Exception as e:
    print("❌ Error uploading resume:", e)
    driver.quit()
    exit()

time.sleep(3)

# -------------------- STEP 5: SUBMIT APPLICATION --------------------
try:
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Submit application")]'))
    )
    submit_btn.click()
    print("🎉 Application submitted!")
except Exception:
    print("⚠️ Manual steps required: Additional form fields might exist.")

driver.quit()
