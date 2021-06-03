from selenium import webdriver
import time
import pytest
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    text_area = browser.find_element_by_css_selector(".ember-text-area")
    text_area.send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()

    feed_back = browser.find_element_by_css_selector(".smart-hints__hint")
    assert feed_back.text == "Correct!", f"Expected 'Correct!', but was {feed_back.text}"
