'''Page object общего для всех страниц хедера.'''
import allure

from locators import header_page_locators as L
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Клик по ссылке «Конструктор»')
    def constructor_link_click(self):
        self.click_element(L.CONSTRUCTOR_LINK)

    @allure.step('Клик по ссылке «Лента Заказов»')
    def orders_list_link_click(self):
        self.click_element(L.ORDERS_LIST_LINK)

    @allure.step('Клик по логотипу «Stellar burgers»')
    def logo_click(self):
        self.click_element(L.LOGO_LINK)

    @allure.step('Клик по ссылке «Личный кабинет»')
    def personal_account_link_click(self):
        self.click_element(L.PERSONAL_ACCOUNT_LINK)
