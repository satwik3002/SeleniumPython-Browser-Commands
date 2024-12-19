from selenium import webdriver
import time

# Base URL
baseURL = "http://automationpractice.com/index.php"

# Initialize Edge WebDriver
driver = webdriver.Edge()

# Open the URL
driver.get(baseURL)
print("Opened URL:", baseURL)
time.sleep(2)  # Wait for the page to load

# 1. Get and print the page title
title = driver.title
print(f"Page Title: {title}")

# 2. Get and print the page title length
title_length = len(title)
print(f"Title Length: {title_length}")

# 3. Get the current URL and verify if it's the desired page
current_url = driver.current_url
print(f"Current URL: {current_url}")

if current_url == baseURL:
    print("The page URL is correct.")
else:
    print("The page URL is incorrect.")

# 4. Get the page source and its length
page_source = driver.page_source
page_source_length = len(page_source)
print(f"Page Source Length: {page_source_length}")

# 5. Close the browser
driver.quit()
print("Browser closed.")
