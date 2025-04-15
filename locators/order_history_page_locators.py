from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    FIRST_ORDER_COMPLETED = (By.XPATH, '//ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]/li[1]')
    FIRST_ORDER_NUMBER = (By.XPATH, '//ul/li[1]//p[@class="text text_type_digits-default"]')
