from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver

class SetOrderplace:

    #Locator
    a_desktop_linktext="Desktops"
    a_mac_linktext="Mac (1)"
    span_cart_xpath="//div[@class='button-group']/button[1]"
    button_item_xpath="//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']"
    a_checkout_xpath="//p[@class='text-right']/a[2]"

    input_billingaddress_xpath="//input[contains(@value,'new')]"
    input_firstname_id="input-payment-firstname"
    input_lastname_id="input-payment-lastname"
    input_company_id="input-payment-company"
    input_address_id="input-payment-address-1"
    input_city_id="input-payment-city"
    input_postcode_id="input-payment-postcode"
    select_country_xpath="//select[@name='country_id']"
    select_zone_xpath="//select[@id='input-payment-zone']"
    input_paymentaddresssubmitbtn_id="button-payment-address"

    input_deliveryaddress_xpath="//input[contains(@name,'shipping_address') and contains(@checked,'checked')]"
    select_deliveryaddress_xapth="//div[@id='accordion']/div[3]/div[2]/div/form/div[2]/select/option"
    input_shippingaddress_xpath="//input[@id='button-shipping-address']"

    input_shippingmethod_xpath="//div[@class='buttons']/div/input"
    input_cod_xpath="//input[@value='cod']"
    input_agreebutton_xpath="//input[@name='agree']"
    input_continuebtn_xpath="//input[@id='button-payment-method']"

    input_confirmbtn_id='button-confirm'
    a_myaacount_xpath="//div[@id='content']/p[2]/a[1]"
    # select_address_xpath="//div[@id='payment-existing']/select"
    # continue_input_id='button-payment-address'
    # button_input_value='existing'
    # shipping_select_xpath="//div[@id='shipping-existing']/select"
    # continue_input_id2='button-shipping-address'

    #Constructor
    def __init__(self,driver):
        self.driver=driver

    #Action Method
    def desktops(self):
        desktop_drop=self.driver.find_element(By.LINK_TEXT,self.a_desktop_linktext)
        self.acts=ActionChains(self.driver)
        self.acts.move_to_element(desktop_drop).click().perform()

    def Macorder(self):
        self.driver.find_element(By.LINK_TEXT,self.a_mac_linktext).click()


    def ClickAddcart(self):
        self.driver.find_element(By.XPATH,self.span_cart_xpath).click()

    def ClickItem(self):
        self.driver.find_element(By.XPATH,self.button_item_xpath).click()

    def Checkout(self):
        self.driver.find_element(By.XPATH,self.a_checkout_xpath).click()


    def ClickOnAddNewAddress(self):
        self.driver.find_element(By.XPATH,self.input_billingaddress_xpath).click()

    def AddFirstname(self,firstname):
        self.driver.find_element(By.ID,self.input_firstname_id).send_keys(firstname)

    def AddLastname(self,lastname):
        self.driver.find_element(By.ID,self.input_lastname_id).send_keys(lastname)

    def AddCompany(self,company):
        self.driver.find_element(By.ID,self.input_company_id).send_keys(company)

    def AddNewAddress(self,address):
        self.driver.find_element(By.ID,self.input_address_id).send_keys(address)

    def AddCity(self,city):
        self.driver.find_element(By.ID,self.input_city_id).send_keys(city)

    def AddPostcode(self,postcode):
        self.driver.find_element(By.ID,self.input_postcode_id).send_keys(postcode)

    def AddCountry(self):
        return self.driver.find_element(By.XPATH,self.select_country_xpath)

    def AddZone(self):
        return self.driver.find_element(By.XPATH,self.select_zone_xpath)

    def SubmitAddressbtn(self):
        self.driver.find_element(By.ID,self.input_paymentaddresssubmitbtn_id).click()


    def DeliveryAddress(self):
        self.driver.find_element(By.XPATH,self.input_deliveryaddress_xpath).click()

    def SelectDeliveryAddress(self):
        deliveraddress=self.driver.find_elements(By.XPATH,self.select_deliveryaddress_xapth)
        return deliveraddress

    def ButtonShippingAddress(self):
        self.driver.find_element(By.XPATH,self.input_shippingaddress_xpath).click()

    def ButtonShippingmethod(self):
        self.driver.find_element(By.XPATH,self.input_shippingmethod_xpath).click()


    def CashonDelivery(self):
        self.driver.find_element(By.XPATH,self.input_cod_xpath).click()
        self.driver.find_element(By.XPATH,self.input_agreebutton_xpath).click()
        self.driver.find_element(By.XPATH,self.input_continuebtn_xpath).click()

    def ConfirmBtn(self):
        self.driver.find_element(By.ID,self.input_confirmbtn_id).click()

    def Myaccount(self):
        self.driver.find_element(By.XPATH,self.a_myaacount_xpath).click()

