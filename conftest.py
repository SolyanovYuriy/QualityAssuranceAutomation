import pytest
from selenium import webdriver
import os


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': f'{os.getcwd()}', "download.prompt_for_download": False,
             "download.directory_upgrade": True, "safebrowsing.enabled": True}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=https://sbis.ru/")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    return chrome_browser


@pytest.fixture(scope='session')
def for_all_test():
    yield
    browser.quit()
