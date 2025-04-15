from selenium.webdriver.common.by import By


class MainPageLocators:
    MODAL_DETAILS_OPENED_STATE = (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]')
    MODAL_DETAILS_CLOSING_ICON = (By.XPATH,
                                  '//div[@class="Modal_modal__container__Wo2l_"]/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    BASKET = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]')
    PLACE_ORDER_BUTTON = (By.XPATH,
                          '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    ORDER_PLACED_MODAL = (By.XPATH, '//div[@class="Modal_modal__container__Wo2l_"]')
    ORDER_PLACED_MODAL_CLOSING_ICON = (
        By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    ORDER_PLACED_MODAL_ORDER_NUMBER = (By.XPATH,
                                       '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')

    def build_section_locator(self, section):
        return (By.XPATH, f'//span[text()="{section}"]')

    def build_ingredient_locator(self, ingredient):
        return (By.XPATH, f'//a[@href="/ingredient/{ingredient}"]')

    def build_ingredient_counter_locator(self, ingredient):
        return (By.XPATH, f'//a[@href="/ingredient/{ingredient}"]//p[@class="counter_counter__num__3nue1"]')
