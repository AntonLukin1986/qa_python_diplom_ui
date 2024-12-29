'''Page object главной страницы.'''
import random

import allure
from selenium.webdriver.support import expected_conditions as e_c

from locators import main_page_locators as L
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по кнопке «Войти в аккаунт»')
    def enter_account_btn_click(self):
        self.click_element(L.ENTER_ACCOUNT_BTN)

    @allure.step('Клик по ссылке «Личный кабинет»')
    def personal_account_link_click(self):
        self.click_element(L.PERSONAL_ACCOUNT_LINK)

    @allure.step('Клик по ссылке «Конструктор»')
    def constructor_link_click(self):
        self.click_element(L.CONSTRUCTOR_LINK)

    @allure.step('Клик по ссылке «Лента Заказов»')
    def orders_list_link_click(self):
        self.click_element(L.ORDERS_LIST_LINK)

    @allure.step('Клик по ингредиенту')
    def ingredient_click(self, ingredient):
        self.scroll_to(ingredient)
        ingredient.click()

    @allure.step('Клик по крестику окна деталей ингредиента')
    def ingredient_details_X_click(self):
        self.click_element(L.CLOSE_BTN)
        self.wait_for(e_c.element_to_be_clickable(L.CLOSE_BTN), until='_not')

    @allure.step('Клик по кнопке «Оформить заказ»')
    def place_order_btn_click(self):
        self.click_element(L.PLACE_ORDER_BTN)

    @allure.step('Получение заголовка конструктора')
    def get_constructor_title(self):
        return self.get_element(L.CONSTRUCTOR_TITLE)

    @allure.step('Получение заголовка ленты заказов')
    def get_orders_list_title(self):
        return self.get_element(L.ORDERS_LIST_TITLE)

    @allure.step('Получение заголовка окна деталей ингредиента')
    def get_ingredient_details_title(self):
        return self.get_element(L.INGREDIENT_DETAILS_TITLE)

    @allure.step('Получение ингредиента')
    def get_ingredient(self):
        return random.choice(self.get_elements_kit(L.INGREDIENT_LINKS))

    @allure.step('Получение счётчика ингредиента')
    def get_counter(self, ingredient):
        index = self.get_elements_kit(L.INGREDIENT_LINKS).index(ingredient)
        return self.get_elements_kit(L.INGREDIENT_COUNTERS)[index]

    @allure.step('Получение корзины заказа')
    def get_basket(self):
        return self.get_element(L.BASKET)

    @allure.step('Получение заголовка окна подтверждения заказа')
    def get_order_confirmation_title(self):
        return self.get_element(L.ORDER_ID)

    @allure.step('Добавление ингредиента в корзину')
    def add_ingredient_to_basket(self, ingredient, basket):
        self.drag_to(ingredient, basket)
