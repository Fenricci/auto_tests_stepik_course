from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

def summ(x, y):
    result = x + y
    return result

try:
    browser = webdriver.Chrome()
    browser.get(link)

    number_1 = browser.find_element(By.ID, "num1")
    number_one = int(number_1.text)
    number_2 = browser.find_element(By.ID, "num2")
    number_two = int(number_2.text)
    results_number = summ(number_one, number_two)
    results = str(results_number)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(results)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
