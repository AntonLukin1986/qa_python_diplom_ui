'''Тесты страницы восстановления паролей.'''
import allure

from data import Restore


class TestRestorePage:

    @allure.title(
        'Успешный переход на страницу восстановления пароля по ссылке '
        '«Восстановить пароль»'
    )
    def test_restore_pass_link_open_restore_page(
        self, main_page, login_page, restore_page
    ):
        restore_page.open_it(main_page, login_page)
        assert restore_page.get_restore_pass_title() == Restore.TITLE

    @allure.title('Успешный ввод email и клик по кнопке «Восстановить»')
    def test_input_email_and_restore_btn_click_success(
        self, main_page, login_page, restore_page
    ):
        restore_page.confirmation(main_page, login_page, Restore.EMAIL)
        assert restore_page.get_enter_code_label() == Restore.ENTER_CODE

    @allure.title('Клик по кнопке «глаз» поля пароль делает поле активным')
    def test_eye_btn_click_password_field_is_active(
        self, main_page, login_page, restore_page
    ):
        restore_page.confirmation(main_page, login_page, Restore.EMAIL)
        field_before = restore_page.get_class_input_pass()
        restore_page.eye_btn_click()
        field_after = restore_page.get_class_input_pass()
        assert (
            Restore.ACTIVE not in field_before and
            Restore.ACTIVE in field_after
        )
