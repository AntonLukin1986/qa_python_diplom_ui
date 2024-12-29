'''Page object с универсальными методами страниц.'''
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        '''Получение заданного элемента.'''
        self.wait_for(e_c.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_elements_kit(self, locator):
        '''Получение заданного набора элементов.'''
        self.wait_for(e_c.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        '''Клик по элементу.'''
        # from selenium.common.exceptions import ElementClickInterceptedException
        # try:
        #     self.get_element(locator).click()
        # except ElementClickInterceptedException:
        #     self.driver.execute_script('arguments[0].click()', self.get_element(locator))
        self.get_element(locator).click()

    def fill_in(self, locator, *value):
        '''Заполнение поля ввода.'''
        self.get_element(locator).send_keys(value)

    def scroll_to(self, element):
        '''Прокрутка экрана до элемента.'''
        self.driver.execute_script('arguments[0].scrollIntoView()', element)
        self.wait_for(e_c.visibility_of(element))

    def wait_for(self, event, timeout=5, until=''):
        '''Приостановка работы драйвера: until или until_not'''
        getattr(WebDriverWait(self.driver, timeout), f'until{until}')(event)

    def drag_to(self, element, target):
        '''Перемещение элемента к другому элементу.'''
        ActionChains(self.driver).drag_and_drop(element, target).perform()
