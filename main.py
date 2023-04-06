from appium import webdriver
import time

# Define the desired capabilities for the iOS app
desired_caps = {
    "platformName": "iOS",
    "platformVersion": "14.4",
    "deviceName": "iPhone 12 Pro Max",
    "automationName": "XCUITest",
    "app": "<path_to_Tokopedia.app>"
}

# Create a new driver object
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Wait for the home screen to load
time.sleep(10)

# Find and click the search button
search_button = driver.find_element_by_accessibility_id("Search")
search_button.click()

# Enter the search term
search_input = driver.find_element_by_accessibility_id("SearchBarTextField")
search_input.send_keys("Samsung Galaxy S21")

# Submit the search query
driver.find_element_by_accessibility_id("Search").click()

# Wait for the search results to load
time.sleep(10)

# Click on the first search result
result = driver.find_element_by_xpath("//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]")
result.click()

# Wait for the product page to load
time.sleep(10)

# Add the product to the cart
add_to_cart_button = driver.find_element_by_accessibility_id("Add to Cart")
add_to_cart_button.click()

# Wait for the cart page to load
time.sleep(10)

# Verify the product is in the cart
cart_item = driver.find_element_by_xpath("//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]")
assert cart_item.text == "Samsung Galaxy S21"

# Close the app
driver.quit()
