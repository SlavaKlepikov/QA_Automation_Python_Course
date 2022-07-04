from page_objects.home_page.home_page_locators import HomePageLocators
from page_objects.login_page import LoginPage
from utils.web_ui.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__home_page_elements = HomePageLocators()

    def get_current_phone_number(self):
        phone_number_element = self.wait_until_element_located(self.__home_page_elements.phone_number_label)
        return self.get_text(phone_number_element)

    def click_sign_in(self):
        self.click(self.__home_page_elements.sign_in_btn)
        return LoginPage(self._driver)

    def click_create_game(self):
        self.click(self.__home_page_elements.create_game_btn)
        return self

    def click_play_with_friend(self):
        self.click(self.__home_page_elements.play_with_friend_btn)
        return self

    def click_play_with_computer(self):
        self.click(self.__home_page_elements.play_with_computer_btn)
        return self

    def get_header_game_setup_menu(self):
        header_game_setup_menu = self.wait_until_element_located(self.__home_page_elements.header_game_setup_menu)
        return self.get_text(header_game_setup_menu)

    def get_variants_game_setup(self):
        variants_game_setup = \
            self.wait_until_presence_of_all_elements_located(self.__home_page_elements.variants_game_setup)
        return variants_game_setup

    def get_time_choice_range_game_setup(self):
        time_choice_range_game_setup = \
            self.wait_until_element_located(self.__home_page_elements.time_choice_range_game_setup)
        return self.get_text(time_choice_range_game_setup)

    def get_time_increment_choice_range_game_setup(self):
        time_increment_choice_range_game_setup = \
            self.wait_until_element_located(self.__home_page_elements.time_increment_choice_range_game_setup)
        return self.get_text(time_increment_choice_range_game_setup)

    def click_donate(self):
        self.click(self.__home_page_elements.donate_btn)
        return self

    def click_swag_store_btn(self):
        self.click(self.__home_page_elements.swag_store_btn)
        return self

