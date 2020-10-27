import configparser


config = configparser.RawConfigParser()
config.read("C:\\Users\\sgite\\PycharmProjects\\HybridFrameWork\\Configurations\\config1.ini")


class ConfigReader :
    @staticmethod
    def get_application_url():
        url = config.get("basic info", "base_url")
        return url

    @staticmethod
    def get_login_username():
        username = config.get("basic info", "username")
        return username

    @staticmethod
    def get_login_password () :
        password = config.get("basic info", "password")
        return password

    @staticmethod
    def getArrtibute():
        attribute = config.get("basic info","attribute")
        return attribute