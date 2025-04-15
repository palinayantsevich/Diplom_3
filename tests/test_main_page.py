import allure
import pytest

from pages.main_page import MainPage
from data import MainPageData


class TestMainPage:

    @allure.title(
        'Verify that user can review burger ingredient details in the modal popup opened by clicking on the ingredient card.')
    @pytest.mark.parametrize(
        'section,ingredient',
        [
            (MainPageData.BUNS_SECTION, MainPageData.BUN_INGREDIENT_ID),
            (MainPageData.SAUCES_SECTION, MainPageData.SAUCE_INGREDIENT_ID),
            (MainPageData.FILINGS_SECTION, MainPageData.FILING_INGREDIENT_ID),
        ]
    )
    def test_check_popup_details_opened_if_click_ingredient(self, driver, section, ingredient):
        main_page = MainPage(driver)
        main_page.wait_click_on_section(section)
        main_page.wait_click_on_ingredient(ingredient)
        modal_displayed = main_page.check_if_popup_details_is_opened()
        assert modal_displayed == True

    @allure.title(
        'Verify that user can close modal popup ingredient details.')
    @pytest.mark.parametrize(
        'section,ingredient',
        [
            (MainPageData.BUNS_SECTION, MainPageData.BUN_INGREDIENT_ID),
            (MainPageData.SAUCES_SECTION, MainPageData.SAUCE_INGREDIENT_ID),
            (MainPageData.FILINGS_SECTION, MainPageData.FILING_INGREDIENT_ID),
        ]
    )
    def test_check_popup_details_closed_if_click_ingredient(self, driver, section, ingredient):
        main_page = MainPage(driver)
        main_page.wait_click_on_section(section)
        main_page.wait_click_on_ingredient(ingredient)
        main_page.close_popup_details()
        modal_not_displayed = main_page.check_if_popup_details_is_closed()
        assert modal_not_displayed == True

    @allure.title(
        'Verify that when user add bun to basket - the bun count value is increased.')
    def test_add_bun_to_basket_counter_increased(self, driver):
        main_page = MainPage(driver)
        main_page.wait_click_on_section(MainPageData.BUNS_SECTION)
        bun_counter_initial = int(main_page.check_buns_counter())
        main_page.add_bun_to_basket()
        bun_counter_final = int(main_page.check_buns_counter())
        assert bun_counter_final == (bun_counter_initial + 2)

    @allure.title(
        'Verify that when user add sauce to basket - the sauce count value is increased.')
    def test_add_sauce_to_basket_counter_increased(self, driver):
        main_page = MainPage(driver)
        main_page.wait_click_on_section(MainPageData.SAUCES_SECTION)
        sauce_counter_initial = int(main_page.check_sauce_counter())
        main_page.add_sauce_to_basket()
        sauce_counter_final = int(main_page.check_sauce_counter())
        assert sauce_counter_final == (sauce_counter_initial + 1)

    @allure.title(
        'Verify that when user add filling to basket - the filling count value is increased.')
    def test_add_filling_to_basket_counter_increased(self, driver):
        main_page = MainPage(driver)
        main_page.wait_click_on_section(MainPageData.FILINGS_SECTION)
        filling_counter_initial = int(main_page.check_filling_counter())
        main_page.add_filing_to_basket()
        filling_counter_final = int(main_page.check_filling_counter())
        assert filling_counter_final == (filling_counter_initial + 1)

    @allure.title(
        'Verify that logged-in user can place order.')
    def test_create_order_created_successfully(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.place_order()
        order_placed = main_page.check_if_order_placed_popup_is_displayed()
        assert order_placed == True
