from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestCSS(unittest.TestCase):
    def test_registration1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            first_name.send_keys('Ivan')

            last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            last_name.send_keys('Ivanov')

            email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            email.send_keys('Ivanov@gmail.com')

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text


            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(2)
            browser.quit()

    def test_registration2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            first_name.send_keys('Ivan')

            last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            last_name.send_keys('Ivanov')

            email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            email.send_keys('Ivanov@gmail.com')

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(2)
            browser.quit()

if __name__ == "__main__":
    unittest.main()