'''Локаторы страницы восстановления пароля.'''
from selenium.webdriver.common.by import By

from . import patterns as p

EMAIL_INPUT = By.XPATH, p.INPUT_ATTR.format('name', 'name')
ENTER_CODE_LABEL = By.XPATH, p.LABEL_TXT.format('Введите код из письма')
EYE_BTN = By.XPATH, p.DIV_CONTAINS_CLS.format('input__icon')
PASSWORD_FRAME = By.XPATH, p.LABEL_TXT.format('Пароль') + p.UP.format('div[1]')
RESTORE_BTN = By.XPATH, p.BUTTON_TXT.format('Восстановить')
RESTORE_PASS_TITLE = By.XPATH, p.HEADER2_TXT.format('Восстановление пароля')
