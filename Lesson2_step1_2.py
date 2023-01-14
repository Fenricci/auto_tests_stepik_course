from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("Value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("Value of robots radio: ", robots_checked)
    assert robots_checked is not None, "Robots radio is not selected by default"

    time.sleep(11)
    button_subm = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_checked = button_subm.get_attribute("disabled")
    print("Кнопка атрибута:", button_checked)
    assert button_checked is not None, "У кнопки нет дизейбла"

finally:
    time.sleep(10)
    browser.quit()
