import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import Urls


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step('Fill in the login form: "{email}", "{password}".')
    def wait_fill_login_form(self, email, password):
        self.wait_visibility_of_element(self.locators.EMAIL_FIELD)
        self.fill_input(self.locators.EMAIL_FIELD, email)
        self.wait_visibility_of_element(self.locators.PASSWORD_FIELD)
        self.fill_input(self.locators.PASSWORD_FIELD, password)

    @allure.step('Click on "Войти" button.')
    def wait_click_login_button(self):
        self.wait_element_is_clickable(self.locators.LOGIN_BUTTON)
        self.click_on_element_as_virtual_mouse(self.locators.LOGIN_BUTTON)

    @allure.step('Check if the user is logged-in.')
    def check_if_user_logged_in(self):
        self.wait_for_token_in_local_storage()

    @allure.step('Fill in the login form and log in.')
    def login_user(self, email, password):
        self.wait_fill_login_form(email, password)
        self.wait_click_login_button()
        self.check_if_user_logged_in()

    @allure.step('Click on "Восстановить пароль" link.')
    def click_on_forgot_password_link(self):
        self.click_on_element_as_virtual_mouse(self.locators.FORGOT_PASSWORD_LINK)

    @allure.step('Wait until "Forgot password" page is loaded.')
    def wait_for_load_forgot_password_page(self):
        self.wait_load_page_by_checking_url(Urls.FORGOT_PASSWORD_PAGE)
