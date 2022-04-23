from Pytest_topics.utils.myconfig_parser import get_gmail_url
from Pytest_topics.utils.config_file_parcer import ConfigFileParser

config = ConfigFileParser("prod.ini")


def test_getgmailurl():
    assert "gmail.com" in get_gmail_url()


def test_get_outlook_url():
    assert "outlook.com" in config.get_outlook_url()
