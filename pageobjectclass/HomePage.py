from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class SetHomePage:

    # Locators
    span_account_xpath="//ul[@class='list-inline']/li[2]/a/span[1]"
    a_register_xpath="//ul[@class='list-inline']/li[2]/ul/li[1]/a"
    a_login_xpath="//ul[@class='list-inline']/li[2]/ul/li[2]/a"

    # Constructor
    def __init__(self,driver):
        self.driver=driver
        self.act=ActionChains(self.driver)

    # Action methods
    def Account(self):
        account=self.driver.find_element(By.XPATH,self.span_account_xpath)
        self.act.move_to_element(account).click().perform()

    def Register(self):
        self.driver.find_element(By.XPATH,self.a_register_xpath).click()

    def Login(self):
        self.driver.find_element(By.XPATH,self.a_login_xpath).click()