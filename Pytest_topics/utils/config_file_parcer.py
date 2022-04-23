import configparser
from pathlib import Path

cfg_file = "qa.ini"
cfg_file_dir = "config"

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfg_file_dir).joinpath(cfg_file)

config.read(CONFIG_FILE)


class ConfigFileParser:
    def __init__(self, cfg="qa.ini", cfg_dir="config"):
        self.cfg_file = cfg  # default config file
        self.cfg_file_dir = cfg_dir  # default config dir

        self.config = configparser.ConfigParser()
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfg_file_dir).joinpath(self.cfg_file)

        self.config.read(self.CONFIG_FILE)

    def get_url(self, provider="gmail") -> str:
        return self.config[provider]["url"]

    def get_user(self, provider="gmail") -> str:
        return self.config[provider]["user"]

    def get_pass(self, provider="gmail") -> str:
        return self.config[provider]["pass"]

    def get_gmail_url(self):
        return self.get_url("gmail")

    def get_outlook_url(self):
        return self.get_url("outlook")

    def get_gmail_user(self):
        return self.get_user("gmail")

    def get_outlook_user(self):
        return self.get_user("outlook")

    def get_gmail_pass(self):
        return self.get_pass("gmail")

    def get_outlook_pass(self):
        return self.get_pass("outlook")


if __name__ == '__main__':
    config = ConfigFileParser("qa.ini")
    print(config.get_gmail_pass())
    print(config.get_outlook_pass())
