import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

# Load credentials
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
EMAIL = os.getenv("INTERNSHALA_EMAIL")
PASSWORD = os.getenv("INTERNSHALA_PASSWORD")
RESUME_PATH = os.getenv("RESUME_PATH")

if not EMAIL or not PASSWORD:
    raise ValueError("Set INTERNSHALA_EMAIL and INTERNSHALA_PASSWORD in your .env")

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(), options=options)

def apply_internshala():
    driver.get("https://internshala.com/login")
    time.sleep(3)

    # Login
    driver.find_element(By.ID, "email").send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login_submit").click()
    time.sleep(5)

    # Go to internships
    driver.get("https://internshala.com/internships/keywords-python/")
    time.sleep(5)

    internships = driver.find_elements(By.CLASS_NAME, "individual_internship")[:3]
    print(f"\n🔍 Found {len(internships)} internships")

    for index, internship in enumerate(internships, start=1):
        try:
            internship.click()
            time.sleep(3)

            driver.switch_to.window(driver.window_handles[1])

            print(f"\n✅ Applying to internship #{index}: {driver.title}")

            if "Apply now" in driver.page_source:
                driver.find_element(By.CLASS_NAME, "btn-primary").click()
                time.sleep(2)

                if "submit" in driver.page_source:
                    driver.find_element(By.CLASS_NAME, "submit").click()
                    print("🟢 Applied successfully.")
                else:
                    print("⚠️ Cannot apply directly or already applied.")
            else:
                print("⚠️ No Apply Now button.")

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
        except Exception as e:
            print(f"❌ Error: {e}")

    driver.quit()

if __name__ == "__main__":
    apply_internshala()
