import json
import logging
import os

from datetime import datetime, timedelta, date
from logging import config
from time import localtime, strftime


def setup_logging():
    if "hb_test.log" in os.listdir("./"):
        os.rename("./hb_test.log",
                  f"./hb_test_{strftime('%d-%m-%Y_%H:%M:%S', localtime())}.log")
    config_file = "./logging_config.json"
    with open(config_file) as file:
        desired_configuration = json.load(file)
    logging.config.dictConfig(desired_configuration)


class HeartbeatMonitoringLogger:
    __thread_pattern: str = "Key TSTFEED0240|7E3E|0400"
    __filtered_lines_list: list[str]

    def __init__(self, thread_pattern: str):
        setup_logging()
        self.__thread_pattern = thread_pattern

    def check_system_and_return_logs(self):
        self.__filtered_lines_list = list(self.__get_lines_with_desired_pattern().__reversed__())

        for period, line in enumerate(self.__filtered_lines_list):
            if period < len(self.__filtered_lines_list) - 1:
                start_time: datetime = self.__format_str_time_into_datetime(
                    self.__return_timestamp_value_from_line(line))
                end_time: datetime = self.__format_str_time_into_datetime(
                    self.__return_timestamp_value_from_line(self.__filtered_lines_list[period + 1]))
                self.__log_based_on_timedelta(start_time, end_time)

    def __log_based_on_timedelta(self, start_time: datetime, end_time: datetime):
        if (end_time - start_time) == timedelta(seconds=32):
            self.__write_warning_logs(end_time.time())
        elif (end_time - start_time) >= timedelta(seconds=33):
            self.__write_error_logs(end_time.time())

    def __format_str_time_into_datetime(self, str_time) -> datetime:
        return datetime.strptime(str_time, "%H:%M:%S")

    def __get_lines_with_desired_pattern(self) -> list[str]:
        with open("./hblog.txt", "r+") as file:
            return [line.strip() for line in file if line.find(self.__thread_pattern) != -1]

    def __return_timestamp_value_from_line(self, line: str) -> str:
        list_of_line_items: list[str] = line.split()
        return list_of_line_items[list_of_line_items.index("Timestamp") + 1]

    def __write_warning_logs(self, raised_time) -> None:
        logger.warning(f"Warning log was raised at: {raised_time}")

    def __write_error_logs(self, raised_time) -> None:
        logger.error(f"Error log was raised at: {raised_time}")

logger = logging.getLogger(__name__)

heart_beat_monitoring_logger: HeartbeatMonitoringLogger = HeartbeatMonitoringLogger("Key TSTFEED0300|7E3E|0400")
heart_beat_monitoring_logger.check_system_and_return_logs()