import loguru
import json
import os
import inspect
from json.decoder import JSONDecodeError
from pathlib import Path
from datetime import datetime


def get_root_dir() -> Path:
    return Path(__file__).parent.parent.parent


class Logger:
    _instance = None
    _worker_id = None  # builtin fixture worker_id
    _root_dir = get_root_dir()

    def __init__(self):
        self.logger = loguru.logger
        with open(os.path.join(Logger._root_dir, "configs", "logger_config.json")) as config_file:
            self.config = json.load(config_file)
        log_file = os.path.join(Logger._root_dir, "logs", f"{datetime.now().strftime('%H_%M_%S')}.log")
        self.logger.add(sink=log_file, format=self.config['format'], level=self.config['level'],
                        rotation=self.config['rotation'], retention=self.config['retention'],
                        compression=self.config['compression'], encoding="utf-8")
        self.step_counter = None

    @staticmethod
    def get_logger():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def test_name(self, **kwargs):
        self.step_counter = 0
        test_name = inspect.stack()[1][3]
        self.logger.info(f"START TEST: {test_name}, {kwargs}" + "\n")

    def step(self, step_desc: str):
        self.step_counter += 1
        self.logger.info(f"{'~' * 50}")
        self.logger.info(f"STEP {self.step_counter}: {step_desc}")
        self.logger.info(f"{'~' * 50}" + '\n')

    def debug(self, msg):
        self.logger.debug(f'{"*" * 50}')
        self.logger.debug(msg)
        self.logger.debug(f'{"*" * 50}' + '\n')

    def error(self, msg):
        self.logger.error(f'{"x" * 50}')
        self.logger.error(msg)
        self.logger.error(f'{"x" * 50}' + '\n')

    def api(self, response):
        self.logger.info(f"{'*' * 50}")
        self.logger.info(f"HTTP Method: {response.request.method} - {response.url}")
        self.logger.debug(f'req_headers: {response.request.headers}')
        self.logger.debug(f'req_body: {response.request.body}')
        self.logger.debug('-' * 50)
        self.logger.debug(f'res_status_code: {response.status_code}')
        self.logger.debug(f'res_headers: {response.headers}')
        try:
            self.logger.debug(f'res_body: {response.json()}')
        except JSONDecodeError:
            self.logger.debug(f"Response without json_data")
        self.logger.info(f"{'*' * 50}" + '\n')