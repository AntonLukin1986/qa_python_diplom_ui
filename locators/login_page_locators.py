'''Локаторы страницы авторизации.'''
from selenium.webdriver.common.by import By

from . import patterns as p

EMAIL_INPUT = By.XPATH, p.INPUT_ATTR.format('name', 'name')
ENTER_BTN = By.XPATH, p.BUTTON_TXT.format('Войти')
ENTRANCE_TITLE = By.XPATH, p.HEADER2_TXT.format('Вход')
PASSWORD_INPUT = By.XPATH, p.INPUT_ATTR.format('name', 'Пароль')
RESTORE_PASS_LINK = By.XPATH, p.LINK_TXT.format('Восстановить пароль')
