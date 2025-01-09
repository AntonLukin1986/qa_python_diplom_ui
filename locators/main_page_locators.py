'''Локаторы главной страницы.'''
from selenium.webdriver.common.by import By

from . import patterns as p

BASKET = By.XPATH, p.UL_CONTAINS_CLS.format('BurgerConstructor_basket')
CONSTRUCTOR_TITLE = By.XPATH, p.HEADER1_TXT.format('Соберите бургер')
ENTER_ACCOUNT_BTN = By.XPATH, p.BUTTON_TXT.format('Войти в аккаунт')
INGREDIENT_DETAILS_TITLE = By.XPATH, p.HEADER2_TXT.format('Детали ингредиента')
INGREDIENT_X_BTN = By.XPATH, p.HEADER2_TXT.format('Детали ингредиента') + p.UP.format('div/button')
INGREDIENTS_COUNTERS = By.XPATH, p.P_CONTAINS_CLS.format('counter')
INGREDIENTS_LINKS = By.XPATH, p.A_CONTAINS_CLS.format('BurgerIngredient')
ORDER_DETAILS_TXT = By.XPATH, p.PARAG_TXT.format('Cостав')
ORDER_ID = By.XPATH, p.PARAG_TXT.format('идентификатор заказа') + p.UP.format('div/h2')
ORDER_ID_X_BTN = By.XPATH, p.PARAG_TXT.format('идентификатор заказа') + '/../../button'
ORDER_IN_LIST = By.XPATH, p.PARAG_TXT
ORDER_IN_PROGRESS = By.XPATH, p.UL_CONTAINS_CLS.format('orderListReady') + p.LI_TXT
ORDER_LINK = By.XPATH, p.FIRST_LI_ITEM.format('OrderHistory_listItem') + '/a'
ORDERS_COUNTER = By.XPATH, p.PARAG_TXT + '/../p[2]'
ORDERS_LIST_TITLE = By.XPATH, p.HEADER1_TXT.format('Лента заказов')
PLACE_ORDER_BTN = By.XPATH, p.BUTTON_TXT.format('Оформить заказ')
