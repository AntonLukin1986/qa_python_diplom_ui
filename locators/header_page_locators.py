'''Локаторы главной страницы.'''
from selenium.webdriver.common.by import By

from . import patterns as p

HEADER_LINK = By.XPATH, p.PARAG_TXT + p.UP.format('a')
LOGO_LINK = By.XPATH, p.LINK_ATTR.format('href', '/')
PERSONAL_ACCOUNT_LINK = By.XPATH, p.LINK_ATTR.format('href', '/account')
