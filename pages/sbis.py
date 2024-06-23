from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import glob

contactsMenuLocator =               "Контакты"
tensorBannerLocator =               "[class='sbisru-Contacts__logo-tensor " "mb-12'] img"
establishedRegionLocator =          ".sbis_ru-Region-Chooser.ml-16 .sbis_ru-Region-Chooser__text.sbis_ru-link"
partnersEstablishedRegionLocator =  "[class='sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32']"
newRegionLocator =                  "span[title='Камчатский край']"
downloadLocalVersionLocator =       "//*[text()='Скачать локальные версии']"
tabSbisPlaginLocator =              "//*[text()='СБИС Плагин']"
tabOsWindowsLocator =               "//*[text()='Windows']"
downloadWebInstallerLocator =       "[href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']"


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

    def find_download_local_versions(self):
        """ Найти ссылку "Скачать локальные версии"
        """
        return self.find((By.XPATH, downloadLocalVersionLocator))

    def download_local_versions_is_displayed(self):
        """ Проверить присутствие ссылки для скачивания локальных версий
        """
        return self.find_download_local_versions().is_displayed()

    def click_download_local_versions(self):
        """ Клик по ссылке "Скачать локальные версии"
        """
        self.find_download_local_versions().click()

    def scroll_download_local_versions(self):
        """ Скролл страницы до элемента "Скачать локальные версии"
        """
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.find_download_local_versions())

    def find_tab_sbis_plagin(self):
        """ Найти вкладку "СБИС Плагин"
        """
        return self.find((By.XPATH, tabSbisPlaginLocator))

    def click_tab_sbis_plagin(self):
        """ Клик по вкладке "СБИС Плагин"
        """
        self.find_tab_sbis_plagin().click()

    def find_tab_os_windows(self):
        """ Найти вкладку "Windows"
        """
        return self.find((By.XPATH, tabOsWindowsLocator))

    def click_tab_os_windows(self):
        """ Клик по вкладке "Windows"
        """
        self.find_tab_os_windows().click()

    def find_web_installer(self):
        """ Найти элемент "Скачать" для скачивания веб-установщика СБИС плагина
        """
        return self.find((By.CSS_SELECTOR, downloadWebInstallerLocator))

    def click_web_installer(self):
        """ Клик по элементу "Скачать" для скачивания веб-установщика СБИС плагина
        """
        self.find_web_installer().click()

    def get_list_of_exe_files_in_current_directory_with_path(self) -> list:
        """ Возвращает список файлов (с абсолютным путем) с расширением *.ехе,
            находящиеся в текущей директории
        """
        return glob.glob(f"{os.getcwd()}\*.exe")

    def get_latest_exe_file_in_current_directory_with_path(self) -> str:
        """ Возвращает недавний файл (с абсолютным путем) с расширением *.ехе из списка файлов,
            находящиеся в текущей директории
        """
        return max(self.get_list_of_exe_files_in_current_directory_with_path(), key=os.path.getctime)

    def get_size_file_from_website(self, size_file_from_website=None) -> float:
        """ Возвращает размер файл с расширением *.ехе, указанный на сайте
        """
        for _ in self.find_web_installer().text.split():
            if "." in _:
                size_file_from_website = float(_)
                break
        return size_file_from_website

    def get_size_file_from_current_directory(self) -> float:
        """ Возвращает размер файл с расширением *.ехе из дирктории, в которую был скачан файл
        """
        latest_file = self.get_latest_exe_file_in_current_directory_with_path().split('\\')[-1]
        return round(os.path.getsize(f"{os.getcwd()}\\{latest_file}") / 1048576, 2)
