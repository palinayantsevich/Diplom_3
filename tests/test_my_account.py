import allure

from pages.my_account_page import MyAccountPage
from urls import Urls


class TestMyAccountPage:

    @allure.title(
        'Verify that user is navigated to the Order History page after clicking on the "История заказов" button on the Login page.')
    def test_check_redirect_to_order_history_from_my_account_page(self, driver, login_user):
        my_account = MyAccountPage(driver)
        my_account.open_my_account_page()
        my_account.wait_click_order_history_button()
        my_account.wait_for_load_order_history_page()
        current_url = my_account.get_current_url()
        assert current_url == Urls.ORDER_HISTORY

    @allure.title(
        'Verify that user is logged-out after clicking on the "Выход" button on the Login page.')
    def test_check_user_logged_out_from_my_account_page(self, driver, login_user):
        my_account = MyAccountPage(driver)
        my_account.open_my_account_page()
        my_account.wait_click_log_out_button()
        my_account.wait_for_load_login_page()
        my_account.wait_for_token_removed_from_local_storage()
        current_url = my_account.get_current_url()
        assert current_url == Urls.LOGIN_PAGE
