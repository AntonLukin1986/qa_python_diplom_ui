'''Page object страницы авторизации.'''
import allure

from locators import login_page_locators as L
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Клик по ссылке «Восстановить пароль»')
    def restore_pass_link_click(self):
        self.click_element(L.RESTORE_PASS_LINK)
