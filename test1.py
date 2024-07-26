import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def extract_addresses_from_etherscan():
    # Setup WebDriver to connect to the existing browser session
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    
    # Path to the chromedriver executable
    chromedriver_path = '/usr/local/bin/chromedriver'
    
    # Create a Service object with the path to chromedriver
    service = Service(chromedriver_path)
    
    # Initialize WebDriver with the service and options
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Wait for the user to manually login and search
        time.sleep(10)  # Adjust sleep time as necessary
        
        # Extract addresses from the search results
        addresses = extract_addresses(driver)
        return addresses
        
    finally:
        # Close the driver, but keep the browser open
        driver.quit()

def extract_addresses(driver):
    addresses = []
    # Locate the addresses on the result page
    results = driver.find_elements(By.XPATH, '//a[contains(@href, "/address/")]')
    for result in results:
        address = result.get_attribute('href').split('/')[-1]
        addresses.append(address)
    return addresses

def save_addresses_to_csv(addresses, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Address"])
        for address in addresses:
            writer.writerow([address])

if __name__ == "__main__":
    search_term = "fake_phishing180824"
    addresses = extract_addresses_from_etherscan()
    
    # Print the captured addresses
    print("Captured addresses:")
    for address in addresses:
        print(address)
    
    # Save addresses to CSV
    save_addresses_to_csv(addresses, 'etherscan_addresses.csv')
    print("Addresses saved to etherscan_addresses.csv")
