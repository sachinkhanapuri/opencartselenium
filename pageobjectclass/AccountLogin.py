from selenium.webdriver.common.by import By

class SetAccountLogin:

    #Locators
    input_email_id="input-email"
    input_password_id="input-password"
    input_submit_xpath="//input[@type='submit']"
    heading_account_xpath="//div[@id='content']/h2[1]"
    display_error_xpath="//div[@id='account-login']/div[1]"

    #Constructor
    def __init__(self,driver):
        self.driver=driver

    #Action Method
    def setemailuser(self,emailid):

        self.email=self.driver.find_element(By.ID,self.input_email_id)
        self.email.clear()
        self.email.send_keys(emailid)

    def setpassworduser(self,password):
        self.password=self.driver.find_element(By.ID,self.input_password_id)
        self.password.clear()
        self.password.send_keys(password)

    def submit(self):
        self.driver.find_element(By.XPATH,self.input_submit_xpath).click()

    def displayaccount(self):
        try:
            return self.driver.find_element(By.XPATH,self.heading_account_xpath).is_displayed()
        except:
            return False

    def displayerrormsg(self):
        return self.driver.find_element(By.XPATH,self.display_error_xpath)