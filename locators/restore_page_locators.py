'''Локаторы страницы восстановления пароля.'''
from selenium.webdriver.common.by import By

from .patterns import BUTTON_TXT, DIV_CONTAINS_CLS, HEADER_TXT, INPUT_ATTR, LABEL_TXT

EMAIL_INPUT = By.XPATH, INPUT_ATTR.format('name', 'name')
ENTER_CODE_LABEL = By.XPATH, LABEL_TXT.format('Введите код из письма')
EYE_BTN = By.XPATH, DIV_CONTAINS_CLS.format('input__icon')
PASSWORD_FRAME = By.XPATH, LABEL_TXT.format('Пароль') + '/ancestor::div[1]'
RESTORE_BTN = By.XPATH, BUTTON_TXT.format('Восстановить')
RESTORE_PASS_TITLE = By.XPATH, HEADER_TXT.format('Восстановление пароля')
