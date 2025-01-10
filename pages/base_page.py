'''Page object с универсальными методами страниц.'''
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait

from config import FIREFOX_JS


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, entity):
        '''Получение заданного элемента.'''
        if isinstance(entity, WebElement):
            return entity
        self.wait_for(e_c.presence_of_element_located(entity))
        return self.driver.find_element(*entity)

    def get_elements_kit(self, locator):
        '''Получение заданного набора элементов.'''
        self.wait_for(e_c.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, entity: tuple | WebElement):
        '''Клик по элементу.'''
        element = self.get_element(entity)
        self.wait_for(e_c.element_to_be_clickable(element))
        if self.driver.name == 'firefox':
            self.click_element_firefox(element)
        else:
            element.click()

    def click_element_firefox(self, element):
        '''Обход учебного блокировщика в тестах на Firefox.'''
        while True:
            try:
                element.click()
            except ElementClickInterceptedException as error:
                if 'Modal_modal_overlay__x2ZCr' not in str(error):
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

    def format_locator(self, locator, value):
        '''Форматирование локатора элемента.'''
        method, pattern = locator
        return method, pattern.format(value)
