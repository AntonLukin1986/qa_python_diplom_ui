'''Тесты главной страницы.'''
import allure
import pytest


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
        confirmation = main_page.make_order(login_page, test_user)
        assert confirmation.is_displayed()

    @allure.title('Клик по заказу в ленте открывает окно с деталями')
    def test_order_click_open_details(self, main_page):
        main_page.orders_list_link_click()
        main_page.order_link_click()
        assert main_page.get_order_details_text().is_displayed()

    @allure.title('Заказы из раздела «История заказов» отображаются в ленте')
    def test_order_from_history_appears_in_orders_list(
        self, main_page, login_page, profile_page, test_user
    ):
        main_page.make_order(login_page, test_user)
        main_page.order_number_X_click()
        main_page.personal_account_link_click()
        profile_page.orders_history_link_click()
        number = profile_page.get_order_number_element().text
        main_page.orders_list_link_click()
        assert main_page.get_order_from_orders_list(number).is_displayed()

    @pytest.mark.parametrize(
        'name',
        [pytest.param('Выполнено за все время:', id='total'),
         pytest.param('Выполнено за сегодня:', id='today')]
    )
    @allure.title('Увеличение счётчиков заказов «за всё время» и «за сегодня»')
    def test_increasing_orders_counters_all_time_and_today(
        self, main_page, login_page, test_user, name
    ):
        main_page.orders_list_link_click()
        before = int(main_page.get_orders_counter(name).text)
        main_page.logo_click()
        main_page.make_order(login_page, test_user)
        main_page.order_number_X_click()
        main_page.orders_list_link_click()
        after = int(main_page.get_orders_counter(name).text)
        assert before + 1 == after

    @allure.title('Номер оформленного заказа появляется в разделе «В работе»')
    def test_new_order_number_appears_in_progress_section(
        self, main_page, login_page, test_user
    ):
        number = main_page.make_order(login_page, test_user).text
        main_page.order_number_X_click()
        main_page.orders_list_link_click()
        assert main_page.get_order_number_in_progress_section(number).is_displayed()
