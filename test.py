from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

def capture_search_url(driver, search_query):
    # Go to the home page
    driver.get('https://etherscan.io')

    # Wait for the search bar to be ready and visible
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search by Address / Txn Hash / Block / Token / Domain Name"]'))
    )

    # Find the search bar and input the search query
    search_bar = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search by Address / Txn Hash / Block / Token / Domain Name"]')
    search_bar.clear()
    search_bar.send_keys(search_query + Keys.RETURN)

    # Wait until the URL changes to contain the search query
    WebDriverWait(driver, 10).until(
        lambda d: "q={}".format(search_query) in d.current_url
    )

    # Capture the current URL which now contains the search query
    current_url = driver.current_url
    return current_url

def save_url_to_csv(url, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL'])  # Write the header
        writer.writerow([url])    # Write the URL

# Setup WebDriver
driver = webdriver.Chrome()

# Search query
search_query = 'Fake_Phishing180000'  # Modify as needed for different queries

# Capture the URL from the search
search_url = capture_search_url(driver, search_query)
print(f"Captured URL: {search_url}")

driver.quit()

# Save the captured URL to a CSV file
save_url_to_csv(search_url, 'Etherscan_Search_URL.csv')
