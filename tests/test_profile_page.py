'''Тесты страницы профиля пользователя.'''
import allure

from config import ORDER_HISTORY_PAGE


class TestProfilePage:

    @allure.title('Успешный переход в профиль по ссылке «Личный кабинет»')
    def test_personal_account_link_click_open_profile_page(
        self, header_page, login_page, profile_page, test_user
    ):
        profile_page.open_profile_page(header_page, login_page, test_user)
        assert profile_page.get_message().is_displayed()

    @allure.title('Успешный переход по ссылке «История заказов»')
    def test_orders_history_link_click_open_orders_section(
        self, header_page, login_page, profile_page, test_user
    ):
        profile_page.open_profile_page(header_page, login_page, test_user)
        profile_page.orders_history_link_click()
        assert profile_page.driver.current_url == ORDER_HISTORY_PAGE

    @allure.title('Успешный выход из аккаунта по ссылке «Выход»')
    def test_exit_link_click_user_logout(
        self, header_page, login_page, profile_page, test_user
    ):
        profile_page.open_profile_page(header_page, login_page, test_user)
        profile_page.exit_link_click()
        assert login_page.get_entrance_title().is_displayed()
