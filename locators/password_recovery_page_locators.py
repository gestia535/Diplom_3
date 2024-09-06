from selenium.webdriver.common.by import By


class TestPasswordRecoveryLocators:
    # Кнопка "Восстановить пароль" на экране входа
    RESTORE_PASSWORD_BUTTON_LOGIN_PAGE = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Поле ввода email
    EMAIL_FIELD = (By.CLASS_NAME, 'input__textfield')

    # Кнопка "Восстановить" на странице восстановления пароля
    RESTORE_PASSWORD_BUTTON_RECOVERY_PAGE = (By.CLASS_NAME, 'button_button__33qZ0')

    # Кнопка показать/скрыть пароль
    HIDE_PASSWORD_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    # Режим видимости пароля: видимый
    VISIBLE_PASSWORD_MODE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                       '"input_status_active")]')
