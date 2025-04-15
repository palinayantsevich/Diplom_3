import allure

from pages.login_page import LoginPage
from urls import Urls


class TestLoginPage:

    @allure.title(
        'Verify that user is navigated to the "Восстановление пароля": step#1 page after clicking on the "Восстановить пароль" button on the Login page.')
    def test_check_redirect_to_forgot_password_from_login_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_PAGE)
        login_page.click_on_forgot_password_link()
        login_page.wait_for_load_forgot_password_page()
        current_url = login_page.get_current_url()
        assert current_url == Urls.FORGOT_PASSWORD_PAGE
