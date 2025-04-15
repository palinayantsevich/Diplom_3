import allure

import re

from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait_time=15):
        self.driver = driver
        self.wait_time = wait_time

    @allure.step('Open page: {url}.')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Wait until the element is displayed: {locator}.')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located(locator))

    @allure.step('Wait until the element is not displayed: {locator}.')
    def wait_unvisibility_of_element(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(EC.invisibility_of_element_located(locator))

    @allure.step('Wait until the element is clickable: {locator}.')
    def wait_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(EC.element_to_be_clickable(locator))

    @allure.step('Wait until the page is loaded and check page url: {url}.')
    def wait_load_page_by_checking_url(self, url):
        return WebDriverWait(self.driver, self.wait_time).until(EC.url_to_be(url))

    @allure.step('Fill the input field {locator} with value: {text}.')
    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Click on element: {locator}.')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Get the field attribute.')
    def get_field_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step('Get current page url.')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Click on element: {locator}.')
    def click_on_element_as_virtual_mouse(self, locator):
        action = ActionChains(self.driver)
        self.wait_element_is_clickable(locator)
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    @allure.step('Check if token "{token_key}" is presented in Local Storage.')
    def wait_for_token_in_local_storage(self, token_key='accessToken', timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script(f"return window.localStorage.getItem('{token_key}')") is not None,
            message=f"Token '{token_key}' is not found in localStorage"
        )

    @allure.step('Check if token "{token_key}" is removed from Local Storage.')
    def wait_for_token_removed_from_local_storage(self, token_key='accessToken', timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script(f"return window.localStorage.getItem('{token_key}')") is None,
            message=f"Token '{token_key}' is still present in localStorage"
        )

    @allure.step('Drug-and-drop element.')
    def drug_and_drop_element(self, locator_source, locator_target, timeout=1):
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(timeout).perform()

    @allure.step('Get text of the element: {locator}.')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Collect the list of elements.')
    def collect_the_list_of_elements(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Ожидание, что текст в элементе {locator} соответствует шаблону: "{pattern}".')
    def wait_for_text_matching_pattern(self, locator, pattern, timeout=20):
        def check_text_matches(driver):
            try:
                text = driver.find_element(*locator).text.strip()
                return re.fullmatch(pattern, text) is not None
            except:
                return False

        return WebDriverWait(self.driver, timeout).until(check_text_matches)
