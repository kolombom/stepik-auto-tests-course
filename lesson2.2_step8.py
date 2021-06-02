from selenium import webdriver
import time
import os 

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    input1 = browser.find_element_by_css_selector("input[name='firstname']")
    input1.send_keys("Smolensk")
    input2 = browser.find_element_by_css_selector("input[name='lastname']")
    input2.send_keys("Smolensk")
    input3 = browser.find_element_by_css_selector("input[name='email']")
    input3.send_keys("Smolensk")
    
    file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)
    file.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()