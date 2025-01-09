'''Page object страницы восстановления пароля.'''
import allure

from locators import restore_page_locators as L
from pages.base_page import BasePage


class RestorePage(BasePage):

    @allure.step('Открытие страницы «Восстановление пароля»')
    def open_restore_page(self, login_page, main_page):
        main_page.enter_account_btn_click()
        login_page.restore_pass_link_click()

    @allure.step('Переход в раздел сохранения нового пароля')
    def confirmation(self, login_page, main_page, email):
        self.open_restore_page(login_page, main_page)
        self.input_email(email)
        self.restore_btn_click()

    @allure.step('Получение заголовка формы «Восстановление пароля»')
    def get_restore_pass_title(self):
        return self.get_element(L.RESTORE_PASS_TITLE)

    @allure.step('Получение плейсхолдера поля «Код из письма»')
    def get_enter_code_label(self):
        return self.get_element(L.ENTER_CODE_LABEL)

    @allure.step('Получение рамки поля для ввода пароля')
    def get_password_frame(self):
        return self.get_element(L.PASSWORD_FRAME)

    @allure.step('Клик по кнопке «Восстановить»')
    def restore_btn_click(self):
        self.click_element(L.RESTORE_BTN)

    @allure.step('Клик по кнопке «Глаз»')
    def eye_btn_click(self):
        self.click_element(L.EYE_BTN)

    @allure.step('Заполнение поля «email»')
    def input_email(self, email):
        self.fill_in(L.EMAIL_INPUT, email)
