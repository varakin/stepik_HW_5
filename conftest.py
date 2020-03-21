import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="Chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Choose language')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if browser_name == "Chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be Chrome or Firefox")
    yield browser
    print("\nquit browser..")
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    browser.save_screenshot('my_allure_reports/screenshot-%s.png' % now)
    browser.quit()
