from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.utils import ChromeType


class DriverFactory:
    CHROME = 1
    FIRE_FOX = 2
    CHROMIUM = 3

    @staticmethod
    def create_driver(driver_id, is_headless):
        if DriverFactory.CHROME == driver_id:
            chrome_options = webdriver.ChromeOptions()
            if is_headless:
                chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        elif DriverFactory.FIRE_FOX == driver_id:
            firefox_options = webdriver.FirefoxOptions()
            if is_headless:
                firefox_options.headless = is_headless
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        elif DriverFactory.CHROMIUM == driver_id:
            chromium_options = webdriver.ChromeOptions()
            if is_headless:
                chromium_options.headless = is_headless
            driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(),
                                      options=chromium_options)
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver

