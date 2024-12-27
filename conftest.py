'''Фикстуры для тестов.'''
import pytest
from selenium import webdriver

from config import BROWSERS, MAIN_PAGE
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.restore_page import RestorePage


@pytest.fixture(scope='function')
def login_page(driver):
    '''Объект страницы авторизации.'''
    return LoginPage(driver)


@pytest.fixture(scope='function')
def main_page(driver):
    '''Объект главной страницы.'''
    return MainPage(driver)


@pytest.fixture(scope='function')
def restore_page(driver):
    '''Объект страницы восстановления пароля.'''
    return RestorePage(driver)


@pytest.fixture(scope='function', params=BROWSERS, ids=BROWSERS)
def driver(request):
    '''Создание драйвера браузера с последующим закрытием.'''
    name = request.param
    options = getattr(webdriver, f'{name}Options')()
    for argument in BROWSERS[name]:
        options.add_argument(argument)
    driver = getattr(webdriver, name)(options)
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()
