import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

# Navigate to Etherscan
driver.get("https://etherscan.io")

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search by Address / Txn Hash / Block / Token / Domain Name']")))

# Search for the address
search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search by Address / Txn Hash / Block / Token / Domain Name']")
search_bar.send_keys("fake_phishing180001")
search_bar.send_keys(Keys.RETURN)

# Wait for human verification (captcha) page to appear and complete it manually
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "alert-danger")))

# Wait for the results page to load
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "card-body")))

# Extract the address from the result page
address = driver.find_element(By.XPATH, "//a[contains(@href, 'address')]").text

# Create a DataFrame and save it as CSV
df = pd.DataFrame({"Address": [address]})
df.to_csv("address.csv", index=False)

# Close the browser
driver.quit()
