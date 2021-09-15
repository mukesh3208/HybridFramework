import logging
import time
from _overlapped import NULL
from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait

import conftest
from testResources import constants


class genKeywords:
    def __init__(self):
        self.prop = conftest.prod
        self.envProp= conftest.envProp
        self.driver = NULL
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def set_ObjectKey(self,OK):
        self.objectKey = OK
    def set_dataKey(self, DK):
        self.dataKey = DK
    def set_testData(self, testData):
        self.data= testData

    def openBrowser(self):

        browsername=self.data[self.dataKey]
        if(self.prop['GridRun']=='Y'):
            if (browsername == constants.CHROME):
                caps = DesiredCapabilities.CHROME.copy()
                caps['browserName']='chrome'
                caps['javascriptEnabled']=True
            elif(browsername==constants.FIREFOX):
                caps = DesiredCapabilities.FIREFOX.copy()
                caps['browserName']='firefox'
                caps['javascriptEnabled']=True
            try:
                self.driver=webdriver.Remote(desired_capabilities=caps, command_executor='http://192.168.189.1:4444/wd/hub')
            except Exception as e:
                print(e)


        else:
            with allure.step("Opening Browser - "+str(browsername)):
                if(browsername==constants.CHROME):
                    self.logging("Opening "+browsername+" Browser")
                    options = webdriver.ChromeOptions()
                    options.add_argument("--disable-infobars")
                    options.add_argument("--disable-notifications")
                    options.add_argument("--start-maximized")
                    self.driver = webdriver.Chrome(options=options)
                elif(browsername==constants.FIREFOX):
                    self.logging("Opening " + browsername + " Browser")
                    # fp = webdriver.FirefoxProfile("C:\\Users\\kumarmu\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
                    # fp.set_preference("dom.webnotification.enabled", False)
                    self.driver = webdriver.Firefox()
                else:
                    self.logging("Opening default Chrome Browser")
                    self.driver = webdriver.Chrome()
                self.logging("Maximizing browser window")
                self.driver.maximize_window()
                self.driver.implicitly_wait(5)
                self.reportSuccess("Browser -"+browsername+" opened and maximized successfully")

    def navigate(self):
        url = self.prop[self.objectKey]
        with allure.step("Navigate to URL - "+str(url)):
            self.logging("Navigate to url - "+str(url))
            self.driver.get(url)
            self.reportSuccess("Navigated to url - "+str(url)+" successfully")

    def type(self):
        with allure.step("Typing data - "+str(self.data[self.dataKey])+" in element - "+str(self.objectKey)):
            self.logging("Typing data - "+str(self.data[self.dataKey])+" in element - "+str(self.objectKey))
            self.getElement(self.objectKey).send_keys(self.data[self.dataKey])
            self.reportSuccess("Typed "+self.data[self.dataKey]+" in "+str(self.objectKey)+" successfully")

    def typing(self, arg1, arg2):
        with allure.step("Typing in - "+arg1+" with - "+arg2):
            self.getElement(arg1).send_keys(arg2)
            self.reportSuccess("Typed in successfully")



    def Click(self, parameter=None):
        with allure.step("Clicking on element "+str(self.objectKey)):
            if(parameter==None):
                if(self.getElement(self.objectKey)):
                    self.logging("Clicking on element "+str(self.objectKey))
                    self.getElement(self.objectKey).click()
                    self.reportSuccess("Clicked on " + self.objectKey + " successfully")
                else:
                    self.reportFailure("Element to be clicked"+self.objectKey+ " is not found")
            else:
                if(self.getElement(parameter)):
                    self.getElement(parameter).click()
                else:
                    self.reportFailure("Element to be clicked "+parameter+" not found")

    def closeApp(self):
        if(self.driver!=NULL):
            with allure.step("Closing browser"):
                self.logging(("Closing browser"))
                self.driver.quit()
                self.reportSuccess("Browser closed successfully")

