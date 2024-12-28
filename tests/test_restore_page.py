'''Тесты страницы восстановления паролей.'''
import allure

from data import Restore


class TestRestorePage:

    @allure.title(
        'Успешный переход на страницу восстановления пароля по ссылке '
        '«Восстановить пароль»'
    )
    def test_restore_pass_link_click_open_restore_page(
        self, main_page, login_page, restore_page
    ):
        restore_page.open_it(main_page, login_page)
        assert restore_page.get_restore_pass_title().is_displayed()

    @allure.title('Успешный ввод email и клик по кнопке «Восстановить»')
    def test_input_email_and_restore_btn_click_success(
        self, main_page, login_page, restore_page
    ):
        restore_page.confirmation(main_page, login_page, Restore.EMAIL)
        assert restore_page.get_enter_code_label().is_displayed()

    @allure.title('Клик по кнопке «глаз» поля пароль делает поле активным')
    def test_eye_btn_click_password_field_is_active(
        self, main_page, login_page, restore_page
    ):
        restore_page.confirmation(main_page, login_page, Restore.EMAIL)
        class_before = restore_page.get_password_frame().get_attribute(
            name='class'
        )
        restore_page.eye_btn_click()
        class_after = restore_page.get_password_frame().get_attribute(
            name='class'
        )
        expected = Restore.ACTIVE
        assert expected not in class_before and expected in class_after
