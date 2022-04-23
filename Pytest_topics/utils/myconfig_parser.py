import configparser
from pathlib import Path

cfg_file = "qa.ini"
cfg_file_dir = "config"

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfg_file_dir).joinpath(cfg_file)

config.read(CONFIG_FILE)


def get_gmail_url() -> str:
    return config["gmail"]["url"]


def get_gmail_user() -> str:
    return config["gmail"]["user"]


def get_gmail_pass() -> str:
    return config["gmail"]["pass"]


if __name__ == '__main__':
    print(get_gmail_url())
