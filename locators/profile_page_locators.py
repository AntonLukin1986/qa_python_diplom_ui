'''Локаторы страницы профиля пользователя.'''
from selenium.webdriver.common.by import By

from . import patterns as p


EXIT_LINK = By.XPATH, p.BUTTON_TXT.format('Выход')
ORDER_HISTORY_LINK = By.XPATH, p.LINK_TXT.format('История заказов')
ORDERS_DIV = By.XPATH, p.DIV_CONTAINS_CLS.format('OrderHistory')
MESSAGE = By.XPATH, p.PARAG_TXT.format(
    'В этом разделе вы можете изменить свои персональные данные'
)
