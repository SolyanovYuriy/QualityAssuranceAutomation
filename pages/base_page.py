# Класс хранит общие методы для других страниц (классов)


class BasePage:
    def __init__(self, browser):
        self.browser = browser
