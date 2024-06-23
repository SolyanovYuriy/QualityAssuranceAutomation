from pages.base_page import BasePage
from selenium.webdriver.common.by import By


powerInPeopleBlockLocator =         '//*[text()="Сила в людях"]'
moredetailedLocator =               '//*[@class="tensor_ru-Index__block4-bg"]/descendant::a[text()="Подробнее"]'
workingChapterLocator =             '//*[text()="Работаем"]'
developmentSbisFotoLocator =        '[alt="Разрабатываем систему СБИС"]'
goServicestSbisFotoLocator =        '[alt="Продвигаем сервисы"]'
createInfrastructureFotoLocator =   '[alt="Создаем инфраструктуру"]'
accompanyClientsFotoLocator =       '[alt="Сопровождаем клиентов"]'


class Tensor(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def find_block_power_in_people(self):
        """ Найти по всей странице блок "Сила в людях"
        """
        return self.find((By.XPATH, powerInPeopleBlockLocator))

    def block_power_in_people_is_displayed(self):
        """ Проверить на веб-странице присутствие раздела "Контакты"
        """
        return self.find_block_power_in_people().is_displayed()

    def find_link_moredetailed_in_block_power_in_people(self):
        """ Найти ссылку "Подробнее" в блоке "Сила в людях"
        """
        return self.find((By.XPATH, moredetailedLocator))

    def scroll_link_moredetailed_in_block_power_in_people(self):
        """ Скролл страницы до элемента "Подробнее" в блоке "Сила в людях"
        """
        self.browser.execute_script("return arguments[0].scrollIntoView(true);",
                                    self.find_link_moredetailed_in_block_power_in_people())

    def click_link_in_block_power_in_people(self):
        """ Клик по ссылке "Подробнее" в блоке "Сила в людях"
        """
        self.find_link_moredetailed_in_block_power_in_people().click()

    def find_chapter_working(self):
        """ Найти раздел "Работаем"
        """
        return self.find((By.XPATH, workingChapterLocator))

    def scroll_chapter_working(self):
        """ Скролл страницы до раздела "Подробнее" "Работаем"
        """
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.find_chapter_working())

    def chapter_working_is_displayed(self):
        """ Проверить на веб-странице присутствие раздела "Работаем"
        """
        return self.find_chapter_working().is_displayed()

    def get_height_foto_development_sbis(self):
        """ Height фото "Разрабатываем систему СБИС"
        """
        return self.find_foto((By.CSS_SELECTOR, developmentSbisFotoLocator)).get_attribute("height")

    def get_width_foto_development_sbis(self):
        """ Width фото "Разрабатываем систему СБИС"
        """
        return self.find_foto((By.CSS_SELECTOR, developmentSbisFotoLocator)).get_attribute("width")

    def get_height_foto_go_services(self):
        """ Height фото "Продвигаем сервисы"
        """
        return self.find_foto((By.CSS_SELECTOR, goServicestSbisFotoLocator)).get_attribute("height")

    def get_width_foto_go_services(self):
        """ Width фото "Продвигаем сервисы"
        """
        return self.find_foto((By.CSS_SELECTOR, goServicestSbisFotoLocator)).get_attribute("width")

    def get_height_foto_create_infrastructure(self):
        """ Height фото "Создаем инфраструктуру"
        """
        return self.find_foto((By.CSS_SELECTOR, createInfrastructureFotoLocator)).get_attribute("height")

    def get_width_foto_create_infrastructure(self):
        """ Width фото "Создаем инфраструктуру"
        """
        return self.find_foto((By.CSS_SELECTOR, createInfrastructureFotoLocator)).get_attribute("width")

    def get_height_foto_accompany_clients(self):
        """ Height фото "Сопровождаем клиентову"
        """
        return self.find_foto((By.CSS_SELECTOR, accompanyClientsFotoLocator)).get_attribute("height")

    def get_width_foto_accompany_clients(self):
        """ Width фото "Сопровождаем клиентов"
        """
        return self.find_foto((By.CSS_SELECTOR, accompanyClientsFotoLocator)).get_attribute("width")
