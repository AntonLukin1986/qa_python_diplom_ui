'''Тесты страницы восстановления паролей.'''
import allure

from data import ACTIVE, EMAIL


class TestRestorePage:

    @allure.title(
        'Успешный переход на страницу восстановления пароля по ссылке '
        '«Восстановить пароль»'
    )
    def test_restore_pass_link_click_open_restore_page(
        self, login_page, main_page, restore_page
    ):
        restore_page.open_restore_page(login_page, main_page)
        assert restore_page.get_restore_pass_title().is_displayed()

    @allure.title('Успешный ввод email и клик по кнопке «Восстановить»')
    def test_input_email_and_restore_btn_click_success(
        self, login_page, main_page, restore_page
    ):
        restore_page.confirmation(login_page, main_page, EMAIL)
        assert restore_page.get_enter_code_label().is_displayed()

    @allure.title('Клик по кнопке «глаз» поля пароль делает поле активным')
    def test_eye_btn_click_password_field_is_active(
        self, login_page, main_page, restore_page
    ):
        restore_page.confirmation(login_page, main_page, EMAIL)
        frame = restore_page.get_password_frame()
        class_before = frame.get_attribute(name='class')
        restore_page.eye_btn_click()
        class_after = frame.get_attribute(name='class')
        assert ACTIVE not in class_before and ACTIVE in class_after
