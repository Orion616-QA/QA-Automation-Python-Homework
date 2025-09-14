"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import os
import unittest

# Створення та налаштування логера
logging.basicConfig(
    filename='login_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("log_event")
logger.setLevel(logging.INFO)

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

class TestingLogWork(unittest.TestCase):
    log_file = 'login_system.log'

    def setUp(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

        self.file_handler = logging.FileHandler(self.log_file)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(formatter)

        logger.addHandler(self.file_handler)

    def tearDown(self):
        logger.removeHandler(self.file_handler)

        self.file_handler.close()

        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_file_exist(self):
        log_event("Ivan", "success")

        expected_result = True
        actual_result = os.path.exists(self.log_file)

        self.assertEqual(expected_result, actual_result)

    def test_log_success(self):
        log_event("John", "success")
        expected_message = "Login event - Username: John, Status: success"
        expected_level = "INFO"

        with open(self.log_file) as f:
            actual_result = f.read().strip()

        self.assertIn(expected_message, actual_result)
        self.assertIn(expected_level, actual_result)

    def test_log_expired(self):
        log_event("Tom", "expired")
        expected_message = "Login event - Username: Tom, Status: expired"
        expected_level = "WARNING"

        with open(self.log_file) as f:
            actual_result = f.read().strip()

        self.assertIn(expected_message, actual_result)
        self.assertIn(expected_level, actual_result)

    def test_log_error(self):
        log_event("Jim", 'sometest')
        expected_message = "Login event - Username: Jim, Status: sometest"
        expected_level = "ERROR"

        with open(self.log_file) as f:
            actual_result = f.read().strip()

        self.assertIn(expected_message, actual_result)
        self.assertIn(expected_level, actual_result)


if __name__ == '__main__':
    unittest.main()
