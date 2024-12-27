'''Page object главной страницы.'''
import allure

from locators import main_page_locators as L
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по кнопке «Войти в аккаунт»')
    def enter_account_btn_click(self):
        self.click_element(L.ENTER_ACCOUN_BTN)
