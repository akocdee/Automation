from inspect import Parameter
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

class TestApp():
    def __init__(self,parameter) -> None:
        self.parameter = parameter
        
    
    def _click_object(self,obj):
        try:
            element = self.driver.find_element(By.ID, obj)
            element.click()
            print("Clicked: "+obj)
            time.sleep(1) 
            #getResponse()
        except:
            print(obj+" doesn't exist")
    
    def _click_css(self,obj):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, obj)
            element.click()
            print("Clicked(CSS): "+obj)
            time.sleep(1) 
            #getResponse()
        except:
            print(obj+" doesn't exist")

    

    def run(self):
        self.groupiot()
        """
        if loopvar == "normalitem":
            self.normalitem()
        elif loopvar == "normalopt":
            self.normalopt()
        else:
            print("end")
        """

            
    #login
    def login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        customer = self.parameter.get('customer')
        email = customer.get('customer_email')
        password = customer.get('password')
        #Opening URL
        self.driver.get("https://testv7.dsoftonline.com.au/")
        self._click_object('promotional_close')
        self._click_object('login-nav')
        #login
        self.driver.find_element(By.NAME, "email").send_keys(email)
        log_in = self.driver.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)
        print('logged in')
    
    #normal item
    def normalitem(self):
        item = self.parameter.get('normal')
        plu = item.get('plu')
        time.sleep(2)
        self._click_object('promotional_close')
        self._click_object('loyal_close')
        self.driver.find_element(By.CLASS_NAME, "menu-197996").click()
        time.sleep(2)
        #add plu normalitem
        self._click_object('add-'+ plu)
      
    #normal item opt
    def normalopt(self):
        item = self.parameter.get('normalitem')
        plu = item.get('plu')
        menuid = item.get('menuid')
        time.sleep(1)
        self._click_object('promotional_close')
        self._click_object('loyal_close')
        #add plu normalitemopt      
        self.driver.find_element(By.CLASS_NAME, "menu-"+menuid).click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".item-add-popup > #"+plu).click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#add-popup-"+plu+"-"+menuid+" .input-group-radio:nth-child(3) > .input-group-label").click()
        print('Item Option Selected')
        self._click_object(plu)
    
    #size group item optop
    def groupiot(self):
        item = self.parameter.get('sizegroup')
        plu = item.get('plu')
        menuid = item.get('menuid')
        rct = item.get('removeitem')
        adct = item.get('additem')
        grpid = item.get('groupid')
        time.sleep(1)
        self._click_object('promotional_close')
        self._click_object('loyal_close')
        #add plu normalitemopt      
        self.driver.find_element(By.LINK_TEXT, "Traditional Pizzas").click()
        time.sleep(1)
        #input = self.driver.find_element_by_name(grpid)
        self.driver.find_element(By.CSS_SELECTOR, ".item-add-popup > #\\31 88129").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#menu-"+grpid+" > .input-group-radio:nth-child(2) > .input-group-label").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#"+rct+" span:nth-child(2)").click()
        self.driver.find_element(By.LINK_TEXT, "Sauces/Mayo").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".open .extra-row-o:nth-child(1) .extra-toppings-desc").click()
        self._click_object(grpid)

    #checkout
    def checkout(self):
        #checkout
        self._click_object('bt-checkout')
        #select pay in store
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,"div:nth-child(2) > .payment_type_label > img:nth-child(2)").click()
        print("pay in store")
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,"pay"))).click()
        print("Clicked: Pay")
        time.sleep(5)
        self.driver.close()
    
    






#json file
test_case = {
    "customer" : {
        "customer_email" : "sonny@easypos.com.ph",
        "password" : "123456"
    },
    "normal" : {
        "plu": "SID05",
        "menuid": "197996",
    },
    "normalitem" : {
        "plu": "SID25",
        "menuid": "197996"
    },
    "sizegroup" : {
        "plu": "SID25",
        "menuid": "197996",
        "groupid": "188129",
        "removeitem": "T001",
        "additem": "T124"
    }
} 


test = TestApp(test_case)

testcases = ["normalitem", "normalopt"]
test.login()
test.run()
test.checkout()   
#Note: One order each scenario if login and checkout is on
#for x in testcases:
    #test.login()
    #test.run(x)
    #test.checkout()
 