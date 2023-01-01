import os
import shelve
from typing import Any

from appdirs import user_config_dir

app_name = "epomodoro"


def check_if_folder_exist_and_create_it():
    if not os.path.exists(user_config_dir(app_name)):
        os.makedirs(user_config_dir(app_name), exist_ok=True)


class Metric:
    def __init__(self, db_name: str) -> None:
        check_if_folder_exist_and_create_it()
        self.db_name = f"{user_config_dir(app_name)}/{db_name}.db"

    def get_value(self, key: str) -> Any:
        with shelve.open(self.db_name) as db:
            return db[key]

    def set_value(self, key: str, value: Any) -> None:
        with shelve.open(self.db_name) as db:
            db[key] = value

    def check_value_exist(self, key: str) -> bool:
        with shelve.open(self.db_name) as db:
            if key in db:
                return True
        return False

    def clean_values(self) -> None:
        with shelve.open(self.db_name) as db:
            db.clear()
