from selenium.webdriver.common.by import By

from utils.web_ui.locators import Locator


class HomePageLocators:

    def __init__(self):
        self.__sign_in_btn = Locator(By.XPATH, '//a[@class="signin button button-empty"]')
        self.__create_game_btn = Locator(By.XPATH, '//a[@class="button button-metal config_hook"]')
        self.__play_with_friend_btn = Locator(By.XPATH, '//a[@class="button button-metal config_friend"]')
        self.__play_with_computer_btn = Locator(By.XPATH, '//a[@class="button button-metal config_ai"]')
        self.__header_game_setup_menu = Locator(By.XPATH, "//div[@id='modal-wrap']/div/h2")
        self.__variants_game_setup = Locator(By.XPATH, "//select[@id = 'sf_variant' ]//option")
        self.__time_choice_range_game_setup = Locator(By.XPATH, "//div[@class = 'time-choice range' ]/span")
        self.__time_increment_choice_range_game_setup = \
            Locator(By.XPATH, "//div[@class = 'increment-choice range' ]/span")
        self.__donate_btn = Locator(By.XPATH, "//strong[text() = 'Donate']")
        self.__swag_store_btn = Locator(By.XPATH, "//strong[text() = 'Swag Store']")

    @property
    def sign_in_btn(self):
        return self.__sign_in_btn.get_locator()

    @property
    def create_game_btn(self):
        return self.__create_game_btn.get_locator()

    @property
    def header_game_setup_menu(self):
        return self.__header_game_setup_menu.get_locator()

    @property
    def game_setup_menu(self):
        return self.__game_setup_menu.get_locator()

    @property
    def play_with_friend_btn(self):
        return self.__play_with_friend_btn.get_locator()

    @property
    def play_with_computer_btn(self):
        return self.__play_with_computer_btn.get_locator()

    @property
    def variants_game_setup(self):
        return self.__variants_game_setup.get_locator()

    @property
    def time_choice_range_game_setup(self):
        return self.__time_choice_range_game_setup.get_locator()

    @property
    def time_increment_choice_range_game_setup(self):
        return self.__time_increment_choice_range_game_setup.get_locator()

    @property
    def donate_btn(self):
        return self.__donate_btn.get_locator()

    @property
    def swag_store_btn(self):
        return self.__swag_store_btn.get_locator()