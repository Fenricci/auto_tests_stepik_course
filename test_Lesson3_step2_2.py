import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestMyTests():
    def test_required1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        input1.send_keys("Vugar")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        input2.send_keys("Guseynov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
        input3.send_keys("fettsain@gmail.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text, "Ошибка!!"

        browser.quit()

    def test_required2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        input1.send_keys("Vugar")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        input2.send_keys("Guseynov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
        input3.send_keys("fettsain@gmail.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text, "Ошибка!!"

        browser.quit()

if __name__ == '__main__':
    unittest.main()