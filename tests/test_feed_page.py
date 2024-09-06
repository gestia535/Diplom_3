import allure
import pytest
from locators.feed_page_locators import TestFeedPageLocators


class TestFeedPage:

    @allure.title('Проверка, если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_card_open_popup(self, driver, main_page, feed_page):
        main_page.click_order_feed_button()
        feed_page.get_text_on_title_of_feed()
        feed_page.click_on_order_card()
        assert 'бургер' in feed_page.get_title_of_order_popup()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_displaying_in_feed_new_order_from_history_success(self, driver, main_page, user_acc_page,
                                                               order_history_page, feed_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.drag_and_drop_ingredient()
        main_page.click_order_button()
        main_page.check_displaying_of_confirmation_modal_of_order()
        order_number = main_page.get_order_id()
        main_page.close_modal_order()
        main_page.click_account_button()
        user_acc_page.click_order_history_button()
        order_id_history = order_history_page.is_order_id_found_at_history(order_number)
        main_page.click_order_feed_button()
        order_id_feed = feed_page.is_order_id_found_at_feed(order_number)
        assert order_id_history and order_id_feed

    @allure.title('При создании заказа, происходит увеличения значения счетчиков заказов '
                  '"Выполнено за все время"/"Выполнено за сегодня"')
    @pytest.mark.parametrize('counter', [TestFeedPageLocators.TOTAL_ORDER_COUNT,
                                         TestFeedPageLocators.DAILY_ORDER_COUNT])
    def test_today_orders_counter(self, driver, counter, main_page, user_acc_page, feed_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.click_order_feed_button()
        first_value = feed_page.get_total_orders_daily(counter)
        main_page.click_constructor_button()
        main_page.create_order()
        main_page.click_order_feed_button()
        second_value = feed_page.get_total_orders_daily(counter)
        assert second_value > first_value

    @allure.title('Проверка отображения номера заказа в разделе "В работе')
    def test_new_order_displaying_in_progress_block(self, driver, main_page, user_acc_page, feed_page):
        main_page.click_login_button()
        user_acc_page.login()
        main_page.drag_and_drop_ingredient()
        main_page.click_order_button()
        main_page.check_displaying_of_confirmation_modal_of_order()
        order_number = main_page.get_order_id()
        main_page.close_modal_order()
        main_page.click_order_feed_button()
        order_number_rename = feed_page.get_user_order(order_number)
        order_in_progress = feed_page.get_user_order_in_progress()
        assert order_number_rename == order_in_progress
