"""
Find a web page with a login form. Log in to a website and verify log in using assert.
You should verify this using 3 different browsers.
Use pytest fixture for creating browser instances. The browser should quiet if some error occurs.
push your HW to the git repository and add a link to it.
"""
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from utils.read_run_settings import ReadConfig

def test_sign_in_chrome():
    try:
        driver = DriverFactory.create_driver(driver_id=1, is_headless=False)
        driver.get(ReadConfig.get_application_login_url())
        driver.maximize_window()
        login_input_id = "form3-username"
        login_input_element = driver.find_element(By.ID, login_input_id)
        login_input_element.send_keys(ReadConfig.get_user_login())
        password_input_id = "form3-password"
        password_input_element = driver.find_element(By.ID, password_input_id)
        password_input_element.send_keys(ReadConfig.get_user_password())
        sign_in_btn_locator = "//div[@class ='one-factor']/button[@class ='submit button']"
        sign_in_btn_element = driver.find_element(By.XPATH, sign_in_btn_locator)
        sign_in_btn_element.click()
        title_web_page_login = driver.title
        title_web_page_login_expected = "lichess.org • Бесплатные шахматы онлайн"
        assert title_web_page_login == title_web_page_login_expected, \
            f"\nWrong title\nActual:{title_web_page_login}\nExpected:{title_web_page_login_expected}"
    except:
        driver.quit()


def test_sign_in_firefox():
    try:
        driver = DriverFactory.create_driver(driver_id=2, is_headless=False)
        driver.get(ReadConfig.get_application_login_url())
        driver.maximize_window()
        login_input_id = "form3-username"
        login_input_element = driver.find_element(By.ID, login_input_id)
        login_input_element.send_keys(ReadConfig.get_user_login())
        password_input_id = "form3-password"
        password_input_element = driver.find_element(By.ID, password_input_id)
        password_input_element.send_keys(ReadConfig.get_user_password())
        sign_in_btn_locator = "//div[@class ='one-factor']/button[@class ='submit button']"
        sign_in_btn_element = driver.find_element(By.XPATH, sign_in_btn_locator)
        sign_in_btn_element.click()
        title_web_page_login = driver.title
        title_web_page_login_expected = "lichess.org • Бесплатные шахматы онлайн"
        assert title_web_page_login == title_web_page_login_expected, \
            f"\nWrong title\nActual:{title_web_page_login}\nExpected:{title_web_page_login_expected}"
    except:
        driver.quit()


def test_sign_in_chromium():
    try:
        driver = DriverFactory.create_driver(driver_id=3, is_headless=False)
        driver.get(ReadConfig.get_application_login_url())
        driver.maximize_window()
        login_input_id = "form3-username"
        login_input_element = driver.find_element(By.ID, login_input_id)
        login_input_element.send_keys(ReadConfig.get_user_login())
        password_input_id = "form3-password"
        password_input_element = driver.find_element(By.ID, password_input_id)
        password_input_element.send_keys(ReadConfig.get_user_password())
        sign_in_btn_locator = "//div[@class ='one-factor']/button[@class ='submit button']"
        sign_in_btn_element = driver.find_element(By.XPATH, sign_in_btn_locator)
        sign_in_btn_element.click()
        title_web_page_login = driver.title
        title_web_page_login_expected = "lichess.org • Бесплатные шахматы онлайн1"
        assert title_web_page_login == title_web_page_login_expected, \
            f"\nWrong title\nActual:{title_web_page_login}\nExpected:{title_web_page_login_expected}"
    except:
        driver.quit()


def test_sign_in(create_driver):
    try:
        login_input_id = "form3-username"
        login_input_element = create_driver.find_element(By.ID, login_input_id)
        login_input_element.send_keys(ReadConfig.get_user_login())
        password_input_id = "form3-password"
        password_input_element = create_driver.find_element(By.ID, password_input_id)
        password_input_element.send_keys(ReadConfig.get_user_password())
        sign_in_btn_locator = "//div[@class ='one-factor']/button[@class ='submit button']"
        sign_in_btn_element = create_driver.find_element(By.XPATH, sign_in_btn_locator)
        sign_in_btn_element.click()
        title_web_page_login = create_driver.title
        title_web_page_login_expected = "lichess.org • Бесплатные шахматы онлайн"
        assert title_web_page_login == title_web_page_login_expected, \
            f"\nWrong title\nActual:{title_web_page_login}\nExpected:{title_web_page_login_expected}"
    except:
        create_driver.quit()
