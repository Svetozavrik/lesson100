"""Фикстуры и тестовые данные для дипломного проекта"""


import pytest
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "https://skyeng.ru"
API_URL = "https://api-teachers.skyeng.ru/v2"


LOGIN = "test.tst317@skyeng.ru"
PASSWORD = "Abc1234567890"


def unique_title(prefix="Событие"):
    """Создает уникальное название с текущим временем"""
    return f"{prefix} {int(time.time())}"


LESSON_DATA = {
    "title": "Урок математики",
    "date": "2026-08-20",
    "time_start": "10:00",
    "time_end": "11:00",
    "student": "Светлана Баженова",
    "subject": "Математика"
}

EVENT_DATA = {
    "title": "Личное событие",
    "date": "2026-08-15",
    "time_start": "10:00",
    "time_end": "11:00",
    "description": "Встреча с коллегами"
}

UPDATED_EVENT_DATA = {
    "title": "Обновленное событие",
    "date": "2026-08-16",
    "time_start": "14:00",
    "time_end": "15:00",
    "description": "Семинар"
}

PAST_EVENT_DATA = {
    "title": "Событие в прошлом",
    "date": "2020-01-01",
    "time_start": "10:00",
    "time_end": "11:00",
    "description": "Это событие уже прошло"
}


SELECTORS = {
    "add_btn": "button.add-event, .create-event-btn",
    "save_btn": "button.save-event, .submit-btn",
    "edit_btn": "button.edit-event, .edit-btn",
    "delete_btn": "button.delete-event, .delete-btn",
    "confirm_btn": "button.confirm, .confirm-btn",
    "title_input": "input[name='title'], .title-input",
    "date_input": "input[name='date'], .date-input",
    "time_start": "input[name='time_start'], .time-start",
    "time_end": "input[name='time_end'], .time-end",
    "desc_input": "textarea[name='description'], .desc-input",
    "student_input": "input[name='student'], .student-input",
    "subject_input": "input[name='subject'], .subject-input",
    "event_item": ".event-item, .calendar-event",
    "lesson_item": ".lesson-item, .schedule-lesson",
    "success_msg": ".success, .toast-success",
    "error_msg": ".error, .toast-error",
}

WAIT = {"fast": 3, "medium": 10, "slow": 30}


def get_headers():
    """Заголовки для API запросов"""
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


@pytest.fixture
def api_client():
    """API клиент для отправки запросов"""
    class APIClient:
        def __init__(self):
            self.base_url = API_URL
            self.session = requests.Session()
            self.session.headers.update(get_headers())

        def get(self, endpoint):
            return self.session.get(f"{self.base_url}{endpoint}")

        def post(self, endpoint, data):
            return self.session.post(f"{self.base_url}{endpoint}", json=data)

        def put(self, endpoint, data):
            return self.session.put(f"{self.base_url}{endpoint}", json=data)

        def delete(self, endpoint):
            return self.session.delete(f"{self.base_url}{endpoint}")

    return APIClient()


@pytest.fixture
def test_data():
    """Тестовые данные для всех тестов"""
    return {
        "unique_title": unique_title,
        "lesson": LESSON_DATA,
        "event": EVENT_DATA,
        "updated": UPDATED_EVENT_DATA,
        "past_event": PAST_EVENT_DATA,
        "selectors": SELECTORS,
        "wait": WAIT
    }


@pytest.fixture
def driver():
    """Браузер для UI тестов"""
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
