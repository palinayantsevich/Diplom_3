import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import MainPageData


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step('Click on "{section}" section.')
    def wait_click_on_section(self, section):
        self.wait_visibility_of_element(self.locators.build_section_locator(section))
        self.click_on_element_as_virtual_mouse(self.locators.build_section_locator(section))

    @allure.step('Click on the ingredient id="{ingredient}" in the section.')
    def wait_click_on_ingredient(self, ingredient):
        self.wait_visibility_of_element(self.locators.build_ingredient_locator(ingredient))
        self.click_on_element(self.locators.build_ingredient_locator(ingredient))

    @allure.step('Check if modal popup with ingredient details is opened.')
    def check_if_popup_details_is_opened(self):
        if self.wait_visibility_of_element(self.locators.MODAL_DETAILS_OPENED_STATE):
            return True
        else:
            return False

    @allure.step('Click on the closing icon in the modal popup with ingredient details.')
    def close_popup_details(self):
        self.wait_visibility_of_element(self.locators.MODAL_DETAILS_CLOSING_ICON)
        self.click_on_element(self.locators.MODAL_DETAILS_CLOSING_ICON)

    @allure.step('Check if modal popup with ingredient details is closed.')
    def check_if_popup_details_is_closed(self):
        if self.wait_unvisibility_of_element(self.locators.MODAL_DETAILS_OPENED_STATE):
            return True
        else:
            return False

    @allure.step('Add buns to the basket.')
    def add_bun_to_basket(self):
        self.drug_and_drop_element(self.locators.build_ingredient_locator(MainPageData.BUN_INGREDIENT_ID),
                                   self.locators.BASKET)

    @allure.step('Add sauce to the basket.')
    def add_sauce_to_basket(self):
        self.drug_and_drop_element(self.locators.build_ingredient_locator(MainPageData.SAUCE_INGREDIENT_ID),
                                   self.locators.BASKET)

    @allure.step('Add filing to the basket.')
    def add_filing_to_basket(self):
        self.drug_and_drop_element(self.locators.build_ingredient_locator(MainPageData.FILING_INGREDIENT_ID),
                                   self.locators.BASKET)

    @allure.step('Check counter value of bun ingredient.')
    def check_buns_counter(self):
        return self.get_element_text(self.locators.build_ingredient_counter_locator(MainPageData.BUN_INGREDIENT_ID))

    @allure.step('Check counter value of sauce ingredient.')
    def check_sauce_counter(self):
        return self.get_element_text(self.locators.build_ingredient_counter_locator(MainPageData.SAUCE_INGREDIENT_ID))

    @allure.step('Check counter value of filling ingredient.')
    def check_filling_counter(self):
        return self.get_element_text(self.locators.build_ingredient_counter_locator(MainPageData.FILING_INGREDIENT_ID))

    @allure.step('Click on "Оформить заказ" button.')
    def wait_click_on_place_order_button(self):
        self.wait_visibility_of_element(self.locators.PLACE_ORDER_BUTTON)
        self.click_on_element_as_virtual_mouse(self.locators.PLACE_ORDER_BUTTON)

    @allure.step('Check if "Order successfuly placed" modal popup is displayed.')
    def check_if_order_placed_popup_is_displayed(self):
        if self.wait_visibility_of_element(self.locators.ORDER_PLACED_MODAL):
            return True
        else:
            return False

    @allure.step('Place order.')
    def place_order(self):
        self.wait_click_on_section(MainPageData.BUNS_SECTION)
        self.add_bun_to_basket()
        self.wait_click_on_section(MainPageData.SAUCES_SECTION)
        self.add_sauce_to_basket()
        self.wait_click_on_section(MainPageData.FILINGS_SECTION)
        self.add_filing_to_basket()
        self.wait_click_on_place_order_button()

    @allure.step('Get order number after the order is placed.')
    def get_order_number(self):
        return self.get_element_text(self.locators.ORDER_PLACED_MODAL_ORDER_NUMBER)

    @allure.step('Close order placed popup.')
    def close_order_placed_popup(self):
        self.check_if_order_number_assigned()
        self.click_on_element(self.locators.ORDER_PLACED_MODAL_CLOSING_ICON)

    @allure.step('Check if order number is assigned instead of default.')
    def check_if_order_number_assigned(self):
        self.wait_for_text_matching_pattern(self.locators.ORDER_PLACED_MODAL_ORDER_NUMBER, r"\d{6}")
