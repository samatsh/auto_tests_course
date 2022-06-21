import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    elem1 = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button1 = browser.find_element(By.CSS_SELECTOR, "[id='book']")
    button1.click()
    #message = browser.find_element(By.ID, "verify_message")

    #assert "successful" in message.text

    element1 = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = int(element1.text)
    y = math.log(abs(12 * math.sin(x)))
    element2 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    element2.send_keys(str(y))

    chk_btn = browser.find_element(By.CSS_SELECTOR, "[id='solve']")
    chk_btn.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()