from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9.0",
    "deviceName": "Android Emulator",
    "appPackage": "com.tokopedia.tkpd",
    "appActivity": "com.tokopedia.tkpd.view.splash.SplashScreenActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# wait for the home screen to load
time.sleep(10)

# click on the search button
search_button = driver.find_element_by_id("com.tokopedia.tkpd:id/search_widget_text")
search_button.click()

# enter the search term
search_input = driver.find_element_by_id("com.tokopedia.tkpd:id/input_query")
search_input.send_keys("Samsung Galaxy S21")

# submit the search query
search_input.submit()

# wait for the search results to load
time.sleep(10)

# click on the first search result
result = driver.find_element_by_id("com.tokopedia.tkpd:id/product_item_container")
result.click()

# wait for the product page to load
time.sleep(10)

# add the product to the cart
add_to_cart_button = driver.find_element_by_id("com.tokopedia.tkpd:id/btn_add_to_cart")
add_to_cart_button.click()

# wait for the cart page to load
time.sleep(10)

# check if the product is in the cart
cart_item_name = driver.find_element_by_id("com.tokopedia.tkpd:id/txt_item_name")
assert cart_item_name.text == "Samsung Galaxy S21"

# close the app
driver.close()
