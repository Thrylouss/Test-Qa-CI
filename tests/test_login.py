import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_success(driver):
    driver.get("https://my.proweb.uz/log-in")

    login = LoginPage(driver)
    login.enter_phone_number("998335814130")
    login.click_login()
    login.enter_password("proweb3106632")
    login.click_login()
    login.find_dropdown()
    login.click_btn_finish()

    home_page = HomePage(driver)
    home_page.click_profile()


# def test_login_invalid(driver):
#     driver.get("https://my.proweb.uz/log-in")
#
#     login = LoginPage(driver)
#     login.enter_phone_number("998335814131")
#     login.click_login()
#     login.enter_password("proweb3106632")
#     login.click_login()