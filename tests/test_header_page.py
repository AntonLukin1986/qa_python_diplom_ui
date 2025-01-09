'''Тесты общего для страниц хедера.'''
import allure
import pytest


class TestHeaderPage:

    @pytest.mark.parametrize(
        'link_name, title_name',
        [pytest.param('Конструктор', 'Соберите бургер', id='constructor'),
         pytest.param('Лента Заказов', 'Лента заказов', id='orders_list')]
    )
    @allure.title('Успешный переход по ссылке в хедере')
    def test_header_link_click_switching_success(
        self, header_page, main_page, link_name, title_name
    ):
        header_page.personal_account_link_click()
        header_page.header_link_click(link_name)
        assert main_page.get_section_title(title_name).is_displayed()
