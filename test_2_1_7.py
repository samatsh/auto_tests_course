import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    element1 = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")

    x = element1.get_attribute("valuex")
    y = calc(x)

    inp_element = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
    inp_element.send_keys(y)
    chk_elmnt = browser.find_element(By.CSS_SELECTOR, "[id = 'robotCheckbox']")
    chk_elmnt.click()
    chk_radbtn = browser.find_element(By.CSS_SELECTOR, "[id = 'robotsRule']")
    chk_radbtn.click()

    chk_btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    chk_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()