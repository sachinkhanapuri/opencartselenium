from selenium.webdriver.common.by import By

class SetAccountRegistration:

    #locators:
    input_firstname_id="input-firstname"
    input_lastname_id="input-lastname"
    input_email_id="input-email"
    input_telephone_id="input-telephone"
    input_password_id="input-password"
    input_confirmpwd_id="input-confirm"
    input_radio_xpath="//label[@class='radio-inline']/input"
    input_checkbox_xpath="//input[@type='checkbox']"
    input_submit_xapth="//input[@type='submit']"
    h1_confirmtext_xpath="//div[@id='content']/h1"
    a_continue_linktext='Continue'

    #constructor
    def __init__(self,driver):
        self.driver=driver

    def setfirstname(self,firstname):
        self.driver.find_element(By.ID,self.input_firstname_id).send_keys(firstname)

    def setlastname(self, lastname):
        self.driver.find_element(By.ID, self.input_lastname_id).send_keys(lastname)

    def setemailid(self, email):
        self.driver.find_element(By.ID, self.input_email_id).send_keys(email)

    def settelephone(self, telephone):
        self.driver.find_element(By.ID, self.input_telephone_id).send_keys(telephone)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.input_password_id).send_keys(password)

    def setconfirmpwd(self, confirmpwd):
        self.driver.find_element(By.ID, self.input_confirmpwd_id).send_keys(confirmpwd)

    def setradiobtn(self):
        radiobtn=self.driver.find_elements(By.XPATH,self.input_radio_xpath)
        return radiobtn

    def setcheckbox(self):
        self.driver.find_element(By.XPATH,self.input_checkbox_xpath).click()

    def setsubmitbtn(self):
        self.driver.find_element(By.XPATH,self.input_submit_xapth).click()

    def confirmmsg(self):
        return self.driver.find_element(By.XPATH,self.h1_confirmtext_xpath)

    def setContinue(self):
        self.driver.find_element(By.LINK_TEXT,self.a_continue_linktext).click()