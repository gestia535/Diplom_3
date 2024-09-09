import allure


class TestRecoveryPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_click_restore_password_button_open_recovery_password_page(self, driver, main_page, pass_recovery_page):
        main_page.click_login_button()
        pass_recovery_page.scroll_to_restore_button()
        pass_recovery_page.click_restore_password_button()
        assert pass_recovery_page.is_on_restore_password_page()

    @allure.title('Проверка открытия страницы смены пароля после ввода email и нажатия кнопки "Восстановить"')
    def test_open_restore_password_page_after_setting_email(self, driver, main_page, pass_recovery_page):
        main_page.click_login_button()
        pass_recovery_page.scroll_to_restore_button()
        pass_recovery_page.click_restore_password_button()
        pass_recovery_page.set_email_field()
        pass_recovery_page.click_reset_password_button()
        assert pass_recovery_page.is_on_reset_password_page()

    @allure.title('Проверка активации поля Пароль по клику по кнопке показать/скрыть пароль')
    def test_click_hide_passw_button_activate_field(self, driver, main_page, pass_recovery_page):
        main_page.click_login_button()
        pass_recovery_page.scroll_to_restore_button()
        pass_recovery_page.click_restore_password_button()
        pass_recovery_page.set_email_field()
        pass_recovery_page.click_reset_password_button()
        pass_recovery_page.click_hide_password_button()
        assert pass_recovery_page.check_visibility_passw_field_active
