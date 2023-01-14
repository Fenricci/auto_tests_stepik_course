import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(5)

url = "https://suninjuly.github.io/text_input_task.html"
driver.get(url)
time.sleep(5)

text_area = driver.find_element(By.CSS_SELECTOR, ".textarea")
text_area.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
submit_button.click()
time.sleep(5)

driver.quit()




link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    browser.quit()
# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае