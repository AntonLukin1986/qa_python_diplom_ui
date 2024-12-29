'''Локаторы главной страницы.'''
from selenium.webdriver.common.by import By

from . import patterns as p


BASKET = By.XPATH, p.UL_CONTAINS_CLS.format('BurgerConstructor_basket')
CLOSE_BTN = By.XPATH, p.HEADER2_TXT.format('Детали ингредиента') + p.UP.format('div/button')
CONSTRUCTOR_LINK = By.XPATH, p.PARAG_TXT.format('Конструктор') + p.UP.format('a')
CONSTRUCTOR_TITLE = By.XPATH, p.HEADER1_TXT.format('Соберите бургер')
ENTER_ACCOUNT_BTN = By.XPATH, p.BUTTON_TXT.format('Войти в аккаунт')
INGREDIENT_COUNTERS = By.XPATH, p.P_CONTAINS_CLS.format('counter')
INGREDIENT_DETAILS_TITLE = By.XPATH, p.HEADER2_TXT.format('Детали ингредиента')
INGREDIENT_LINKS = By.XPATH, p.A_CONTAINS_CLS.format('BurgerIngredient')
ORDER_ID = By.XPATH, p.PARAG_TXT.format('идентификатор заказа')
ORDERS_LIST_LINK = By.XPATH, p.PARAG_TXT.format('Лента Заказов') + p.UP.format('a')
ORDERS_LIST_TITLE = By.XPATH, p.HEADER1_TXT.format('Лента заказов')
PERSONAL_ACCOUNT_LINK = By.XPATH, p.LINK_ATTR.format('href', '/account')
PLACE_ORDER_BTN = By.XPATH, p.BUTTON_TXT.format('Оформить заказ')
