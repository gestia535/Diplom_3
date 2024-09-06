from selenium.webdriver.common.by import By


class TestUserAccountPageLocators:

    # Поле email в форме входа в ЛК
    EMAIL_FIELD_LOGIN_PAGE = By.XPATH, "(//input[@name='name' and @type='text'])[1]"

    # Поле пароль в форме входа в ЛК
    PASSWORD_FIELD_LOGIN_PAGE = By.XPATH, "//input[@type='password']"

    # Кнопка Войти на странице формы входа в ЛК
    LOGIN_BUTTON_LOGIN_PAGE = By.XPATH, "//button[text()='Войти']"

    # Раздел "История заказов"
    ORDERS_HISTORY_ACCOUNT_PAGE = (By.XPATH, '//a[@href = "/account/order-history"]')

    # Кнопка "Выход"
    LOGOUT_BUTTON_ACC_PAGE = (By.XPATH, '//button[text()="Выход"]')
