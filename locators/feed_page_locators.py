from selenium.webdriver.common.by import By


class TestFeedPageLocators:
    # Заголовок страницы Лента заказов
    FEED_TITLE = By.XPATH, "//h1[text()='Лента заказов']"

    # Карточка заказа в ленте
    ORDER_CARD = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    # Заголовок всплывающего окна с деталями заказа
    ORDER_POPIP_TITLE = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')

    # Все заказы в разделе Лента заказов
    ALL_ORDERS_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                    "text_type_digits-default']")

    # Номер заказа В работе
    NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem "
                                    "OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")


    # Номер заказа в ленте
    ORDER_ID_FEED = (By.XPATH, './/*[text()="{order_id}"]')

    ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]'  # Состав
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в Ленте заказов



    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_IN_PROGRESS_2 = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')  # Номер в разделе "В работе"

    # Раздел заказов
    section_orders_list = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Заголовок ленты заказов
    title_of_orders_feed = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')



    # Всплывающее окно с деталями заказа
    modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')



    # Счетчик заказов "Выполнено за все время"
    quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    # Счетчик заказов "Выполнено за сегодня"
    daily_quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Заказ в разделе "В работе"
    order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    # Номер заказа в разделе "В работе"
    number_of_order_in_progress = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')


