import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_title(driver):

    title = driver.title
    assert title == 'Web form', f"Expected title to be 'Web form', but got {title}"

    print(title)

    # driver.implicitly_wait(0.5)
    #
    # text_box = driver.find_element(by=By.NAME, value='my-text')
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value='button')
    #
    # text_box.send_keys('Selenium')
    # submit_button.click()
    #
    # message = driver.find_element(by=By.ID, value='message')
    # value = message.text
    # assert value == 'Received!'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.selenium.dev/selenium/web/web-form.html')
    yield driver
    driver.quit()
