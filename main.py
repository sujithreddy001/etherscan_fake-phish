import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    time.sleep(3)  # Wait for the page to load

    # Find the search bar using the provided XPath and enter the search term
    search_bar = driver.find_element(By.XPATH, '//*[@id="search-panel"]')
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for the search results to load

def extract_addresses(driver):
    addresses = []
    # Locate the addresses on the result page
    results = driver.find_elements(By.XPATH, '//a[contains(@href, "/address/")]')
    for result in results:
        address = result.get_attribute('href').split('/')[-1]
        addresses.append(address)
    return addresses

def save_addresses_to_csv(addresses, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        for address in addresses:
            writer.writerow([address])

if __name__ == "__main__":
    driver = setup_driver()
    
    try:
        for i in range(180001, 180101):
            search_term = f"Fake_Phishing{i:06d}"
            perform_search(driver, search_term)
            addresses = extract_addresses(driver)
            
            # Print the captured addresses for each search term
            print(f"Captured addresses for {search_term}:")
            for address in addresses:
                print(address)
            
            # Save addresses to CSV
            save_addresses_to_csv(addresses, 'etherscan_addresses.csv')
    
        print("All addresses saved to etherscan_addresses.csv")
    
    finally:
        # Close the driver
        driver.quit()
