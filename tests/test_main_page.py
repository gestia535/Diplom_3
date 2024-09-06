import allure
from pages.feed_page import FeedPage


class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_click_constructor_button(self, driver, main_page):
        main_page.click_order_feed_button()
        main_page.click_constructor_button()
        assert 'Соберите бургер' in main_page.get_text_on_title_of_constructor()

    @allure.title('Проверка перехода по клику на «Ленту заказов»')
    def test_click_feed_button(self, driver, main_page):
        main_page.click_order_feed_button()
        feed_page_obj = FeedPage(driver)
        assert 'Лента заказов' in feed_page_obj.get_text_on_title_of_feed()

    @allure.title('Проверка отображения окна "Детали ингредиента" при клике на ингредиент')
    def test_displaying_popup_with_details(self, driver, main_page):
        main_page.click_ingredient()
        assert main_page.check_open_popup_with_details()

    @allure.title('Проверка закрытия всплывающего окна кликом по крестику')
    def test_close_ingredient_details_popup_with_close_button(self, driver, main_page):
        main_page.click_ingredient()
        main_page.click_on_close_button_popup()
        assert main_page.check_not_displaying_of_modal_details()

    @allure.title('При добавлении ингридиента в заказ, счетчик увеличивается')
    def test_ingredient_quantity_increase_in_counter(self, driver, main_page):
        main_page.drag_and_drop_ingredient()
        assert main_page.count_ingredients() == '2'

    @allure.title('Проверка возможности оформления заказ авторизованным пользователем')
    def test_successful_order_login_user(self, driver, main_page, user_acc_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.drag_and_drop_ingredient()
        main_page.click_order_button()
        assert main_page.check_displaying_of_confirmation_modal_of_order()
