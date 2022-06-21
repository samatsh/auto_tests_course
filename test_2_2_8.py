import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    element1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    element1.send_keys("Samat")
    element2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    element2.send_keys("Sh")
    element3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    element3.send_keys("Sh@qwe.ru")

    element4 = browser.find_element(By.CSS_SELECTOR, "[name='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'txtfile.txt')
    element4.send_keys(file_path)

    chk_btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    chk_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
