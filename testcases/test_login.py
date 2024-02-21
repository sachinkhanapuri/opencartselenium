import time
import pytest
from pageobjectclass.AccountLogin import SetAccountLogin
from pageobjectclass.HomePage import SetHomePage
from utilities.readproperties import ReadConfig


class TestLogin:
    @pytest.mark.sanity
    def testlogin(self,setup):
        self.driver=setup                    # ---> Initilazed the driver object
        url=ReadConfig.getApplicationurl()      # Reading the url from config.ini file through utilites by using static method,means calling with class name
        #print("url:", url)
        self.driver.get(url=url)
        self.driver.maximize_window()
        time.sleep(2)

        self.hp=SetHomePage(self.driver)     # ---> Creating the object for homepage pageobject model class by passing driver
        self.hp.Account()                    # ---> Calling the account method
        self.hp.Login()                      # ---> Calling the Login method
        time.sleep(3)

        self.accountlogin=SetAccountLogin(self.driver)          # ---> Creating the object for Accountlogin pageobject model class by passing driver
        time.sleep(4)

        email,password = ReadConfig.logindetails()              # --> Taking email data as well as password from config.ini file through utilites
        print("email:",email)
        print("password:",password)
        self.accountlogin.setemailuser(email)
        self.accountlogin.setpassworduser(password)
        self.accountlogin.submit()
        time.sleep(4)

    def testdemo(self):
        print("this is sample test")

