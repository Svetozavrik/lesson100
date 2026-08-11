"""
UI тесты для Skyeng
"""

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
class TestTeacherUI:

    @allure.epic("Личные события")
    @allure.feature("UI тесты")
    @allure.story("Загрузка страниц")
    @allure.title("UI: Проверка загрузки главной страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_main_page_load(self, driver):
        """Проверка загрузки главной страницы"""
        driver.get("https://skyeng.ru")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        assert "skyeng" in driver.current_url.lower()

    @allure.epic("Личные события")
    @allure.feature("UI тесты")
    @allure.story("Проверка элементов")
    @allure.title("UI: Проверка заголовка страницы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_title(self, driver):
        """Проверка заголовка страницы"""
        driver.get("https://skyeng.ru")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        title = driver.title
        assert len(title) > 0

    @allure.epic("Личные события")
    @allure.feature("UI тесты")
    @allure.story("Проверка элементов")
    @allure.title("UI: Проверка наличия элементов на странице")
    @allure.severity(allure.severity_level.NORMAL)
    def test_main_elements(self, driver):
        """Проверка наличия основных элементов"""
        driver.get("https://skyeng.ru")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        links = driver.find_elements(By.TAG_NAME, "a")
        assert len(links) > 0

        buttons = driver.find_elements(By.TAG_NAME, "button")
        assert len(buttons) > 0

    @allure.epic("Личные события")
    @allure.feature("UI тесты")
    @allure.story("Навигация")
    @allure.title("UI: Проверка страницы расписания")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_schedule_page(self, driver):
        """Проверка загрузки страницы расписания"""
        driver.get("https://teacher.skyeng.ru/schedule")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        current_url = driver.current_url.lower()
        assert "skyeng.ru" in current_url

    @allure.epic("Личные события")
    @allure.feature("UI тесты")
    @allure.story("Проверка элементов")
    @allure.title("UI: Проверка наличия формы на странице")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_has_form(self, driver):
        """Проверка наличия формы на странице"""
        driver.get("https://skyeng.ru")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        forms = driver.find_elements(By.TAG_NAME, "form")
        assert len(forms) > 0

        inputs = driver.find_elements(By.TAG_NAME, "input")
        assert len(inputs) > 0
