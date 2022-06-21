import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    element1 = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = int(element1.text)
    y = math.log(abs(12 * math.sin(x)))
    element2 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element2)
    element2.send_keys(str(y))

    chk_elmnt = browser.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']")
    chk_elmnt.click()
    chk_radbtn = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']")
    chk_radbtn.click()

    chk_btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    chk_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
