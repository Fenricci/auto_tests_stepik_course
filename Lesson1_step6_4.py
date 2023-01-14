from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        element.send_keys('value')
    # в цикле for мы можем последовательно взять каждый элемент из найденного списка текстовых полей и отправить произвольный текст в каждое поле

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()


