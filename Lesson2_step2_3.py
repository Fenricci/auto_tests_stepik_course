from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    f_name = browser.find_element(By.NAME, "firstname").send_keys("Vugar")
    l_name = browser.find_element(By.NAME, "lastname").send_keys("Guseynov")
    mail = browser.find_element(By.NAME, "email").send_keys("senior1345@mail.com")

    choice = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')
    choice.send_keys(file_path)
    # Добавление прикрепленного файла (Пути к нему)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()