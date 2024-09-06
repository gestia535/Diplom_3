import allure
from locators.feed_page_locators import TestFeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Получение главного заголовка ленты заказов')
    def get_text_on_title_of_feed(self):
        return self.get_text_on_element(TestFeedPageLocators.FEED_TITLE)

    @allure.step('Кликнуть по заказу в ленте')
    def click_on_order_card(self):
        self.wait_until_element_visibility(TestFeedPageLocators.ORDER_CARD)
        self.click_on_element(TestFeedPageLocators.ORDER_CARD)

    @allure.step('Получить текст заголовка окна с деталями заказа')
    def get_title_of_order_popup(self):
        return self.get_text_on_element(TestFeedPageLocators.ORDER_POPIP_TITLE)

    @allure.step("Проверка совпадения заказов в истории и в ленте")
    def check_order_id(self, order_id, locator):
        elements = self.find_until_all_elements_located(locator)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Получение количества заказов")
    def get_total_orders_daily(self, locator):
        return self.get_text_on_element(locator)

    @allure.step("Проверка нахождение идентификатора заказа в ленте")
    def is_order_id_found_at_feed(self, order_number):
        return self.check_order_id(order_number, TestFeedPageLocators.ALL_ORDERS_FEED)

    @allure.step('Получение номера заказа')
    def get_user_order(self, orders_numbers):
        order_rename = f'0{orders_numbers}'
        self.wait_for_text_to_be_present_in_element(TestFeedPageLocators.NUMBER_IN_PROGRESS, order_rename)
        return order_rename

    @allure.step('Получение номера заказа со статусом В работе')
    def get_user_order_in_progress(self):
        return self.get_text_on_element(TestFeedPageLocators.NUMBER_IN_PROGRESS)
