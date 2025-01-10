'''Page object страницы профиля пользователя.'''
import allure

from locators import profile_page_locators as L
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Клик по ссылке «История заказов»')
    def orders_history_link_click(self):
        self.click_element(L.ORDERS_HISTORY_LINK)

    @allure.step('Клик по ссылке «Выход»')
    def exit_link_click(self):
        self.click_element(L.EXIT_LINK)

    @allure.step('Получение информационного сообщения')
    def get_message(self):
        return self.get_element(L.MESSAGE)

    @allure.step('Получение номера заказа из истории')
    def get_order_number(self):
        return self.get_element(L.ORDER_NUMBER)

    @allure.step('Открытие профиля пользователя')
    def open_profile_page(self, header_page, login_page, test_user):
        header_page.personal_account_link_click()
        login_page.login(**test_user)
        header_page.personal_account_link_click()
