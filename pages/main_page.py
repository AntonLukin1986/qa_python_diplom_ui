'''Page object главной страницы.'''
import random

import allure
from selenium.webdriver.support import expected_conditions as e_c

from data import ORDER_NUMBER_STUB, SLICERS
from helpers import format_locator
from locators import main_page_locators as L
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по логотипу «Stellar burgers»')
    def logo_click(self):
        self.click_element(L.LOGO_LINK)

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
        self.wait_and_click_element(L.CLOSE_BTN)

    @allure.step('Клик по кнопке «Оформить заказ»')
    def place_order_btn_click(self):
        self.click_element(L.PLACE_ORDER_BTN)

    @allure.step('Клик по заказу в ленте')
    def order_link_click(self):
        self.click_element(L.ORDER_LINK)

    @allure.step('Клик по X окна с номером заказа')
    def order_number_X_click(self):
        self.click_element(L.ORDER_ID_X_BTN)

    @allure.step('Получение заголовка конструктора')
    def get_constructor_title(self):
        return self.get_element(L.CONSTRUCTOR_TITLE)

    @allure.step('Получение заголовка ленты заказов')
    def get_orders_list_title(self):
        return self.get_element(L.ORDERS_LIST_TITLE)

    @allure.step('Получение заголовка окна деталей ингредиента')
    def get_ingredient_details_title(self):
        return self.get_element(L.INGREDIENT_DETAILS_TITLE)

    @allure.step('Получение ингредиента конкретного типа')
    def get_ingredient(self, slicer):
        return random.choice(self.get_elements_kit(L.INGREDIENTS_LINKS)[slicer])

    @allure.step('Получение счётчика ингредиента')
    def get_counter(self, ingredient):
        index = self.get_elements_kit(L.INGREDIENTS_LINKS).index(ingredient)
        return self.get_elements_kit(L.INGREDIENTS_COUNTERS)[index]

    @allure.step('Получение корзины заказа')
    def get_basket(self):
        return self.get_element(L.BASKET)

    @allure.step('Получение заголовка окна подтверждения заказа')
    def get_order_number_element(self):
        self.wait_for(
            e_c.text_to_be_present_in_element(L.ORDER_ID, text_=ORDER_NUMBER_STUB),
            until='_not'
        )
        return self.get_element(L.ORDER_ID)

    @allure.step('Получение текста в окне деталей заказа')
    def get_order_details_text(self):
        return self.get_element(L.ORDER_DETAILS_TXT)

    @allure.step('Получение заказа из ленты')
    def get_order_from_orders_list(self, number):
        return self.get_element(format_locator(L.ORDER_IN_LIST, number))

    @allure.step('Получение номера заказа в секции «В работе»')
    def get_order_number_in_progress_section(self, number):
        return self.get_element(format_locator(L.ORDER_IN_PROGRESS, number))

    @allure.step('Получение счётчика заказов «за всё время» или «за сегодня»')
    def get_orders_counter(self, name):
        return self.get_element(format_locator(L.ORDERS_COUNTER, name))

    @allure.step('Добавление ингредиента в корзину')
    def add_ingredient_to_basket(self, ingredient, basket):
        self.drag_to(ingredient, basket)

    @allure.step('Создание заказа и получение его номера')
    def make_order(self, login_page, test_user):
        login_page.login(self, **test_user)
        for slicer in SLICERS:
            self.add_ingredient_to_basket(
                self.get_ingredient(slicer), self.get_basket()
            )
        self.place_order_btn_click()
        return self.get_order_number_element()
