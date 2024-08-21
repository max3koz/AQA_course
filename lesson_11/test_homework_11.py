import logging

from assertpy import assert_that
from lesson_11.log_event_fun import log_event
from logging import config


user_name="testuser"

logging.config.fileConfig('logging_config.ini')
logging.getLogger('sampleLogger')

def logger_message_parser() -> str:
    with open("login_system.log") as f:
        log_string = f.readlines()[-1]
    return log_string

def verify_status_and_log_level_values(log_level, status):
    for item in [log_level, status]:
        is_true = item in logger_message_parser()
        assert_that(is_true).is_true()

class TestLoggerEvent:

    def test_log_with_use_username_in_message(self, status="success"):
        logging.info(f"Step_1: Get log string for '{user_name}' with status '{status}'")
        log_event(user_name, status)
        logging.info(f"Step_2: Verify expected username '{user_name}' in the log string")
        is_true = user_name in logger_message_parser()
        assert_that(is_true).is_true()

    def test_log_with_success_status_and_info_log_level(self, log_level="INFO", status="success"):
        logging.info(f"Step_1: Get log string for '{user_name}' with status '{status}'")
        log_event(user_name, status)
        logging.info(f"Step_2: Verify expected status '{status}' and log level {log_level} in the log string")
        verify_status_and_log_level_values(log_level, status)

    def test_log_with_expired_status_and_warning_log_level(self, log_level="WARNING", status="expired"):
        logging.info(f"Step_1: Get log string for '{user_name}' with status '{status}'")
        log_event(user_name, status)
        logging.info(f"Step_2: Verify expected status '{status}' and log level {log_level} in the log string")
        verify_status_and_log_level_values(log_level, status)

    def test_log_with_invalid_status_and_error_log_level(self, log_level="ERROR", status="succ"):
        logging.info(f"Step_1: Get log string for '{user_name}' with status '{status}'")
        log_event(user_name, status)
        logging.info(f"Step_2: Verify expected status '{status}' and log level {log_level} in the log string")
        verify_status_and_log_level_values(log_level, status)
