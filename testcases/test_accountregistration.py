import time

import pytest
from pageobjectclass.HomePage import SetHomePage
from pageobjectclass.AccountRegistration import SetAccountRegistration
from utilities.randomstring import Genrandomstring
from utilities.readproperties import ReadConfig


class TestClass:
    @pytest.mark.sanity
    def testhomepage(self,setup):

        self.driver=setup                      # ---> Initilazted the driver object
        url = ReadConfig.getApplicationurl()    # Reading the url from config.ini file through utilites
        # print("url:", url)
        self.driver.get(url=url)
        self.driver.maximize_window()
        time.sleep(2)

        self.hp=SetHomePage(self.driver)       # ---> Creating the object for SetHomPage and passing the driver
        self.hp.Account()                      # ---> Calling the method of Account()
        self.hp.Register()                     # ---> Calling the method of Register()
        time.sleep(4)


        self.setacc=SetAccountRegistration(self.driver)             # ---> Creating the object for AccountRegistration
        time.sleep(2)

        self.setacc.setfirstname("sachin")
        self.setacc.setlastname("khanapuri")
        self.setacc.setemailid(Genrandomstring(10))
        self.setacc.settelephone("9284125520")
        self.setacc.setpassword("khanapuri09")
        self.setacc.setconfirmpwd("khanapuri09")
        self.radiobtns=self.setacc.setradiobtn()
        for radiobtn in self.radiobtns:
            if radiobtn.get_attribute('value') == "1":
                radiobtn.click()
        time.sleep(2)
        self.setacc.setcheckbox()
        self.setacc.setsubmitbtn()
        time.sleep(4)

        self.msg=self.setacc.confirmmsg()
        print("msg:",self.msg.text)
        if self.msg.text=='Your Account Has Been Created!':
            self.setacc.setContinue()
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

        time.sleep(4)