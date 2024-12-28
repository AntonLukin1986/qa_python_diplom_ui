'''Тесты страницы профиля пользователя.'''
import allure


class TestProfilePage:

    @allure.title('Успешный переход в профиль по ссылке «Личный кабинет»')
    def test_personal_account_link_click_open_profile_page(
        self, test_user, main_page, login_page, profile_page
    ):
        profile_page.open_it(test_user, main_page, login_page)
        assert profile_page.get_message().is_displayed()

    @allure.title('Успешный переход по ссылке «История заказов»')
    def test_orders_history_link_click_open_orders_section(
        self, test_user, main_page, login_page, profile_page
    ):
        profile_page.open_it(test_user, main_page, login_page)
        profile_page.orders_history_link_click()
        assert profile_page.get_orders_div()                                   # ???????????????????????????????

    @allure.title('Успешный выход из аккаунта по ссылке «Выход»')
    def test_exit_link_click_user_logout(
        self, test_user, main_page, login_page, profile_page
    ):
        profile_page.open_it(test_user, main_page, login_page)
        profile_page.exit_link_click()
        assert login_page.get_entrance_title().is_displayed()
