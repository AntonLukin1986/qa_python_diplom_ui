'''Page object с универсальными методами страниц.'''
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait

from config import FIREFOX_JS
from data import BLOCKER


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        '''Получение заданного элемента.'''
        self.wait_for(e_c.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_elements_kit(self, locator):
        '''Получение заданного набора элементов.'''
        self.wait_for(e_c.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        '''Клик по элементу.'''
        self.wait_for(e_c.element_to_be_clickable(locator))
        while True:
            try:
                self.get_element(locator).click()
            except ElementClickInterceptedException as error:
                if BLOCKER in str(error):  # ожидаемо для Firefox
                    pass  # блокировщик отключается сам
                else:
                    raise ElementClickInterceptedException(error)
            else:
                break

    def fill_in(self, locator, *values):
        '''Заполнение поля ввода.'''
        self.get_element(locator).send_keys(values)

    def scroll_to(self, element):
        '''Прокрутка экрана до элемента.'''
        self.driver.execute_script('arguments[0].scrollIntoView()', element)
        self.wait_for(e_c.visibility_of(element))

    def wait_for(self, event, timeout=10, until=''):
        '''Приостановка работы драйвера: until или until_not'''
        getattr(WebDriverWait(self.driver, timeout), f'until{until}')(event)

    def drag_to(self, element, target):
        '''Перемещение элемента к другому элементу.'''
        if self.driver.name == 'firefox':
            self.driver.execute_script(FIREFOX_JS, element, target)
        else:
            ActionChains(self.driver).drag_and_drop(element, target).perform()
