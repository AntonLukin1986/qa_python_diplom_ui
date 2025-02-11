'''Фикстуры для тестов.'''
import pytest
import requests
from selenium import webdriver

from config import API_CREATE_USER, API_DELETE_USER, BROWSERS, MAIN_PAGE
from helpers import get_user_data
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.restore_page import RestorePage


@pytest.fixture(scope='function')
def header_page(driver):
    '''Объект хедера всех страниц.'''
    return HeaderPage(driver)


@pytest.fixture(scope='function')
def profile_page(driver):
    '''Объект страницы профиля пользователя.'''
    return ProfilePage(driver)


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


@pytest.fixture(scope='session')
def test_user():
    '''Создание пользователя с последующим удалением.'''
    user_data = get_user_data()
    token = requests.post(
        url=API_CREATE_USER, data=user_data
    ).json().get('accessToken')
    del user_data['name']
    yield user_data  # email & password
    requests.delete(url=API_DELETE_USER, headers={'Authorization': token})
