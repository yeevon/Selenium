import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Define pytest fixture for setup and teardown
@pytest.fixture(scope="function", params=["chrome", "firefox", "edge"])
def driver(request):
    rul = 'http://localhost:4444'

    if request.param == "chrome":
        driver = webdriver.Remote(command_executor=rul, options=webdriver.ChromeOptions())
    elif request.param == "firefox":
        driver = webdriver.Remote(command_executor=rul, options=webdriver.FirefoxOptions())
    else:
        driver = webdriver.Remote(command_executor=rul, options=webdriver.EdgeOptions())

    # Yield the driver object to the test function
    yield driver

    # Teardown: Quit the browser after test completion
    driver.quit()


def test_first(driver):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
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
