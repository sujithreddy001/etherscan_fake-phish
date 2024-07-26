# Etherscan Address Extraction Script

This script automates the process of searching for Ethereum addresses on Etherscan using a range of search terms (`Fake_Phishing180001` to `Fake_Phishing180100`), extracts the addresses displayed in the search results, and saves them to a CSV file.

## Prerequisites

- Python 3.6 or higher
- Selenium package
- Chrome browser
- ChromeDriver

## Installation

1. **Clone the repository or download the script:**

    ```sh
    git clone https://github.com/yourusername/etherscan_address_extraction.git
    cd etherscan_address_extraction
    ```

2. **Install the required Python packages:**

    ```sh
    pip install selenium
    ```

3. **Download ChromeDriver:**

    - Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/downloads).
    - Download the version that matches your installed version of Chrome.
    - Move the `chromedriver` executable to `/usr/local/bin`:

    ```sh
    sudo mv ~/Downloads/chromedriver /usr/local/bin/chromedriver
    sudo chmod +x /usr/local/bin/chromedriver
    ```

## Usage

1. **Start Chrome in Debugging Mode:**

    Open Terminal and run:

    ```sh
    open -na "Google Chrome" --args --remote-debugging-port=9222 --user-data-dir="$HOME/chromedev"
    ```

2. **Run the Python Script:**

    ```sh
    python trail.py
    ```

## Script Explanation

The script performs the following steps:

1. **Setup WebDriver:**

    - Connects to a new browser session using ChromeDriver.

2. **Perform Search:**

    - Refreshes the Etherscan page before each search.
    - Waits for the search bar to be present on the page.
    - Enters the search term in the format `Fake_PhishingXXXXXX` where `XXXXXX` ranges from `180001` to `180100`.
    - Simulates pressing the Enter key to submit the search.
    - Waits for the address element to be present on the page.

3. **Extract Address:**

    - Waits for the address element using the provided XPath (`//*[@id="mainaddress"]`).
    - Extracts the text of the address element.

4. **Save Address to CSV:**

    - Saves the extracted address to a CSV file, appending each result if the address is not `None`.

5. **Loop Through Search Terms:**

    - Iterates over the search terms from `Fake_Phishing180001` to `Fake_Phishing180100`.

## Example Output

The script will create a CSV file named `etherscan_addresses.csv` containing the extracted addresses, with each address on a new line.

```csv
0x4d911CF0A007e6fcA2d8946F1a0D2bA91D0a5d50
0x7eBD915c41bCfc82A5a6fA5A78eD4fEe2d94Db1f
...
Troubleshooting
If you encounter any issues, ensure that:

Chrome is running in debugging mode.
The correct version of ChromeDriver is installed and accessible in your PATH.
The necessary Python packages are installed.
License
This project is licensed under the MIT License.

perl
Copy code

### Pushing to GitHub

To push your project including the `README.md` to GitHub, follow these steps:

1. **Ensure you have initialized your git repository** (if not already done):

    ```sh
    git init
    ```

2. **Stage your changes**:

    ```sh
    git add .
    ```

3. **Commit your changes**:

    ```sh
    git commit -m "Add initial script and README"
    ```

4. **Add your GitHub repository as a remote**:

    ```sh
    git remote add origin https://github.com/yourusername/etherscan_address_extraction.git
    ```

5. **Push your changes to GitHub**:

    ```sh
    git push -u origin master
    ```

If your default branch is `main`, use:

```sh
git push -u origin main
By following these steps, your project including the README.md file should be pushed to GitHub and visible in your repository. If you encounter any issues, feel free to ask for further assistance!






