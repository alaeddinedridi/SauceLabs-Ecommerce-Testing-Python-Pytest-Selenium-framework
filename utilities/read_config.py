import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/config.ini")

# This is used to read properties from config.ini file, and we are doing it this way, because the config will
# be used by multiple testcase, so we don't write the same thing each time
class ReadConfig:

    #Static methods used to be accessed directly without the need to instantiate the ReaadConfig Object
    #To read a property, we have to indicate under which block/group it is, then we give the property name we want to read from te config
    @staticmethod
    def getApplicationURL():
        baseUrl=config.get("common data for testcases","baseUrl")
        return baseUrl

    @staticmethod
    def getUsername():
        username=config.get("common data for testcases","username")
        return username

    @staticmethod
    def getPassword():
        password=config.get("common data for testcases","password")
        return password

