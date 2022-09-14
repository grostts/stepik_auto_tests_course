from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

def calc(x,y):
  return int(x)+int(y)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1').text
    y_element = browser.find_element(By.ID, 'num2').text
    z = calc(x_element, y_element)
    print(z)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла