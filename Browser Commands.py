from selenium import webdriver
import time

# Base URL
baseURL = "https://www.google.com"

# Initialize WebDriver
driver = webdriver.Chrome()

# 1. Open the URL
driver.get(baseURL)
print("Opened URL:", baseURL)
time.sleep(2)  # Wait for the page to load

# 2. Maximize the browser window
driver.maximize_window()
print("Browser window maximized")
time.sleep(2)

# 3. Get and print the page title
title = driver.title
print(f"Page title: {title}")

# 4. Get and print the current URL
current_url = driver.current_url
print(f"Current URL: {current_url}")

# 5. Minimize the browser window
driver.minimize_window()
print("Browser window minimized")
time.sleep(2)

# 6. Maximize the browser window again
driver.maximize_window()
print("Browser window maximized again")
time.sleep(2)

# 7. Refresh the page
driver.refresh()
print("Page refreshed")
time.sleep(2)

# 8. Navigate to a different page (forward and back)
driver.get("https://www.bing.com")
print("Navigated to Bing")
time.sleep(2)

# Navigate back
driver.back()
print("Navigated back to Google")
time.sleep(2)

# Navigate forward
driver.forward()
print("Navigated forward to Bing")
time.sleep(2)

# 9. Fullscreen the browser window
driver.fullscreen_window()
print("Browser window is fullscreen")
time.sleep(2)

# 10. View the page source
page_source = driver.page_source
print("Page Source:")
print(page_source[:500])  # Print only the first 500 characters of the page source for brevity

# 11. Close the browser
driver.quit()
print("Browser closed")
