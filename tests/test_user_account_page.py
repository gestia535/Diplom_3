import allure


class TestUserAccountPage:

    @allure.title('Проверка перехода на страницу личного кабинета по кнопке "Личный кабинет"')
    def test_click_account_button_open_user_account_page(self, driver, main_page, user_acc_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.click_account_button()
        assert user_acc_page.is_on_profile_page()

    @allure.title('Проверка перехода в раздел "История заказов" в ЛК')
    def test_open_history_page(self, driver, main_page, user_acc_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.click_account_button()
        user_acc_page.click_order_history_button()
        assert user_acc_page.is_on_order_history_page()

    @allure.title('Проверка выхода из ЛК')
    def test_logout(self, driver, main_page, user_acc_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.click_account_button()
        user_acc_page.click_logout_button()
        assert user_acc_page.is_on_login_page()
