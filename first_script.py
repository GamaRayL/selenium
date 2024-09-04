import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_title(driver):
    title = driver.title
    assert title == 'Web form', f"Expected title to be 'Web form', but got {title}"

    print(title)


def test_form_submission(driver):
    text_box = driver.find_element(by=By.NAME, value='my-text')
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value='button')

    text_box.send_keys('Selenium')
    submit_button.click()

    message = driver.find_element(by=By.ID, value='message')
    value = message.text
    assert value == 'Received!', f'Ожидаемый ответ "Received!", но получен {value}'


def test_empty_submission(driver):
    submit_button = driver.find_element(by=By.CLASS_NAME, value='btn')
    submit_button.click()

    message = driver.find_element(by=By.ID, value='message')
    value = message.text

    assert value == 'Received!', f'Ожидаемый ответ "Please enter a value", но получен {value}'


#   Please enter a value

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.selenium.dev/selenium/web/web-form.html')
    yield driver
    driver.quit()
