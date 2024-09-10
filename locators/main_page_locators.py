from selenium.webdriver.common.by import By


class TestMainPageLocators:
    # Кнопка Войти в аккаунт на Главной
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка Личный кабинет на главной
    ACCOUNT_BUTTON_MAIN_PAIGE = By.XPATH, ".//p[text()='Личный Кабинет']"

    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"

    # Заголовок Соберите бургер в разделе Конструктор
    MAKE_BURGER_TITLE = By.XPATH, "//h1[text()='Соберите бургер']"

    # Кнопка Лента заказов
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"

    # Заголовок страницы Лента заказов
    FEED_TITLE = By.XPATH, "//h1[text()='Лента заказов']"

    # Ингредиент
    INGREDIENT_BUTTON = By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"

    # Заголовок Детали ингредиента в поп-апе
    INGREDIENT_POPUP_TITLE = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')

    # Кнопка закрытия поп-апа "Детали ингредиента"
    CLOSE_BUTTON_POPUP = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]')

    # Выбранный ингредиент для добавления
    SOURCE_INGREDIENT = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Корзина для добавления ингредиентов
    BASKET_FOR_CHOSEN_INGREDIENTS = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните "
                                               "булочку сюда (низ)']")

    # Счетчик количества добавленных ингредиентов
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')

    # Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'

    # Надпись "Идентификатор заказа"
    ORDER_IDENTIFICATOR = (By.XPATH, '//p[text()="идентификатор заказа"]')

    # Номер заказа
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")

    # Кнопка закрытия модального окна заказа
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
