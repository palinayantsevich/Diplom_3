import allure

from pages.base_page import BasePage
from locators.order_history_page_locators import OrderHistoryPageLocators


class OrderHistoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderHistoryPageLocators()

    @allure.step('Click on first order in a list.')  # delete
    def wait_click_on_order(self):
        self.wait_visibility_of_element(self.locators.FIRST_ORDER_COMPLETED)
        self.click_on_element(self.locators.FIRST_ORDER_COMPLETED)

    @allure.step('Check order number.')
    def check_order_number(self):
        self.wait_visibility_of_element(self.locators.FIRST_ORDER_NUMBER)
        return self.get_element_text(self.locators.FIRST_ORDER_NUMBER)
