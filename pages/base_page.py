# Класс хранит общие методы для других страниц (классов)


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        """ Найти html-элемент на веб-странице
        :param args: turple (метод поиска, значение)
        """
        return self.browser.find_element(*args)

    def go_to_other_tab(self):
        """ Сделать активной другую открывшуюся вкладку
        """
        return self.browser.switch_to.window(self.browser.window_handles[-1])

    def find_foto(self, args):
        """ Найти html-элемент на веб-странице
        :param args: turple (метод поиска, значение)
        """
        return self.browser.find_element(*args)
