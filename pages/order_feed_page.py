import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators()

    @allure.step('Click on first order in a list.')
    def wait_click_on_order(self):
        self.wait_visibility_of_element(self.locators.FIRST_ORDER_IN_LIST)
        self.click_on_element(self.locators.FIRST_ORDER_IN_LIST)

    @allure.step('Check if modal popup with order details is displayed.')
    def check_if_popup_order_details_is_opened(self):
        if self.wait_visibility_of_element(self.locators.ORDER_DETAILS_MODAL):
            return True
        else:
            return False

    @allure.step('Find "{order_number}" in the list of last orders.')
    def find_order_number_in_list_of_orders(self, order_number):
        orders_list = self.collect_the_list_of_elements(self.locators.ORDER_NUMBERS)
        for order in orders_list:
            if order_number == order.text:
                return True
        return False

    @allure.step('Check "Выполнено за всё время" counter value.')
    def check_counter_all_times_value(self):
        self.wait_visibility_of_element(self.locators.ORDERS_PLACED_ALL_TIMES)
        return self.get_element_text(self.locators.ORDERS_PLACED_ALL_TIMES)

    @allure.step('Check "Выполнено за сегодня" counter value.')
    def check_counter_today_value(self):
        self.wait_visibility_of_element(self.locators.ORDERS_PLACED_TODAY)
        return self.get_element_text(self.locators.ORDERS_PLACED_TODAY)

    @allure.step('Get orders numbers from "В работе" section.')
    def get_orders_numbers_from_orders_processing_section(self):
        self.wait_visibility_of_element(self.locators.ORDER_ID_PROCESSING)
        return self.get_element_text(self.locators.ORDER_ID_PROCESSING)

    @allure.step('Check if "Все текущие заказы готовы!" text is not displayed.')
    def wait_text_all_orders_ready_is_not_displayed(self):
        self.wait_unvisibility_of_element(self.locators.NO_ORDERS_PROCESSING_TEXT)
