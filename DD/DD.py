from inspect import Parameter
from lib2to3.pgen2 import driver
from pickle import OBJ
import time
import json
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC



class TestDDApp():
    def __init__(self,parameter) -> None:
        self.parameter = parameter
        
    
    def click_object(self,obj):
        try:
            element = self.driver.find_element(By.ID, obj)
            element.click()
            print("Clicked(ID): "+obj)
            time.sleep(1) 
            #getResponse()
        except:
            print(obj+" doesn't exist")
    
    def click_css(self,obj):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, obj)
            element.click()
            print("Clicked(CSS): "+obj)
            time.sleep(1) 
            #getResponse()
        except:
            print(obj+" doesn't exist")

    def click_class(self,obj):
        try:
            element = self.driver.find_element(By.CLASS_NAME, obj)
            element.click()
            print("Clicked(Class): "+obj)
            time.sleep(1) 
            #getResponse()
        except:
            print(obj+" doesn't exist")

    def run(self):
        self.loginfirefox()

    #CHROME
    def loginchrome(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window() 
        # Getting account details on JSON(test_case)
        account = self.parameter.get('account')
        email = account.get('customer_email')
        password = account.get('password')
        #Opening URL
        self.driver.get("https://identity.doordash.com/auth?client_id=1666519390426295040&enable_last_social=false&intl=en-US&layout=consumer_web&prompt=none&redirect_uri=https%3A%2F%2Fwww.doordash.com%2Fpost-login%2F&response_type=code&scope=%2A&state=%2Fstore%2Fdeliverit-test-business-gillen-23484130%2F13787575%2F%7C%7Cab91d155-d158-4ee0-b55f-1416f5b51b35")
        time.sleep(3)
        self.driver.find_element(By.ID, "FieldWrapper-0").send_keys(email)
        self.driver.find_element(By.ID, "FieldWrapper-1").send_keys(password)
        self.click_object("login-submit-button")
        time.sleep(15)

    #EDGE
    def loginedge(self):
        # Instantiate the webdriver with the executable location of MS Edge web driver
        self.driver = webdriver.Edge(r"C:\Users\Admin\Desktop\AppDynamicsJob\msedgedriver.exe")
        # Getting account details on JSON(test_case)
        account = self.parameter.get('account')
        email = account.get('customer_email')
        password = account.get('password')
        #Opening URL
        self.driver.get("https://identity.doordash.com/auth?client_id=1666519390426295040&enable_last_social=false&intl=en-US&layout=consumer_web&prompt=none&redirect_uri=https%3A%2F%2Fwww.doordash.com%2Fpost-login%2F&response_type=code&scope=%2A&state=%2Fstore%2Fdeliverit-test-business-gillen-23484130%2F13787575%2F%7C%7Cab91d155-d158-4ee0-b55f-1416f5b51b35")
        time.sleep(3)
        self.driver.find_element(By.ID, "FieldWrapper-0").send_keys(email)
        self.driver.find_element(By.ID, "FieldWrapper-1").send_keys(password)
        self.click_object("login-submit-button")
        time.sleep(15)

    #FIREFOX
    def loginfirefox(self):
        # Instantiate the webdriver with the executable location of Firefox web driver
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Admin\Desktop\AppDynamicsJob\geckodriver.exe')
        # Getting account details on JSON(test_case)
        account = self.parameter.get('account')
        email = account.get('customer_email')
        password = account.get('password')
        #Opening URL
        self.driver.get("https://identity.doordash.com/auth?client_id=1666519390426295040&enable_last_social=false&intl=en-US&layout=consumer_web&prompt=none&redirect_uri=https%3A%2F%2Fwww.doordash.com%2Fpost-login%2F&response_type=code&scope=%2A&state=%2Fstore%2Fdeliverit-test-business-gillen-23484130%2F13787575%2F%7C%7Cab91d155-d158-4ee0-b55f-1416f5b51b35")
        time.sleep(3)
        self.driver.find_element(By.ID, "FieldWrapper-0").send_keys(email)
        self.driver.find_element(By.ID, "FieldWrapper-1").send_keys(password)
        self.click_object("login-submit-button")
        time.sleep(15)

    #SAFARI??
    def loginsafari(self):
        # Getting account details on JSON(test_case)
        account = self.parameter.get('account')
        email = account.get('customer_email')
        password = account.get('password')
        #Opening URL
        self.driver.get("https://identity.doordash.com/auth?client_id=1666519390426295040&enable_last_social=false&intl=en-US&layout=consumer_web&prompt=none&redirect_uri=https%3A%2F%2Fwww.doordash.com%2Fpost-login%2F&response_type=code&scope=%2A&state=%2Fstore%2Fdeliverit-test-business-gillen-23484130%2F13787575%2F%7C%7Cab91d155-d158-4ee0-b55f-1416f5b51b35")
        time.sleep(3)
        self.driver.find_element(By.ID, "FieldWrapper-0").send_keys(email)
        self.driver.find_element(By.ID, "FieldWrapper-1").send_keys(password)
        self.click_object("login-submit-button")
        time.sleep(15)

    

#json file
test_case = {
    "account" : {
        "customer_email" : "deliverit-aus-testing@doordash.com",
        "password" : "D00rd@$h-deliverit"
    }
}         

test = TestDDApp(test_case)
test.run()