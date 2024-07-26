import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    # Setup WebDriver to connect to a new browser session
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    
    # Path to the chromedriver executable
    chromedriver_path = '/usr/local/bin/chromedriver'
    
    # Create a Service object with the path to chromedriver
    service = Service(chromedriver_path)
    
    # Initialize WebDriver with the service and options
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def perform_search(driver, search_term):
    # Navigate to Etherscan
    driver.get("https://etherscan.io/")
    try:
        search_bar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="search-panel"]'))
        )
        # Clear the search bar and enter the search term
        search_bar.clear()
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.RETURN)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mainaddress"]'))
        )
    except Exception as e:
        print(f"Error occurred during search: {e}")

def extract_address(driver):
    # Locate the address element using the provided XPath
    try:
        address_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mainaddress"]'))
        )
        address = address_element.text.strip()
        return address
    except Exception as e:
        print(f"Error occurred while extracting address: {e}")
        return None

def save_address_to_csv(address, filename):
    if address:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([address])

if __name__ == "__main__":
    driver = setup_driver()
    
    try:
        for i in range(180001, 180101):
            search_term = f"Fake_Phishing{i:06d}"
            perform_search(driver, search_term)
            address = extract_address(driver)
            
            if address:
                # Print the captured address for each search term
                print(f"Captured address for {search_term}: {address}")
                
                # Save address to CSV
                save_address_to_csv(address, 'etherscan_addresses.csv')
            else:
                print(f"Failed to capture address for {search_term}")
    
        print("All addresses saved to etherscan_addresses.csv")
    
    finally:
        # Close the driver
        driver.quit()
