import time
import pytest
import os

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup(browser):
    if browser == 'Edge':
        service=Service(executable_path=EdgeChromiumDriverManager().install())
        driver=webdriver.Edge(service=service)
    elif browser == 'Firefox':
        service=Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    return driver


########################### Hokes for sending the browser command from CLI ###############################
def pytest_addoption(parser):           # This take the browser value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                   # This will return the browser value to setup method
    return request.config.getoption("--browser")


################################## Pytest HTML Report #####################################################
#
# # It is a hook for Adding Enviroment info to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name']='OpenCart'
#     config._metadata['Module Name']='CurtRegistration'
#     config._metadata['Tester']= 'Sachin'
#
# # It is a hook for deleting/Adding enviroment info to HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)
#
# # Specifying the report folder location and save report with timestamp
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     path = os.getcwd()
#     print("pathh:", path)
#     report = path + '\\reports\\'
#     config.option.htmlpath = report + datetime.now().strftime("%d-%m-%Y" "%H-%M-%S")+".html"


