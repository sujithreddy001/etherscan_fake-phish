import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Function to set Chrome options to avoid detection
def set_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    return options

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
options = set_chrome_options()
driver = webdriver.Chrome(service=service, options=options)

# Additional JavaScript to further avoid detection
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        window.navigator.chrome = {
            runtime: {}
        };
        Object.defineProperty(navigator, 'languages', {
            get: () => ['en-US', 'en']
        });
        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3, 4, 5]
        });
    """
})

# Navigate to the Etherscan page
driver.get('https://etherscan.io/search?f=0&q=Fake_Phishing180000')

try:
    # Wait for the address element to be present
    address_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mainaddress"]'))
    )

    # Extract the address text
    address = address_element.text

    # Debugging: Print the address to console
    print("Extracted Address:", address)

    # Create a DataFrame and save it as CSV
    df = pd.DataFrame({"Address": [address]})
    df.to_csv("address.csv", index=False)
    print("Address saved to address.csv")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    # Close the browser
    driver.quit()
