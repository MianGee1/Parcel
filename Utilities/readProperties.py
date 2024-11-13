import configparser

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")


class ReadConfig():

    @staticmethod
    def getWebsiteURL():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getUserpassword():
        password = config.get('common data', 'password')
        return password