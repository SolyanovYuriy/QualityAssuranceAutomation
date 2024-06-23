from pages.base_page import BasePage
from selenium.webdriver.common.by import By

contactsMenuLocator =               "Контакты"
tensorBannerLocator =               "[class='sbisru-Contacts__logo-tensor " "mb-12'] img"


class Sbis(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_web_page_sbis_ru(self):
        """ Открыть веб-страницу sbis.ru
        """
        self.browser.get("https://sbis.ru/")

    def find_menu_contacts(self):
        """ Найти меню "Контакты"
        """
        return self.find((By.LINK_TEXT, contactsMenuLocator))

    def menu_contacts_is_displayed(self):
        """ Проверить присутствие меню "Контакты" на веб-странице
        """
        return self.find_menu_contacts().is_displayed()

    def click_menu_contacts(self):
        """ Клик по меню "Контакты"
        """
        self.find_menu_contacts().click()

    def find_banner_tensor(self):
        """ Найти баннер "Тензор"
        """
        return self.find((By.CSS_SELECTOR, tensorBannerLocator))

    def banner_tensor_is_displayed(self):
        """ Проверить присутствие баннерa "Тензор" на веб-странице
        """
        return self.find_banner_tensor().is_displayed()

    def click_banner_tensor(self):
        """ Клик по баннеру "Тензор"
        """
        self.find_banner_tensor().click()
