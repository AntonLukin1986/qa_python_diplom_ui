'''Page object страницы профиля пользователя.'''
import allure

from locators import profile_page_locators as L
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Открытие профиля пользователя')
    def open_it(self, test_user, main_page, login_page):
        login_page.login(main_page, **test_user)
        main_page.personal_account_link_click()

    @allure.step('Получение информационного сообщения')
    def get_message(self):
        return self.get_element(L.MESSAGE)

    @allure.step('Получение блока с заказами')
    def get_orders_div(self):
        return self.get_element(L.ORDERS_DIV)

    @allure.step('Клик по ссылке «История заказов»')
    def orders_history_link_click(self):
        self.click_element(L.ORDER_HISTORY_LINK)

    @allure.step('Клик по ссылке «Выход»')
    def exit_link_click(self):
        self.click_element(L.EXIT_LINK)
