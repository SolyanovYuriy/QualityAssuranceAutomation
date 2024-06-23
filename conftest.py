import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    return chrome_browser


@pytest.fixture(scope='session')
def for_all_test():
    yield
    browser.quit()
