import time

from pageobjectclass.AccountLogin import SetAccountLogin
from pageobjectclass.HomePage import SetHomePage
from pageobjectclass.AccountLogout import SetAccountLogout
from utilities.XLUtilis import GetExcelData
from utilities.readproperties import ReadConfig


class TestLoginDDT:

    def testloginddt(self,setup):

        self.driver = setup
        url = ReadConfig.getApplicationurl()         # Reading the url from config.ini file through utilites
        self.driver.get(url=url)
        self.driver.maximize_window()
        time.sleep(2)

        self.hp = SetHomePage(self.driver)              # Object creation for Homepage pageobject model class
        self.hp.Account()
        self.hp.Login()
        time.sleep(4)

        self.file=ReadConfig.getexeclefilepath()        # Reading the filepath from config.ini file by using utilites.py file.
        self.exceldata=GetExcelData(self.file,'Sheet1')
        self.row=self.exceldata.getrows()
        self.col=self.exceldata.getcols()
        print("row:",self.row)
        print("col:",self.col)
        for r in range(2,self.row+1):


            self.email=self.exceldata.ReadData(r,1)
            self.password=self.exceldata.ReadData(r,2)
            self.excepted_result=self.exceldata.ReadData(r,3)
            print('email:',self.email)
            print('password:',self.password)
            print("e:",self.excepted_result)

            self.acclogin = SetAccountLogin(self.driver)     #  Object creation for Accounlogin pageobject model class
            self.acclogin.setemailuser(self.email)
            self.acclogin.setpassworduser(self.password)
            self.acclogin.submit()
            time.sleep(3)
            self.displaydata=self.acclogin.displayaccount()
            print("display:",self.displaydata)

            if self.displaydata == True:
                if self.excepted_result == 'passed':
                    self.exceldata.WriteData(self.file,"Sheet1",r,4,'passed')
                else:
                    self.exceldata.WriteData(self.file,"Sheet1",r, 4, 'failed')
            else:
                self.exceldata.WriteData(self.file,"Sheet1",r, 4, 'failed')

