from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

"""
Normal
Waits for the entire page and all its components to load, including CSS, images, and frames

Eager
Waits for the HTML document to load and parse, but discards loading of stylesheets, images, and sub frames

None
Only waits for the initial page to download

"""


def test_page_load_strategy_normal():
    options = webdriver.ChromeOptions()

    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)    

    driver.get("https://www.selenium.dev/")
    driver.quit()


def test_page_load_strategy_eager():
    options = webdriver.ChromeOptions()

    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.selenium.dev/")
    driver.quit()


def test_page_load_strategy_none():
    options = webdriver.ChromeOptions()

    options.page_load_strategy = 'none'
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.selenium.dev/")
    driver.quit()

# Customize browser capabilities


def test_capabilities():
    options = webdriver.ChromeOptions()
    options.browser_version = 'sable'
    options.platform_name = 'any'
    options.accept_insecure_certs = True
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.selenium.dev/")
    driver.quit()

# Customize page load timeouts


def test_timeouts_page_load():
    options = webdriver.ChromeOptions()
    options.timeouts = {"pageLoad": 5000}
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.selenium.dev/")
    driver.quit()


def test_timeouts_implicit_wait():
    options = webdriver.ChromeOptions()
    options.timeouts = {'implicit': 5000}
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.selenium.dev/")
    driver.quit()

# Have browser handle prompts


def test_unhandled_prompt():
    options = webdriver.ChromeOptions()
    options.unhandled_prompt_behavior = 'accept'
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.selenium.dev/")
    driver.quit()


"""
strict_file_interactability determines whether the WebDriver should 
enforce strict checks to ensure that files can be uploaded
"""


def test_strict_file_interactability():
    options = webdriver.ChromeOptions()
    options.strict_file_interactability = True
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.selenium.dev/")
    driver.quit()


def test_proxy():
    options = webdriver.ChromeOptions()
    options.proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': 'http.proxy:1234'})
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.selenium.dev/")
    driver.quit()
