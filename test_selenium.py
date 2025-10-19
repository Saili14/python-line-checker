from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure headless Chrome (no visible window)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start Chrome
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

print("Title:", driver.title)
driver.quit()
