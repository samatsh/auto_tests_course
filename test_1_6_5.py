from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link1 = "http://suninjuly.github.io/simple_form_find_task.html"
link2 = "http://suninjuly.github.io/find_link_text"
value1 = "input[name='first_name']"
value2 = "input[name='last_name']"
value3 = "input.city"

try:
    time.sleep(5)
    browser = webdriver.Chrome()
    browser.get(link2)
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element(By.CSS_SELECTOR, value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(13)
    # закрываем браузер после всех манипуляций
    browser.quit()