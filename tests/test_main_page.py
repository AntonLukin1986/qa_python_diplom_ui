'''Тесты главной страницы.'''
import random

import allure


class TestMainPage:

    @allure.title('Успешный переход по клику на «Конструктор»')
    def test_constructor_link_click_open_constructor(self, main_page):
        main_page.personal_account_link_click()
        main_page.constructor_link_click()
        assert main_page.get_constructor_title().is_displayed()

    @allure.title('Успешный переход по клику на «Лента заказов»')
    def test_orders_list_link_click_open_orders_list(self, main_page):
        main_page.personal_account_link_click()
        main_page.orders_list_link_click()
        assert main_page.get_orders_list_title().is_displayed()

    @allure.title('Клик по ингредиенту открывает окно с деталями')
    def test_ingredient_click_open_details(self, main_page):
        main_page.ingredient_click(main_page.get_ingredient())
        assert main_page.get_ingredient_details_title().is_displayed()

    @allure.title('Клик по крестику закрывает окно с деталями')
    def test_ingredient_details_X_click_close_details(self, main_page):
        main_page.ingredient_click(main_page.get_ingredient())
        main_page.ingredient_details_X_click()
        assert not main_page.get_ingredient_details_title().is_displayed()

    @allure.title('Добавление ингредиента в заказ увеличивает его счётчик')
    def test_add_ingredient_to_order_increase_counter(self, main_page):
        ingredient = main_page.get_ingredient()
        counter = main_page.get_counter(ingredient)
        counter_before = int(counter.text)
        main_page.add_ingredient_to_basket(ingredient, main_page.get_basket())
        counter_after = int(counter.text)
        assert counter_before + 1 == counter_after

    @allure.title('Успешное оформление заказа авторизованным пользователем')
    def test_authorized_user_make_order_success(
        self, main_page, login_page, test_user
    ):
        login_page.login(main_page, **test_user)
        ingredient = main_page.get_ingredient()
        main_page.add_ingredient_to_basket(ingredient, main_page.get_basket())
        main_page.place_order_btn_click()
        assert main_page.get_order_confirmation_title().is_displayed()
