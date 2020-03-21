import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_positive_registration(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    wait = WebDriverWait(browser, 20)
    email = str(time.time()) + "@fakemail.org"
    password = "2020varakin2020"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#register_form .btn.btn-lg.btn-primary")))
    browser.find_element(By.CSS_SELECTOR, "#id_registration-email").send_keys(email)
    browser.find_element(By.CSS_SELECTOR, "#id_registration-password1").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "#id_registration-password2").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "11#register_form .btn-primary").click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#messages > div.alert.alert-success.fade.in > div"),
                                                "Thanks for registering!"), "NO message registration ")

