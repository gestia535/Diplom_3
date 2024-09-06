from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    # Карточка заказа в истории заказов
    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    # Заголовок карточки заказа с названием бургера
    ORDER_CARD_TITLE = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    # Номер заказа в карточке заказа
    ORDER_ID = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, '
                          '"text_type_digits-default")])[1]')

    ALL_ORDERS_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]")
