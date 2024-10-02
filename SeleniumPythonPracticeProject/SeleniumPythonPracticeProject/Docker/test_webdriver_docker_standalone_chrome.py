import time

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

# Define pytest fixture for setup and teardown
@pytest.fixture(scope="function")
def driver():
    global driver
    rul = 'http://localhost:4445'
    try:
        driver = webdriver.Remote(
            command_executor=rul,
            options=webdriver.ChromeOptions()
        )
        time.sleep(2)

        # Navigate to the test website
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    except:
        print("Could not start browser")

    # Yield the driver object to the test function
    yield driver

    # Teardown: Quit the browser after test completion
    driver.quit()

def test_first(driver):
    time.sleep(10)
    # Get test website title
    title = driver.title

    # Get text box and submit button
    text_box = driver.find_element(By.NAME, "my-text")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button")

    # Input text into the text box and submit
    text_box.send_keys("Selenium")
    submit_button.click()

    # Get the resulting message
    message = driver.find_element(By.ID, "message").text
    
    # Assert the message and the title
    assert message == "Received!"
    assert title == "Web form"
