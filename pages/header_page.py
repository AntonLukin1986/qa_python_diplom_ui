'''Page object общего для всех страниц хедера.'''
import allure

from locators import header_page_locators as L
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Клик по ссылке хедера')
    def header_link_click(self, name):
        self.click_element(self.format_locator(L.HEADER_LINK, name))

    @allure.step('Клик по ссылке «Лента Заказов»')
    def orders_list_link_click(self):
        self.header_link_click('Лента Заказов')

    @allure.step('Клик по ссылке «Личный кабинет»')
    def personal_account_link_click(self):
        self.click_element(L.PERSONAL_ACCOUNT_LINK)
