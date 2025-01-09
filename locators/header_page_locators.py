'''Локаторы главной страницы.'''
from selenium.webdriver.common.by import By

from . import patterns as p

CONSTRUCTOR_LINK = By.XPATH, p.PARAG_TXT.format('Конструктор') + p.UP.format('a')
ORDERS_LIST_LINK = By.XPATH, p.PARAG_TXT.format('Лента Заказов') + p.UP.format('a')
LOGO_LINK = By.XPATH, p.LINK_ATTR.format('href', '/')
PERSONAL_ACCOUNT_LINK = By.XPATH, p.LINK_ATTR.format('href', '/account')
