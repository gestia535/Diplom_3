import allure
from data import PROFILE_URL
from locators.main_page_locators import TestMainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажатие кнопки "Войти в аккаунт"')
    def click_login_button(self):
        self.wait_until_element_visibility(TestMainPageLocators.LOGIN_BUTTON_MAIN_PAGE)
        self.wait_until_element_to_be_clickable(TestMainPageLocators.LOGIN_BUTTON_MAIN_PAGE)
        self.click_on_element(TestMainPageLocators.LOGIN_BUTTON_MAIN_PAGE)

    @allure.step('Нажатие кнопки "Личный кабинет"')
    def click_account_button(self):
        self.find_element_with_wait(TestMainPageLocators.ACCOUNT_BUTTON_MAIN_PAIGE)
        self.click_on_element(TestMainPageLocators.ACCOUNT_BUTTON_MAIN_PAIGE)
        self.wait_url_to_be(PROFILE_URL)

    @allure.step('Переход в "Конструктор"')
    def click_constructor_button(self):
        self.wait_until_element_visibility(TestMainPageLocators.CONSTRUCTOR_BUTTON)
        self.find_element_with_wait(TestMainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(TestMainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_until_element_visibility(TestMainPageLocators.MAKE_BURGER_TITLE)

    @allure.step('Получение главного заголовка конструктора')
    def get_text_on_title_of_constructor(self):
        return self.get_text_on_element(TestMainPageLocators.MAKE_BURGER_TITLE)

    @allure.step('Нажатие кнопки "Лента Заказов"')
    def click_order_feed_button(self):
        self.wait_until_element_visibility(TestMainPageLocators.ORDER_FEED_BUTTON)
        self.move_to_element_and_click(TestMainPageLocators.ORDER_FEED_BUTTON)
        self.wait_until_element_visibility(TestMainPageLocators.FEED_TITLE)

    @allure.step('Нажатие на ингредиент на главной странице')
    def click_ingredient(self):
        self.wait_until_element_visibility(TestMainPageLocators.INGREDIENT_BUTTON)
        self.wait_until_element_to_be_clickable(TestMainPageLocators.INGREDIENT_BUTTON)
        self.click_on_element(TestMainPageLocators.INGREDIENT_BUTTON)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_open_popup_with_details(self):
        self.wait_until_element_visibility(TestMainPageLocators.INGREDIENT_POPUP_TITLE)
        return self.check_displaying_of_element(TestMainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step('Нажатие на кнопку закрытия поп-апа')
    def click_on_close_button_popup(self):
        self.wait_until_element_visibility(TestMainPageLocators.CLOSE_BUTTON_POPUP)
        self.move_to_element_and_click(TestMainPageLocators.CLOSE_BUTTON_POPUP)

    @allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_modal_details(self):
        self.wait_for_closing_of_element(TestMainPageLocators.INGREDIENT_POPUP_TITLE)
        return self.check_invisibility(TestMainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step('Добавить ингредиент')
    def drag_and_drop_ingredient(self):
        source_locator = TestMainPageLocators.SOURCE_INGREDIENT
        target_locator = TestMainPageLocators.BASKET_FOR_CHOSEN_INGREDIENTS
        self.drag_and_drop_element(source_locator, target_locator)

    @allure.step('Получить количество добавленных ингредиентов')
    def count_ingredients(self):
        return self.get_text_on_element(TestMainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(TestMainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        self.wait_until_element_visibility(TestMainPageLocators.ORDER_IDENTIFICATOR)
        return self.get_text_on_element(TestMainPageLocators.ORDER_IDENTIFICATOR)

    @allure.step('Получение номера заказа')
    def get_order_id(self):
        self.wait_until_element_visibility(TestMainPageLocators.ORDER_IDENTIFICATOR)
        order_id = self.get_text_on_element(TestMainPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_text_on_element(TestMainPageLocators.ORDER_ID)
        return f"{order_id}"

    @allure.step("Закрыть модальное окно после создания заказа")
    def close_modal_order(self):
        self.find_element_with_wait(TestMainPageLocators.CLOSE_MODAL_ORDER)
        self.click_on_element(TestMainPageLocators.CLOSE_MODAL_ORDER)

    @allure.step("Создание заказа")
    def create_order(self):
        self.drag_and_drop_ingredient()
        self.click_order_button()
        self.check_displaying_of_confirmation_modal_of_order()
        self.get_order_id()
        self.close_modal_order()

