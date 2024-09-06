import allure

from data import TEST_EMAIL, TEST_PASSWORD, BASE_URL, LOGIN_URL
from locators.user_account_page_locators import TestUserAccountPageLocators
from pages.base_page import BasePage


class UserAccountPage(BasePage):
    @allure.step('Залогиниться')
    def login(self):
        self.set_text_to_elm(TestUserAccountPageLocators.EMAIL_FIELD_LOGIN_PAGE, TEST_EMAIL)
        self.set_text_to_elm(TestUserAccountPageLocators.PASSWORD_FIELD_LOGIN_PAGE, TEST_PASSWORD)
        self.find_element_with_wait(TestUserAccountPageLocators.LOGIN_BUTTON_LOGIN_PAGE)
        self.click_on_element(TestUserAccountPageLocators.LOGIN_BUTTON_LOGIN_PAGE)
        self.wait_url_to_be(BASE_URL)

    @allure.step('Нажатие кнопки "История заказов" на странице ЛК')
    def click_order_history_button(self):
        self.find_element_with_wait(TestUserAccountPageLocators.ORDERS_HISTORY_ACCOUNT_PAGE)
        self.click_on_element(TestUserAccountPageLocators.ORDERS_HISTORY_ACCOUNT_PAGE)

    @allure.step('Нажатие кнопки "Выход" на странице ЛК')
    def click_logout_button(self):
        self.find_element_with_wait(TestUserAccountPageLocators.LOGOUT_BUTTON_ACC_PAGE)
        self.click_on_element(TestUserAccountPageLocators.LOGOUT_BUTTON_ACC_PAGE)
        self.wait_url_to_be(LOGIN_URL)
