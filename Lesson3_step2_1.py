from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
input1.send_keys("Vugar")
input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
input2.send_keys("Guseynov")
input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
input3.send_keys("fettsain@gmail.com")

button  = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


browser.quit()