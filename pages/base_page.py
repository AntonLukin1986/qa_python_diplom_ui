'''Page object с универсальными методами страниц.'''
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        '''Получение заданного элемента страницы.'''
        self.wait_for(e_c.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        '''Клик по элементу.'''
        from selenium.common.exceptions import ElementClickInterceptedException
        try:
            self.get_element(locator).click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click()', self.get_element(locator))

    def fill_in(self, locator, *value):
        '''Заполнение поля ввода.'''
        self.get_element(locator).send_keys(value)

    def wait_for(self, event, until=''):
        '''Приостановка работы драйвера.'''
        getattr(WebDriverWait(self.driver, timeout=5), f'until{until}')(event)
