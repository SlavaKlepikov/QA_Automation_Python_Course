import configparser
import os

from CONSTS import ROOT_DIR

abs_path = os.path.abspath(fr"{ROOT_DIR}/configurations/configuration.ini")
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_application_login_url():
        return config.get('app_info', 'login_url')

    @staticmethod
    def get_driver_id():
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_headless_mod():
        return config.get('browser', 'is_headless')

    @staticmethod
    def get_user_login():
        return config.get('app_info', 'user_login')

    @staticmethod
    def get_user_password():
        return config.get('app_info', 'user_password')

