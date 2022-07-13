#from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def document_initialised(driver):
    return driver.execute_script("return initialised")

def clickObject(self,obj):
    try:
      element = driver.find_element(By.ID, obj)
      element.click()
      print("Clicked: "+obj)
      time.sleep(1) 
      #getResponse()
    except:
      print(obj+" doesn't exist")
    
def getResponse():
    for request in driver.requests:
        if request.response:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )

#Opening URL
driver.get("https://testv7.dsoftonline.com.au/")

clickObject('promotional_close')
clickObject('login-nav')

#login
driver.find_element(By.NAME, "email").send_keys("0412969140")
log_in = driver.find_element(By.NAME, "password").send_keys("326435@Dc" + Keys.ENTER)
print('logged in')

time.sleep(2)
clickObject('promotional_close')
clickObject('loyal_close')

driver.find_element(By.CLASS_NAME, "menu-197996").click()
time.sleep(1)

clickObject('add-SID05')
clickObject('bt-checkout')

driver.find_element(By.CSS_SELECTOR,"div:nth-child(2) > .payment_type_label > img:nth-child(2)").click()
clickObject('pay')

driver.close()

