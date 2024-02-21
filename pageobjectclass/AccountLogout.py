from selenium.webdriver.common.by import By

class SetAccountLogout:

    a_logout_xpath="//li[@class='dropdown open']/ul/li[5]/a"

    def __init__(self,driver):
        self.driver=driver

    def logout(self):
        self.driver.find_element(By.XPATH,self.a_logout_xpath).click()
