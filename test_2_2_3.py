import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    element1 = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    num1 = int(element1.text)
    element2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    num2 = int(element2.text)
    summa = num1 + num2
    select1 = Select(browser.find_element(By.TAG_NAME, "select"))
    select1.select_by_visible_text(str(summa))
    chk_btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    chk_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()