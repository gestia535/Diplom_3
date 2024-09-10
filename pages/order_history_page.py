import allure

from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):

    @allure.step("Проверка совпадения заказов в истории и в ленте")
    def check_order_id(self, order_id, locator):
        elements = self.find_until_all_elements_located(locator)
        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Проверка нахождение идентификатора заказа в истории")
    def is_order_id_found_at_history(self, order_number):
        return self.check_order_id(order_number, OrderHistoryPageLocators.ALL_ORDERS_HISTORY)

    @allure.step("Проверка совпадения заказов в истории и в ленте")
    def check_order_id(self, order_id, locator):
        elements = self.find_until_all_elements_located(locator)
        for element in elements:
            if order_id == element.text:
                return True
        return True
