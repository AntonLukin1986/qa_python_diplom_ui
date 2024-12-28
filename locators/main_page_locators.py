'''Локаторы главной страницы.'''
from selenium.webdriver.common.by import By

from .patterns import BUTTON_TXT, LINK_ATTR


ENTER_ACCOUNT_BTN = By.XPATH, BUTTON_TXT.format('Войти в аккаунт')
PERSONAL_ACCOUNT_LINK = By.XPATH, LINK_ATTR.format('href', '/account')
