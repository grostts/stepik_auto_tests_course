from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('Ivanov')

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('Ivanov@mail.ru')

    file = browser.find_element(By.NAME, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла