import allure

from data import RESTORE_PASS_URL, RESET_PASS_URL
from helpers import email_generator
from locators.password_recovery_page_locators import TestPasswordRecoveryLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    @allure.step('Скролл до кнопки "Восстановить пароль" на странице логина')
    def scroll_to_restore_button(self):
        self.scroll_to_element(TestPasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON_LOGIN_PAGE)
        self.find_element_with_wait(TestPasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON_LOGIN_PAGE)

    @allure.step('Нажатие кнопки "Восстановить пароль" на странице входа в ЛК')
    def click_restore_password_button(self):
        self.find_element_with_wait(TestPasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON_LOGIN_PAGE)
        self.click_on_element(TestPasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON_LOGIN_PAGE)
        self.wait_url_to_be(RESTORE_PASS_URL)

    @allure.step('Заполнить поле email')
    def set_email_field(self):
        self.find_element_with_wait(TestPasswordRecoveryLocators.EMAIL_FIELD)
        self.click_on_element(TestPasswordRecoveryLocators.EMAIL_FIELD)
        self.set_text_to_elm(TestPasswordRecoveryLocators.EMAIL_FIELD, email_generator())
        return self

    @allure.step('Нажатие кнопки "Восстановить" на странице восстановления пароля')
    def click_reset_password_button(self):
        self.find_element_with_wait(TestPasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON_RECOVERY_PAGE)
        self.click_on_element(TestPasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON_RECOVERY_PAGE)
        self.wait_url_to_be(RESET_PASS_URL)

    @allure.step('Нажатие кнопки показать/скрыть пароль')
    def click_hide_password_button(self):
        self.find_element_with_wait(TestPasswordRecoveryLocators.HIDE_PASSWORD_BUTTON)
        self.click_on_element(TestPasswordRecoveryLocators.HIDE_PASSWORD_BUTTON)

    @allure.step('Отображение поля Пароль в активном режиме')
    def check_visibility_passw_field_active(self):
        return self.wait_until_element_visibility(TestPasswordRecoveryLocators.VISIBLE_PASSWORD_MODE)