#common utility functions
    def waitForPageToBeLoaded(self):
        i=1
        while(i!=10):
            load_status = self.driver.execute_script("return document.readyState")
            try:
                if(load_status=='complete'):
                    break
                else:
                    time.sleep(2)
                    self.logging("Waiting for page to be loaded")
            except Exception as e:
                self.reportFailure("Failed to load the page, load status of page is -"+str(load_status))

    def isElementPresent(self, locator):
        wait = WebDriverWait(self.driver, 20)
        elementList=[]
        obj = self.envProp[locator]
        self.waitForPageToBeLoaded()
        if (locator.endswith('_xpath')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.XPATH, obj)))
        elif (locator.endswith('_id')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.ID, obj)))
        elif (locator.endswith('_name')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.NAME, obj)))
        elif (locator.endswith('_cssSelectror')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, obj)))
        else:
            elementList = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, obj)))
        if(len(elementList)==0):
            self.reportFailure("The Element -"+str(locator)+" is not present")
        else:
            return True

    def isElementVisible(self, locator):
        wait = WebDriverWait(self.driver, 20)
        elementList = []
        obj = self.envProp[locator]
        self.waitForPageToBeLoaded()
        if (locator.endswith('_xpath')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.XPATH, obj)))
        elif (locator.endswith('_id')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.ID, obj)))
        elif (locator.endswith('_name')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.NAME, obj)))
        elif (locator.endswith('_cssSelector')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, obj)))
        else:
            elementList = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, obj)))
        if (len(elementList) == 0):
            self.reportFailure("The Element - "+str(locator)+" is not visible")
        else:
            return True

    def getElement(self, locator):
        obj = self.envProp[locator]
        element=NULL
        print("Locator is "+str(locator))
        print("Object is "+str(obj))
        if(self.isElementVisible(locator) and self.isElementPresent(locator)):
            try:
                if (locator.endswith('_xpath')):
                    element= self.driver.find_element_by_xpath(obj)
                elif (locator.endswith('_id')):
                    element= self.driver.find_element_by_id(obj)
                elif (locator.endswith('_name')):
                    element= self.driver.find_element_by_name(obj)
                elif (locator.endswith('_cssSelector')):
                    element= self.driver.find_element_by_css_selector(obj)
                elif(locator.endswith('_className')):
                    element = self.driver.find_element_by_class_name(obj)
                else:
                    return False
                return element
            except Exception:
                return False
        else:
            self.reportFailure("The Element - "+str(locator)+" is not visible or present")

    def takeScreenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "Screenshot taken at : "+str(datetime.now()), AttachmentType.PNG)
        self.logging("Screenshot taken at : "+str(datetime.now()))

    def reportFailure(self, message):
        self.takeScreenshot()
        self.logging(message)
        with allure.step(message):
            assert False, message

    def reportSuccess(self, message):
        self.logging(message)
        with allure.step(message):
            assert True

    def logging(self, message):
        self.logger.info(message)

    def wait(self):
        time.sleep(5)

    def selectDate(self):
        pass
        # with allure.step("Selecting date: "+self.data['ClosingDate']):
        #     date = self.data['ClosingDate']
        #     dt = datetime.strptime(date, "%d-%m-%Y")
        #     year = dt.year
        #     month = dt.strftime("%B")
        #     day = dt.day
        #     desired_date=month+" "+str(year)
        #     print(desired_date)



    # Application specific functions
    def validateTitle(self):
        print("In validate title")
        with allure.step("Validating Url Title..."):
            expectedTitle = self.envProp[self.objectKey]
            actualTitle = self.driver.title
            if(expectedTitle==actualTitle):
                self.reportSuccess("Title validation successful")
            else:
                self.reportFailure("Title validation failed...Got title as "+actualTitle+" instead of "+expectedTitle)

    def validateLogin(self):
        with allure.step("Validate Login...."):
            element = self.getElement(self.objectKey)
            if(element.is_displayed() and self.data[self.dataKey]=='Success'):
                self.reportSuccess("Login Successful")
            else:
                self.reportFailure("Login Failed")

    def doLogin(self):
        with allure.step("Log In"):
            self.typing("usernameTextBox_id",self.prop['defaultUsername'])
            self.typing("passwordTextBox_id", self.prop['defaultPassword'])
            self.Click("submitBtn_id")

    def acceptingAlert(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present)
        a = self.driver.switch_to.alert()
        print(a.text)
        a.accept()
        self.driver.switch_to.default_content()








