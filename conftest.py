import pytest
from utils.driver_factory import DriverFactory
from utils.read_run_settings import ReadConfig


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=int(ReadConfig.get_driver_id()),
                                         is_headless=ReadConfig.get_headless_mod())
    driver.get(ReadConfig.get_application_login_url())
    driver.maximize_window()
    yield driver
    driver.quit()

