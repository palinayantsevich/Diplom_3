import pytest
import allure

from selenium import webdriver

from api.user_api import RegisterUserAPI, DeleteUserAPI
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.order_history_page import OrderHistoryPage
from pages.main_page import MainPage
from helper import Helper
from urls import Urls


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    with allure.step('Open browser.'):
        browser = None

    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        browser = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--height=1024")
        firefox_options.add_argument("--width=1920")
        browser = webdriver.Firefox(options=firefox_options)
    browser.get(Urls.MAIN_PAGE)

    yield browser

    with allure.step('Close browser.'):
        browser.quit()


@pytest.fixture(scope='function')
def generate_user_data():
    email = Helper.generate_user_email()
    password = Helper.generate_user_password()
    name = Helper.generate_user_name()

    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    return payload


@pytest.fixture(scope='function')
def register_and_delete_user(generate_user_data):
    with allure.step('Register new user.'):
        register_user = RegisterUserAPI.register_user(generate_user_data['email'], generate_user_data['password'],
                                                      generate_user_data['name'])
    token = register_user.json()['accessToken']
    yield register_user
    with allure.step('Delete user.'):
        DeleteUserAPI.delete_user(token)


@pytest.fixture(scope='function')
def login_user(register_and_delete_user, generate_user_data, driver):
    login_user = LoginPage(driver)
    login_user.open_page(Urls.LOGIN_PAGE)
    login_user.login_user(generate_user_data['email'], generate_user_data['password'])


@pytest.fixture(scope='function')
def order_history_page(driver):
    order_history_page = OrderHistoryPage(driver)
    return order_history_page


@pytest.fixture(scope='function')
def main_page(driver):
    main_page = MainPage(driver)
    return main_page


@pytest.fixture(scope='function')
def header_page(driver):
    header_page = HeaderPage(driver)
    return header_page


@pytest.fixture(scope='function')
def my_account_page(driver):
    my_account_page = MyAccountPage(driver)
    return my_account_page
