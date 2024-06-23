from pages.sbis import Sbis
from pages.tensor import Tensor
import time


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
    assert tensor_ru.get_height_foto_development_sbis() == tensor_ru.get_height_foto_go_services()\
           == tensor_ru.get_height_foto_create_infrastructure() \
           == tensor_ru.get_height_foto_accompany_clients(), "Фотографии имеют разные высоты"
    assert tensor_ru.get_width_foto_development_sbis() == tensor_ru.get_width_foto_go_services() \
           == tensor_ru.get_width_foto_create_infrastructure()\
           == tensor_ru.get_width_foto_accompany_clients(), "Фотографии имеют разные ширины"


def test_second_task_from_get_test_tasks(browser):
    sbis_ru = Sbis(browser)
    sbis_ru.open_web_page_sbis_ru()
    assert sbis_ru.menu_contacts_is_displayed()
    sbis_ru.click_menu_contacts()
    time.sleep(5)

    sbis_ru.find_established_region()
    assert sbis_ru.get_text_established_region() == "Ярославская обл.", "Регион не определился"
    assert sbis_ru.established_region_is_displayed
    assert len(sbis_ru.find_partners_established_region()) > 0, "Отсутствует список контактов"
    partners_current_region = sbis_ru.get_partners(sbis_ru.find_partners_established_region())

    sbis_ru.click_established_region()
    sbis_ru.find_new_region()
    sbis_ru.click_new_region()
    time.sleep(5)

    assert sbis_ru.get_text_established_region() == 'Камчатский край', "Выбранный регион не подставился"
    partners_new_region = sbis_ru.get_partners(sbis_ru.find_partners_established_region())
    assert len(partners_current_region - partners_new_region) != 0, "Список партнеров не изменился"
    assert browser.current_url.find("kamchatsk") != -1, "url вкладки не cодержит информацию выбранного региона"
    assert browser.title.find("Камчатс") != -1, "title вкладки не cодержит информацию выбранного региона"


def test_third_task_from_get_test_tasks(browser):
    sbis_ru = Sbis(browser)
    sbis_ru.open_web_page_sbis_ru()

    sbis_ru.scroll_download_local_versions()
    assert sbis_ru.download_local_versions_is_displayed()
    sbis_ru.click_download_local_versions()

    sbis_ru.find_tab_sbis_plagin()
    sbis_ru.click_tab_sbis_plagin()
    time.sleep(1)
    sbis_ru.find_tab_os_windows()
    sbis_ru.find_tab_os_windows()
    time.sleep(1)
    sbis_ru.find_web_installer()
    sbis_ru.click_web_installer()
    time.sleep(5)

    assert len(sbis_ru.get_list_of_exe_files_in_current_directory_with_path()) > 0, "Плагин не скачался"

    assert sbis_ru.get_size_file_from_website() == sbis_ru.get_size_file_from_current_directory(), \
        "Размер скаченного файла не совпадает с размером файла, указанного на сайте"
