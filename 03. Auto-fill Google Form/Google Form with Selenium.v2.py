# Step 1: Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Step 2: Define Chrome options and service
chrome_options = Options()
service = ChromeService()

# Step 3: Initialize Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Step 4: Define form URL and data
form_url = "https://forms.gle/Szpu6TLVKzhAtEkb9"
data = [
    ['JDE student', 'JDE@gmail.com', '123456789', '2474 Hong Kong SAR', 'NA'],
    ['JDE Instructor', 'JDE2@gmail.com', '987654321', '2143 Singapore', 'NA']
]

# Step 5: Define XPath locators
name_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
email_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
phone_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input"
address_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea"
comments_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea"
submit_button_xpath = "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span"
confirmation_xpath = "/html/body/div[1]/div[2]/div[1]/div/div[3]"

# Step 6: Iterate through each data entry
for entry in data:
    driver.get(form_url)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, email_xpath)))

    # Fill form fields
    name, email, phone, address, comments = entry
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, email_xpath))).send_keys(email)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, name_xpath))).send_keys(name)
    
    try:
        phone_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, phone_xpath)))
        phone_input.send_keys(phone)
    except TimeoutException:
        print("Phone input not found. Check if it appears after filling the previous fields.")

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, address_xpath))).send_keys(address)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, comments_xpath))).send_keys(comments)

    # Submit form
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
    submit_button.click()

    # Check for submission confirmation
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, confirmation_xpath)))
        print("Form submitted successfully.")
    except TimeoutException:
        print("Form submission failed or confirmation message not found.")

# Step 7: Close browser
#driver.quit()