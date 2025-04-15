import allure

from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from data import ForgotPasswordPageData
from urls import Urls


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordPageLocators()

    @allure.step('Wait and fill in the "email" filed in the forgot password form: "{email}".')
    def wait_fill_email_field(self, email):
        self.fill_input(self.locators.EMAIL_FIELD, email)

    @allure.step('Wait and click on "Восстановить" button.')
    def click_restore_button(self):
        self.click_on_element_as_virtual_mouse(self.locators.RESTORE_BUTTON)

    @allure.step('Wait until "Пароль" field is displayed and enter new password.')
    def wait_enter_new_password(self, new_password):
        self.wait_visibility_of_element(self.locators.RESTORE_PASSWORD_INPUT)
        self.fill_input(self.locators.RESTORE_PASSWORD_INPUT, new_password)

    @allure.step('Click on "Hide/display password" icon.')
    def wait_click_hide_icon(self):
        self.click_on_element_as_virtual_mouse(self.locators.RESTORE_PASSWORD_HIDE_ICON)

    @allure.step('Check if the password is displayed in "Пароль" field.')
    def check_password_display(self):
        return self.get_field_attribute(self.locators.RESTORE_PASSWORD_FIELD,
                                        ForgotPasswordPageData.ACTIVE_STATE_ATTRIBUTE)

    @allure.step('Wait until "Reset password" page is loaded.')
    def wait_for_load_reset_password_page(self):
        self.wait_load_page_by_checking_url(Urls.FORGOT_PASSWORD_RESET_PASSWORD_PAGE)
