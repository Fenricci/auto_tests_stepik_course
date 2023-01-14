from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import re

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

    prompt = browser.switch_to.alert
    prompt_text = prompt.text
    prompt.accept()

    nums = re.findall(r'\d*\.\d+|\d+', prompt_text)

    nums = [float(i) for i in nums]
    filter_text = nums

    urrl = "https://stepik.org/catalog"
    browser.get(urrl)
    time.sleep(1)

    author_stepik = browser.find_element(By.ID, "ember276")
    author_stepik.click()

    input_mail = browser.find_element(By.ID, "id_login_email").send_keys("senior123@gmail.com")
    input_password = browser.find_element(By.ID, "id_login_password").send_keys("password123")
    enter_stepik = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    stepik_lesson_url = "https://stepik.org/lesson/184253/step/4?unit=158843"
    time.sleep(10)
    browser.get(stepik_lesson_url)


    time.sleep(5)
    browser.execute_script("window.scrollBy(0, 130);")
    code_lesson = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area").send_keys(nums[0])


    submission = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    submission.click()

finally:
    time.sleep(10)
    browser.quit()