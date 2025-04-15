import allure

from pages.forgot_password_page import ForgotPasswordPage
from urls import Urls
from helper import Helper
from data import ForgotPasswordPageData


class TestForgotPasswordPage:

    @allure.title(
        'Verify that user is navigated to the "Восстановление пароля": step#2 page after entering email and clicking on "Восстановить" button on the forgot password page.')
    def test_check_redirect_to_forgot_password_from_login_page_header(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        forgot_password_page.wait_fill_email_field(Helper.generate_user_email())
        forgot_password_page.click_restore_button()
        forgot_password_page.wait_for_load_reset_password_page()
        current_url = forgot_password_page.get_current_url()
        assert current_url == Urls.FORGOT_PASSWORD_RESET_PASSWORD_PAGE

    @allure.title(
        'Verify that user can show entered password in the "Пароль" field on the "Восстановление пароля": step#2 page.')
    def test_show_entered_password_forgot_password_page(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        forgot_password_page.wait_fill_email_field(Helper.generate_user_email())
        forgot_password_page.click_restore_button()
        forgot_password_page.wait_enter_new_password(Helper.generate_user_password())
        forgot_password_page.wait_click_hide_icon()
        password_field_state = forgot_password_page.check_password_display()
        assert ForgotPasswordPageData.ACTIVE_STATE_PROPERTY in password_field_state
