'''Page object главной страницы.'''
import random

import allure
from selenium.webdriver.support.expected_conditions import (
    text_to_be_present_in_element as text_in_element,
    invisibility_of_element_located as element_invisible
)

from data import SLICERS, STUB
from helpers import format_locator
from locators import main_page_locators as L
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по кнопке «Войти в аккаунт»')
    def enter_account_btn_click(self):
        self.click_element(L.ENTER_ACCOUNT_BTN)

    @allure.step('Клик по ингредиенту')
    def ingredient_click(self, ingredient):
        self.scroll_to(ingredient)
        ingredient.click()

    @allure.step('Клик по X окна деталей ингредиента')
    def ingredient_details_X_click(self):
        self.click_element(L.INGREDIENT_X_BTN)
        self.wait_for(element_invisible(L.INGREDIENT_X_BTN))

    @allure.step('Клик по кнопке «Оформить заказ»')
    def place_order_btn_click(self):
        self.click_element(L.PLACE_ORDER_BTN)

    @allure.step('Клик по заказу в ленте')
    def order_link_click(self):
        self.click_element(L.ORDER_LINK)

    @allure.step('Клик по X окна с номером заказа')
    def order_number_X_click(self):
        self.click_element(L.ORDER_ID_X_BTN)

    @allure.step('Получение ингредиента')
    def get_ingredient(self, slicer=slice(None)):
        return random.choice(
            self.get_elements_kit(L.INGREDIENTS_LINKS)[slicer]
        )

    @allure.step('Получение заголовка окна деталей ингредиента')
    def get_ingredient_details_title(self):
        return self.get_element(L.INGREDIENT_DETAILS_TITLE)

    @allure.step('Получение счётчика ингредиента')
    def get_counter(self, ingredient):
        index = self.get_elements_kit(L.INGREDIENTS_LINKS).index(ingredient)
        return self.get_elements_kit(L.INGREDIENTS_COUNTERS)[index]

    @allure.step('Получение корзины для заказа')
    def get_basket(self):
        return self.get_element(L.BASKET)

    @allure.step('Получение номера оформленного заказа')
    def get_order_number(self):
        self.wait_for(text_in_element(L.ORDER_ID, text_=STUB), until='_not')
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

    @allure.step('Получение заголовка раздела главной страницы')
    def get_section_title(self, name):
        return self.get_element(format_locator(L.SECTION_TITLE, name))

    @allure.step('Добавление ингредиента в корзину')
    def add_ingredient_to_basket(self, ingredient, basket):
        self.drag_to(ingredient, basket)

    @allure.step('Создание заказа и получение его номера')
    def make_order(self, header_page, login_page, test_user):
        header_page.personal_account_link_click()
        login_page.login(**test_user)
        basket = self.get_basket()
        for slicer in SLICERS:
            self.add_ingredient_to_basket(self.get_ingredient(slicer), basket)
        self.place_order_btn_click()
        order_number = self.get_order_number()
        self.order_number_X_click()
        return order_number
