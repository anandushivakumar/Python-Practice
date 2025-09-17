import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_EMAIL = "anandu@test.com"
ACCOUNT_PASSWORD = "testpassword123"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), r"py_bootcamp\d49_gym_project\chrome_profile")
chrome_options.add_argument(f"user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 2)

# login
login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

# find email input
email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
# enter email
email_input.send_keys(ACCOUNT_EMAIL)

# find password input
password_input = driver.find_element(By.ID, "password-input")
password_input.clear()
# enter password
password_input.send_keys(ACCOUNT_PASSWORD)

# submit button
submit_button = driver.find_element(By.ID, value = "submit-button")
submit_button.click()

# wait for page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# check if class is already booked
check_if_booked = wait.until(ec.presence_of_element_located((By.ID, "book-button-spin-2025-09-23-1800")))
if check_if_booked.text == "Waitlisted" or check_if_booked.text == "Booked":
    print("Class already booked!")
    driver.quit()
else:
    join_button = wait.until(ec.element_to_be_clickable((By.ID, "book-button-spin-2025-09-23-1800")))
    join_button.click()
    print("Class booked!")

# driver.quit()