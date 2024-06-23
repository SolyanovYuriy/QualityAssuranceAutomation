from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

contactsMenuLocator =               "Контакты"
tensorBannerLocator =               "[class='sbisru-Contacts__logo-tensor " "mb-12'] img"
establishedRegionLocator =          ".sbis_ru-Region-Chooser.ml-16 .sbis_ru-Region-Chooser__text.sbis_ru-link"
partnersEstablishedRegionLocator =  "[class='sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32']"
newRegionLocator =                  "span[title='Камчатский край']"


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

    def find_established_region(self):
        """ Найти установившийся регион
        """
        return self.find((By.CSS_SELECTOR, establishedRegionLocator))

    def get_text_established_region(self):
        """ Возвращает название установившегося региона на веб-странице
        """
        return self.find_established_region().text

    def established_region_is_displayed(self):
        """ Проверить присутствие установившегося региона на веб-странице
        """
        return self.find_established_region().is_displayed()

    def find_partners_established_region(self):
        """ Найти список партнеров для установившегося региона
        """
        return self.finds((By.CSS_SELECTOR, partnersEstablishedRegionLocator))

    def get_partners(self, partners) -> set:
        """ Возвращает список партнеров текущего установленного региона
        :param partners: список партнеров установленного региона
        """
        lst_partners = []
        for partner in partners:
            contact = partner.text
            lst_partners.append(contact)
            assert partner.is_displayed()
        partners_region = set(lst_partners)
        return partners_region

    def click_established_region(self):
        """ Клик по установившемуся региону
        """
        self.find_established_region().click()

    def find_new_region(self):
        """ Найти новый регион "Камчатский край"
        """
        # return self.find_until((By.CSS_SELECTOR, newRegionLocator))
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, newRegionLocator)))

    def click_new_region(self):
        """ Клик по выбранному новому региону
        """
        self.find_new_region().click()
