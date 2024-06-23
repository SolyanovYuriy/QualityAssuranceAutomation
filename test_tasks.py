from pages.sbis import Sbis
from pages.tensor import Tensor


def test_first_task_from_get_test_tasks(browser):
        sbis_ru = Sbis(browser)
        sbis_ru.open_web_page_sbis_ru()
        assert sbis_ru.menu_contacts_is_displayed()
        sbis_ru.click_menu_contacts()

        sbis_ru.find_menu_contacts()
        assert sbis_ru.banner_tensor_is_displayed()
        sbis_ru.click_banner_tensor()

        sbis_ru.go_to_other_tab()
        assert browser.current_url == "https://tensor.ru/"
        tensor_ru = Tensor(browser)

        tensor_ru.find_block_power_in_people()
        assert tensor_ru.block_power_in_people_is_displayed(), "Отсутствует блок 'Сила в людях'"

        tensor_ru.find_link_moredetailed_in_block_power_in_people()
        tensor_ru.scroll_link_moredetailed_in_block_power_in_people()
        tensor_ru.click_link_in_block_power_in_people()
        assert browser.current_url == "https://tensor.ru/about", "Сайт https://tensor.ru/about не открывается"

        tensor_ru.find_chapter_working()
        tensor_ru.scroll_chapter_working()
        assert tensor_ru.chapter_working_is_displayed()
        assert tensor_ru.get_height_foto_development_sbis() == tensor_ru.get_height_foto_go_services() \
               == tensor_ru.get_height_foto_create_infrastructure() \
               == tensor_ru.get_height_foto_accompany_clients(), "Фотографии имеют разные высоты"
        assert tensor_ru.get_width_foto_development_sbis() == tensor_ru.get_width_foto_go_services() \
               == tensor_ru.get_width_foto_create_infrastructure() \
               == tensor_ru.get_width_foto_accompany_clients(), "Фотографии имеют разные ширины"
