"""
API тесты для Skyeng
"""

import pytest
import allure


@pytest.mark.api
class TestTeacherAPI:

    @allure.epic("Личные события")
    @allure.feature("API тесты")
    @allure.story("Создание события")
    @allure.title("API: Создание личного события")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_personal_event(self, api_client, test_data):
        """Создание личного события через API"""
        event = test_data["event"].copy()
        event["title"] = test_data["unique_title"]("Личное событие")

        response = api_client.post("/schedule/events", event)

        if response.status_code == 401:
            pytest.skip("Требуется авторизация (401)")

        assert response.status_code in [200, 201], (
            "Событие не создано"
        )

    @allure.epic("Личные события")
    @allure.feature("API тесты")
    @allure.story("Создание урока")
    @allure.title("API: Создание урока по математике")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_math_lesson(self, api_client, test_data):
        """Создание урока по математике через API"""
        lesson = test_data["lesson"].copy()
        lesson["title"] = test_data["unique_title"]("Урок математики")

        response = api_client.post("/schedule/events", lesson)

        if response.status_code == 401:
            pytest.skip("Требуется авторизация (401)")

        assert response.status_code in [200, 201], (
            "Урок не создан"
        )

    @allure.epic("Личные события")
    @allure.feature("API тесты")
    @allure.story("Редактирование события")
    @allure.title("API: Редактирование события")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_event(self, api_client, test_data):
        """Редактирование события через API"""
        event = test_data["event"].copy()
        event["title"] = test_data["unique_title"](
            "Событие для редактирования"
        )

        create_response = api_client.post("/schedule/events", event)
        if create_response.status_code == 401:
            pytest.skip("Требуется авторизация (401)")

        event_id = create_response.json().get("id", 1)

        updated = test_data["updated"].copy()
        updated["title"] = test_data["unique_title"](
            "Обновленное событие"
        )

        url = f"/schedule/events/{event_id}"
        response = api_client.put(url, updated)

        assert response.status_code in [200, 204], (
            "Событие не обновлено"
        )

    @allure.epic("Личные события")
    @allure.feature("API тесты")
    @allure.story("Удаление события")
    @allure.title("API: Удаление события")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_event(self, api_client, test_data):
        """Удаление события через API"""
        event = test_data["event"].copy()
        event["title"] = test_data["unique_title"](
            "Событие для удаления"
        )

        create_response = api_client.post("/schedule/events", event)
        if create_response.status_code == 401:
            pytest.skip("Требуется авторизация (401)")

        event_id = create_response.json().get("id", 1)

        url = f"/schedule/events/{event_id}"
        response = api_client.delete(url)

        assert response.status_code in [200, 204], (
            "Событие не удалено"
        )

    @allure.epic("Личные события")
    @allure.feature("API тесты")
    @allure.story("Негативные сценарии")
    @allure.title("API: Создание события в прошлом (негативный)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_past_event(self, api_client, test_data):
        """Создание события в прошлом - должно вернуть ошибку"""
        past_event = test_data["past_event"].copy()
        past_event["title"] = test_data["unique_title"](
            "Событие в прошлом"
        )

        response = api_client.post("/schedule/events", past_event)

        if response.status_code == 401:
            pytest.skip("Требуется авторизация (401)")

        assert response.status_code in [400, 422], (
            "Ожидалась ошибка!"
        )
