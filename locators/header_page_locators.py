from selenium.webdriver.common.by import By


class HeaderPageLocators:
    MY_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')
    ORDERS_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')
    CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')
