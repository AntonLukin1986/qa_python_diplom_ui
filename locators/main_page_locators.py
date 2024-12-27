'''Локаторы главной страницы.'''
from selenium.webdriver.common.by import By

from .patterns import BUTTON_TXT


ENTER_ACCOUN_BTN = By.XPATH, BUTTON_TXT.format('Войти в аккаунт')
