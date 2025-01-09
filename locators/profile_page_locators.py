'''Локаторы страницы профиля пользователя.'''
from selenium.webdriver.common.by import By

from . import patterns as p

EXIT_LINK = By.XPATH, p.BUTTON_TXT.format('Выход')
MESSAGE = By.XPATH, p.PARAG_TXT.format(
    'В этом разделе вы можете изменить свои персональные данные'
)
ORDER_NUMBER = By.XPATH, p.FIRST_LI_ITEM.format('OrderHistory_listItem') + p.P_CONTAINS_CLS.format('digits')
ORDERS_HISTORY_LINK = By.XPATH, p.LINK_TXT.format('История заказов')
