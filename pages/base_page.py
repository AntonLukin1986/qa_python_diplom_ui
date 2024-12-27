'''Page object с универсальными методами страниц.'''
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, event):
        '''Приостановка работы драйвера.'''
        WebDriverWait(self.driver, timeout=5).until(event)

    def get_element(self, locator):
        '''Получение заданного элемента страницы.'''
        self.wait_for(e_c.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_element_text(self, locator):
        '''Получение текста заданного элемента страницы.'''
        return self.get_element(locator).text

    def click_element(self, locator):
        '''Клик по элементу.'''
        self.get_element(locator).click()

    def fill_in(self, locator, *value):
        '''Заполнение поля ввода.'''
        self.get_element(locator).send_keys(value)
