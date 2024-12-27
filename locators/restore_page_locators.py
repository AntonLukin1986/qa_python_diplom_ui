'''Локаторы страницы восстановления пароля.'''
from selenium.webdriver.common.by import By

from data import Restore

from .patterns import BUTTON_TXT, DIV_CONTAINS_CLS, HEADER_TXT, LABEL_TXT

EMAIL_INPUT = By.XPATH, LABEL_TXT.format('Email') + '/../input'
ENTER_CODE_LABEL = By.XPATH, LABEL_TXT.format(Restore.ENTER_CODE)
EYE_BTN = By.XPATH, DIV_CONTAINS_CLS.format('input__icon')
PASSWORD_INPUT = By.XPATH, LABEL_TXT.format('Пароль') + '/parent::div'
RESTORE_BTN = By.XPATH, BUTTON_TXT.format('Восстановить')
RESTORE_PASS_HEADER = By.XPATH, HEADER_TXT.format(Restore.TITLE)
