from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    FIRST_ORDER_IN_LIST = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li[1]')
    ORDER_DETAILS_MODAL = (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]')
    ORDER_NUMBERS = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    ORDERS_PLACED_ALL_TIMES = (By.XPATH, '//*[text()="Выполнено за все время:"]/following::*[@class][1]')
    ORDERS_PLACED_TODAY = (By.XPATH, '//*[text()="Выполнено за сегодня:"]/following::*[@class][1]')
    ORDER_ID_PROCESSING = (
    By.XPATH, '//*[text()="В работе:"]/following::li[@class="text text_type_digits-default mb-2"][6]')
    NO_ORDERS_PROCESSING_TEXT = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')
