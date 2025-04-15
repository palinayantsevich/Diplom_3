import allure

from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
from urls import Urls


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderPageLocators()

    @allure.step('Click on "Конструктор" in the page header.')
    def click_constructor_button(self):
        self.click_on_element_as_virtual_mouse(self.locators.CONSTRUCTOR)

    @allure.step('Click on "Лента Заказов" in the page header.')
    def click_orders_feed_button(self):
        self.click_on_element_as_virtual_mouse(self.locators.ORDERS_FEED)

    @allure.step('Click on "Личный Кабинет" in the page header.')
    def click_my_account_button(self):
        self.click_on_element_as_virtual_mouse(self.locators.MY_ACCOUNT)

    @allure.step('Wait until "Main" page is loaded.')
    def wait_for_load_main_page(self):
        self.wait_load_page_by_checking_url(Urls.MAIN_PAGE)

    @allure.step('Wait until "Orders list" page is loaded.')
    def wait_for_load_orders_feed_page(self):
        self.wait_load_page_by_checking_url(Urls.ORDER_FEED)

    @allure.step('Wait until "Login" page is loaded.')
    def wait_for_load_login_page(self):
        self.wait_load_page_by_checking_url(Urls.LOGIN_PAGE)

    @allure.step('Wait until "My Account" page is loaded.')
    def wait_for_load_my_account_page(self):
        self.wait_load_page_by_checking_url(Urls.MY_ACCOUNT)
