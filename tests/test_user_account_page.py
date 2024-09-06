import allure
from data import PROFILE_URL, ORDER_HISTORY_URL, LOGIN_URL


class TestUserAccountPage:

    @allure.title('Проверка перехода на страницу личного кабинета по кнопке "Личный кабинет"')
    def test_click_account_button_open_user_account_page(self, driver, main_page, user_acc_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.click_account_button()
        assert driver.current_url == PROFILE_URL

    @allure.title('Проверка перехода в раздел "История заказов" в ЛК')
    def test_open_history_page(self, driver, main_page, user_acc_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.click_account_button()
        user_acc_page.click_order_history_button()
        assert driver.current_url == ORDER_HISTORY_URL

    @allure.title('Проверка выхода из ЛК')
    def test_logout(self, driver, main_page, user_acc_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.click_account_button()
        user_acc_page.click_logout_button()
        assert driver.current_url == LOGIN_URL
