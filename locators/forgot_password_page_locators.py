from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    RESTORE_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    RESTORE_PASSWORD_INPUT = (By.XPATH, '//input[@name="Введите новый пароль"]')
    RESTORE_PASSWORD_HIDE_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    RESTORE_PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/parent::div')
