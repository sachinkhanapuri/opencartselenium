import time

import pytest
from pageobjectclass.HomePage import SetHomePage
from pageobjectclass.AccountLogin import SetAccountLogin
from pageobjectclass.OrderPlace import SetOrderplace
from utilities.readproperties import ReadConfig
from selenium.webdriver.support.select import Select

class TestOrderSuccess:
    @pytest.mark.sanity
    def testordersuccess(self,setup):
        self.driver=setup

        self.url=ReadConfig.getApplicationurl()
        self.driver.get(url=self.url)
        self.driver.maximize_window()
        time.sleep(4)

        self.hp=SetHomePage(self.driver)
        self.hp.Account()
        self.hp.Login()

        self.acclogin=SetAccountLogin(self.driver)
        email, password = ReadConfig.logindetails()  # --> Taking email data as well as password from config.ini file through utilites
        print("email:", email)
        print("password:", password)
        self.acclogin.setemailuser(email)
        self.acclogin.setpassworduser(password)
        self.acclogin.submit()
        time.sleep(4)

        ### orderplace page object model class ####
        self.op=SetOrderplace(self.driver)
        self.op.desktops()
        self.op.Macorder()
        time.sleep(2)
        self.op.ClickAddcart()
        self.op.ClickItem()
        self.op.Checkout()
        time.sleep(3)

        self.op.ClickOnAddNewAddress()
        self.op.AddFirstname('Snehal')
        self.op.AddLastname("khanapuri")
        self.op.AddCompany("abc.pvt.ltd")
        self.op.AddNewAddress("510 xriba hinjewadi marunji")
        self.op.AddCity('pune')
        self.op.AddPostcode("538904")
        self.countrydata=self.op.AddCountry()
        selectcountrydata=Select(self.countrydata)
        selectcountrydata.select_by_visible_text("India")
        time.sleep(4)
        self.zonedata=self.op.AddZone()
        selectzone = Select(self.zonedata)
        selectzone.select_by_visible_text("Maharashtra")
        self.op.SubmitAddressbtn()
        time.sleep(4)

        self.op.DeliveryAddress()
        self.deliveraddress=self.op.SelectDeliveryAddress()
        time.sleep(3)
        for existaddres in self.deliveraddress:
            print(existaddres.text)
            if existaddres.text == "Snehal khanapuri, 510 xriba hinjewadi marunji, pune, Maharashtra, India":
                existaddres.click()
        time.sleep(4)
        self.op.ButtonShippingAddress()
        time.sleep(4)
        self.op.ButtonShippingmethod()
        time.sleep(2)
        self.op.CashonDelivery()
        time.sleep(2)
        self.op.ConfirmBtn()
        time.sleep(2)
        self.op.Myaccount()
        time.sleep(4)