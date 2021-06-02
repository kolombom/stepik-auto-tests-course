from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    
    button = browser.find_element_by_class_name("btn").click()
    new_window = browser.window_handles[1]  
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id("input_value")
    y = calc(int(x_element.text))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    # Отправляем заполненную форму
    button2 = browser.find_element_by_class_name("btn").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()