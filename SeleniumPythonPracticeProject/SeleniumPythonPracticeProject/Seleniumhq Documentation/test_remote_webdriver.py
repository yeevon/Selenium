import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.support.wait import WebDriverWait


def test_start_remote(server):
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=server, options=options)

    assert "localhost" in driver.command_executor._url
    driver.quit()


def test_remote_file_uploads(server):
    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(command_executor=server, options=options)
    driver.get("https://the-internet.herokuapp.com/upload")
    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "selenium-snapshot.png")
    )

    driver.file_detector = LocalFileDetector()
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(upload_file)
    driver.find_element(By.ID, "file-submit").click()

    file_name = driver.find_element(By.ID, "uploaded-files").text
    assert file_name == "selenium-snapshot.png"


def test_enable_downloads(server, temp_dir):
    options = webdriver.ChromeOptions()
    options.enable_downloads = True
    driver = webdriver.Remote(options=options, command_executor=server)

    file_names = ["file_1.txt", "file_2.txt"]
    driver.get("https://www.selenium.dev/selenium/web/downloads/download.html")
    driver.find_element(By.ID, "file-1").click()
    driver.find_element(By.ID, "file-2").click()
    WebDriverWait(driver, 3).until(lambda d: "file_2.jpg" in d.get_downloadable_files())

    files = driver.get_downloadable_files()

    assert sorted(files) == sorted(file_names)
    downloadable_file = file_names[0]
    target_directory = temp_dir

    driver.download_file(downloadable_file, target_directory)

    target_file = os.path.join(target_directory, downloadable_file)
    with open(target_file, "r") as file:
        assert "Hello, World!" in file.read()

    driver.delete_downloadable_files()

    assert not driver.get_downloadable_files()
