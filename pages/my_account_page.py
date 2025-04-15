import allure

from pages.base_page import BasePage
from locators.my_account_page_locators import MyAccountPageLocators
from urls import Urls


class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MyAccountPageLocators()

    @allure.step('Open "My Account" page.')
    def open_my_account_page(self):
        self.click_on_element_as_virtual_mouse(self.locators.MY_ACCOUNT_HEADER_BUTTON)

    @allure.step('Click on "История заказов" button in My Account.')
    def wait_click_order_history_button(self):
        self.wait_element_is_clickable(self.locators.ORDER_HISTORY_BUTTON)
        self.click_on_element(self.locators.ORDER_HISTORY_BUTTON)

    @allure.step('Click on "Выход" button in My Account.')
    def wait_click_log_out_button(self):
        self.wait_element_is_clickable(self.locators.LOG_OUT_BUTTON)
        self.click_on_element(self.locators.LOG_OUT_BUTTON)

    @allure.step('Wait until "Order history" page is loaded.')
    def wait_for_load_order_history_page(self):
        self.wait_load_page_by_checking_url(Urls.ORDER_HISTORY)

    @allure.step('Wait until "Login" page is loaded.')
    def wait_for_load_login_page(self):
        self.wait_load_page_by_checking_url(Urls.LOGIN_PAGE)

    @allure.step('Check if the user is logged-out.')
    def check_if_user_logged_out(self):
        self.wait_for_token_removed_from_local_storage()
