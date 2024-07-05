from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Initialize the service
service = Service('/home/shital/Downloads/chromedriver')

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

# Create a new instance of the Chrome driver with the specified options
driver = webdriver.Remote(service.service_url, chrome_options)

# Navigate to a webpage
driver.get("http://www.google.com")
print(driver.title)
driver.quit()
