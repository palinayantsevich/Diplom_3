from selenium.webdriver.common.by import By


class MyAccountPageLocators:
    ORDER_HISTORY_BUTTON = (
    By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive"]')
    LOG_OUT_BUTTON = (
    By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
    MY_ACCOUNT_HEADER_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
