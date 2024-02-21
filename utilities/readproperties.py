"""
    Reading the data from config.ini file into utilites(readproperties.py) , then from utilites(readproperties.py) we can use into any testcase file.
            config.ini ---> utilites(readproperties.py) ---> Testcases
"""
import configparser
import os

# config=configparser.RawConfigParser()
path = os.path.abspath("C:\\Users\\Snehal\\PycharmProjects\\Python_Selenium_framework\\Selenium_Hybrid_Framework")
print("path:", path)
newpath = os.path.join(path, 'configurations\\config.ini')
print("newpath:", newpath)


def configuration():
    config = configparser.ConfigParser()
    config.read(newpath)
    return config

class ReadConfig:
    @staticmethod
    def getApplicationurl():
        #url=config.get('config','url')
        url=configuration()['configinfo']['baseurl']
        #print("url:",url)
        return url

    @staticmethod
    def logindetails():
        email=configuration()['configinfo']['email']
        password=configuration()['configinfo']['password']
        return email ,password

    @staticmethod
    def getexeclefilepath():
        filepath=configuration()['configinfo']['excelfilepath']
        return filepath

#readconfi=ReadConfig()
# print(readconfi.getApplicationurl())
#print(readconfi.getexeclefilepath())