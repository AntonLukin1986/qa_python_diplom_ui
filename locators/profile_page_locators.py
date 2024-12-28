'''Локаторы страницы профиля пользователя.'''
from selenium.webdriver.common.by import By

from .patterns import BUTTON_TXT, DIV_CONTAINS_CLS, LINK_TXT, PARAGRAPH_TXT


EXIT_LINK = By.XPATH, BUTTON_TXT.format('Выход')
ORDER_HISTORY_LINK = By.XPATH, LINK_TXT.format('История заказов')
ORDERS_DIV = By.XPATH, DIV_CONTAINS_CLS.format('OrderHistory')
MESSAGE = By.XPATH, PARAGRAPH_TXT.format(
    'В этом разделе вы можете изменить свои персональные данные'
)
