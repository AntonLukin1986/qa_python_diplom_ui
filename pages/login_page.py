'''Page object страницы авторизации.'''
import allure

from locators import login_page_locators as L
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Клик по ссылке «Восстановить пароль»')
    def restore_pass_link_click(self):
        self.click_element(L.RESTORE_PASS_LINK)

    @allure.step('Клик по кнопке «Войти»')
    def enter_button_click(self):
        self.click_element(L.ENTER_BTN)

    @allure.step('Получение заголовка формы «Вход»')
    def get_entrance_title(self):
        return self.get_element(L.ENTRANCE_TITLE)

    @allure.step('Заполнение поля «email»')
    def input_email(self, email):
        self.fill_in(L.EMAIL_INPUT, email)

    @allure.step('Заполнение поля «пароль»')
    def input_password(self, password):
        self.fill_in(L.PASSWORD_INPUT, password)

    @allure.step('Авторизация пользователя')
    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.enter_button_click()
