'''Локаторы страницы авторизации.'''
from selenium.webdriver.common.by import By

from .patterns import BUTTON_TXT, HEADER_TXT, INPUT_ATTR, LINK_TXT


EMAIL_INPUT = By.XPATH, INPUT_ATTR.format('name', 'name')
ENTER_BTN = By.XPATH, BUTTON_TXT.format('Войти')
ENTRANCE_TITLE = By.XPATH, HEADER_TXT.format('Вход')
PASSWORD_INPUT = By.XPATH, INPUT_ATTR.format('name', 'Пароль')
RESTORE_PASS_LINK = By.XPATH, LINK_TXT.format('Восстановить пароль')
