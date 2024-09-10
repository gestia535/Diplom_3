from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дождаться видимости элемента')
    def wait_until_element_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Найти элемент с ожиданием')
    def find_element_with_wait(self, locator):
        self.wait_until_element_visibility(locator)
        return self.driver.find_element(*locator)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Ожидание url')
    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 20).until((expected_conditions.url_to_be(url)))

    @allure.step('Дождаться кликабельности элемента')
    def wait_until_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Переместиться до элемента и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Ввести значение в поле ввода')
    def set_text_to_elm(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        self.wait_until_element_visibility(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.find_element_with_wait(locator).is_displayed()

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_element, target_element):
        script = """
        function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
            var dataTransfer = new DataTransfer();
            var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragStartEvent);

            var dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            destinationNode.dispatchEvent(dropEvent);

            var dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragEndEvent);
        }
        simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """
        source_element = self.driver.find_element(*source_element)
        target_element = self.driver.find_element(*target_element)
        self.driver.execute_script(script, source_element, target_element)

    @allure.step('Подождать, пока элемент закроется')
    def wait_for_closing_of_element(self, locator):
        WebDriverWait(self.driver, 15).until_not(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Дождаться появления текста в элементе')
    def wait_for_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step("Нахождение нескольких элементов")
    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located(locator))

    @allure.step("Проверка текущего url")
    def get_current_url(self):
        return self.driver.current_url
