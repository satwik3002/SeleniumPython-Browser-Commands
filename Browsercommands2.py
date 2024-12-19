import time
from selenium import webdriver

# Initialize the WebDriver (ensure WebDriver path is set in the system PATH or provide it explicitly)
driver = webdriver.Chrome()

# Open the first URL
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(5)

# Navigate to the second URL
driver.get("https://www.google.com")
time.sleep(5)

# Navigate back to the previous page
driver.back()
time.sleep(5)

# Navigate forward to the next page
driver.forward()
time.sleep(5)

# Refresh the current page
driver.refresh()
time.sleep(5)

# Print page details
print(f"Page Source: {driver.page_source[:500]}...")  # Print the first 500 characters of the page source
print(f"Current URL: {driver.current_url}")  # Corrected to current_url
print(f"Page Title: {driver.title}")  # Corrected to title

# Close the browser
driver.quit()
