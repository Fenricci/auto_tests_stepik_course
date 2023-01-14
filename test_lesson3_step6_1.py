import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True)
def test_get_autorization(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_element(By.LINK_TEXT, "Войти")
    button.click()

    email_check = browser.find_element(By.CSS_SELECTOR, "input#id_login_email")
    email_check.send_keys("senior34@gmail.com")
    password_check = browser.find_element(By.CSS_SELECTOR, "input#id_login_password")
    password_check.send_keys("password123")
    button_log = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    button_log.click()
    time.sleep(1)

@pytest.mark.parametrize("url", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_get_answer(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1/"
    browser.get(link)
    time.sleep(3)

    get_answer = browser.find_element(By.TAG_NAME, "textarea")
    answer = math.log(int(time.time()))
    get_answer.clear()
    get_answer.send_keys(answer)
    time.sleep(6)
    button_answer = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button_answer.click()
    button_again = browser.find_element(By.CSS_SELECTOR, "button.again-btn.white")
    button_again.click()

    time.sleep(3)
    feedback_text = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    check_text = feedback_text.text
    print(check_text)
    assert "Correct!" == check_text, "Текст не совпадает!"



