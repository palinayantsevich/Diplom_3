import allure

from pages.order_feed_page import OrderFeedPage
from urls import Urls


class TestOrderFeedPage:

    @allure.title(
        'Verify that user can review order details in the modal popup opened by clicking on the order card.')
    def test_check_popup_order_details_opened_if_click_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_page(Urls.ORDER_FEED)
        order_feed_page.wait_click_on_order()
        modal_displayed = order_feed_page.check_if_popup_order_details_is_opened()
        assert modal_displayed == True

    @allure.title(
        'Verify that orders from My account -> Order History page is displayed in the "Лента Заказов" page.')
    def test_check_orders_from_order_history_is_displayed_in_order_feed_page(self, driver, login_user,
                                                                             order_history_page, main_page, header_page,
                                                                             my_account_page):
        order_feed_page = OrderFeedPage(driver)
        main_page.place_order()
        main_page.close_order_placed_popup()
        header_page.click_my_account_button()
        my_account_page.wait_click_order_history_button()
        order_number = order_history_page.check_order_number()
        header_page.click_orders_feed_button()
        header_page.wait_for_load_orders_feed_page()
        order_feed_page.wait_text_all_orders_ready_is_not_displayed()
        is_order_number_in_order_list = order_feed_page.find_order_number_in_list_of_orders(order_number)
        assert is_order_number_in_order_list == True

    @allure.title(
        'Verify that after the order is placed - its number is displayed in "В работе" section in the Order Feed page.')
    def test_check_order_number_displayed_in_orders_processing_section(self, driver, login_user, main_page,
                                                                       header_page):
        order_feed_page = OrderFeedPage(driver)
        main_page.place_order()
        main_page.close_order_placed_popup()
        order_number = main_page.get_order_number()
        header_page.click_orders_feed_button()
        header_page.wait_for_load_orders_feed_page()
        order_feed_page.wait_text_all_orders_ready_is_not_displayed()
        orders_processing_list = order_feed_page.get_orders_numbers_from_orders_processing_section()
        assert order_number in orders_processing_list

    @allure.title(
        'Verify that "Выполнено за всё время" counter value is increased after the order is placed.')
    def test_counter_all_times_increased_after_order_placed(self, driver, login_user, main_page, header_page):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_page(Urls.ORDER_FEED)
        initial_counter_value = order_feed_page.check_counter_all_times_value()
        header_page.click_constructor_button()
        header_page.wait_for_load_main_page()
        main_page.place_order()
        main_page.close_order_placed_popup()
        header_page.click_orders_feed_button()
        header_page.wait_for_load_orders_feed_page()
        order_feed_page.wait_text_all_orders_ready_is_not_displayed()
        final_counter_value = order_feed_page.check_counter_all_times_value()
        assert final_counter_value > initial_counter_value

    @allure.title(
        'Verify that "Выполнено за сегодня" counter value is increased after the order is placed.')
    def test_counter_today_increased_after_order_placed(self, driver, login_user, main_page, header_page):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_page(Urls.ORDER_FEED)
        initial_counter_value = order_feed_page.check_counter_today_value()
        header_page.click_constructor_button()
        header_page.wait_for_load_main_page()
        main_page.place_order()
        main_page.close_order_placed_popup()
        header_page.click_orders_feed_button()
        header_page.wait_for_load_orders_feed_page()
        order_feed_page.wait_text_all_orders_ready_is_not_displayed()
        final_counter_value = order_feed_page.check_counter_today_value()
        assert final_counter_value > initial_counter_value
