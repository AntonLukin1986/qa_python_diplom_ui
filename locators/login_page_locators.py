'''Локаторы страницы авторизации.'''
from selenium.webdriver.common.by import By

from .patterns import LINK_TXT                                  # кажется, что с __init__.py точка не нужна будет???


RESTORE_PASS_LINK = By.XPATH, LINK_TXT.format('Восстановить пароль')
