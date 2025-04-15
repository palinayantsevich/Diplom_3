import allure
import pytest

from pages.header_page import HeaderPage
from urls import Urls


class TestHeaderPage:

    @allure.title(
        'Verify that user is navigated to the "Main" page after clicking on the "Конструктор" button the page header.')
    @pytest.mark.parametrize(
        'url',
        [
            Urls.LOGIN_PAGE,
            Urls.ORDER_FEED,
            Urls.FORGOT_PASSWORD_PAGE
        ]
    )
    def test_check_redirect_to_main_page_after_clicking_on_constructor_button(self, driver, url):
        header_page = HeaderPage(driver)
        header_page.open_page(url)
        header_page.click_constructor_button()
        header_page.wait_for_load_main_page()
        current_url = header_page.get_current_url()
        assert current_url == Urls.MAIN_PAGE

    @allure.title(
        'Verify that user is navigated to the "Orders list" page after clicking on the "Лента Заказов" button the page header.')
    @pytest.mark.parametrize(
        'url',
        [
            Urls.LOGIN_PAGE,
            Urls.MAIN_PAGE,
            Urls.FORGOT_PASSWORD_PAGE
        ]
    )
    def test_check_redirect_to_orders_feed_page_after_clicking_on_orders_list_button(self, driver, url):
        header_page = HeaderPage(driver)
        header_page.open_page(url)
        header_page.click_orders_feed_button()
        header_page.wait_for_load_orders_feed_page()
        current_url = header_page.get_current_url()
        assert current_url == Urls.ORDER_FEED

    @allure.title(
        'Verify that guest user is navigated to the "Login" page after clicking on the "Личный Кабинет" button the page header.')
    @pytest.mark.parametrize(
        'url',
        [
            Urls.ORDER_FEED,
            Urls.MAIN_PAGE,
            Urls.FORGOT_PASSWORD_PAGE
        ]
    )
    def test_check_redirect_to_login_page_after_clicking_on_my_account_button_guest_user(self, driver, url):
        header_page = HeaderPage(driver)
        header_page.open_page(url)
        header_page.click_my_account_button()
        header_page.wait_for_load_login_page()
        current_url = header_page.get_current_url()
        assert current_url == Urls.LOGIN_PAGE

    @allure.title(
        'Verify that logged-in user is navigated to the "My Account" page after clicking on the "Личный Кабинет" button the page header.')
    @pytest.mark.parametrize(
        'url',
        [
            Urls.ORDER_FEED,
            Urls.MAIN_PAGE,
        ]
    )
    def test_check_redirect_to_login_page_after_clicking_on_my_account_button_loggedin_user(self, driver, login_user, url):
        header_page = HeaderPage(driver)
        header_page.open_page(url)
        header_page.click_my_account_button()
        header_page.wait_for_load_my_account_page()
        current_url = header_page.get_current_url()
        assert current_url == Urls.MY_ACCOUNT
