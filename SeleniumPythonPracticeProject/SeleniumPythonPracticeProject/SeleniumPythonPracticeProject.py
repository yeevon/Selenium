
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

#Create Chrome options and set debugging port to 5555
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=5555")

#instatiate chromedriver 
driver = webdriver.Chrome(options=chrome_options)

#navigate to test website
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#get test website title
title = driver.title

#Get text box and submit button
text_box = driver.find_element(By.NAME, "my-text")
submit_button = driver.find_element(By.CSS_SELECTOR, "button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(By.ID, "message").text
assert message == "Received!"

print(title)