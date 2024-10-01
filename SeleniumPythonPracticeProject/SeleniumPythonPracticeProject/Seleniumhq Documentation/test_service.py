from selenium import webdriver


def test_service():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)

    driver.quit()


def test_driver_location(chromedriver_bin, chrome_bin):
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_bin

    service = webdriver.ChromeService(executable_path=chromedriver_bin)

    driver = webdriver.Chrome(service=service, options=options)

    driver.quit()


def test_driver_port():
    service = webdriver.ChromeService(port=5555)

    driver = webdriver.Chrome(service=service)

    driver.quit()


def test_logging_chrome(log_path):
    service = webdriver.ChromeService(log_output=log_path)

    driver = webdriver.Chrome(service=service)

    driver.quit()