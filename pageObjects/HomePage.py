#encoding=utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseCofigFile
from appModules.LoginAction import  LoginAction
class HomePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF=ParseCofigFile()
        self.loginOptions = self.parseCF.getItemsSection('126mail_homePage')
        print(self.loginOptions)
    def addressLink(self):
        try:
            locateType, locatorExpression = self.loginOptions \
                ['homepage.addressbook'.lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Firefox()

    url = "http://mail.126.com"
    driver.get(url)
    LoginAction.login(driver, 'xiyang198803', 'guoliping1988')
    driver.refresh()
    hp = HomePage(driver)
    hp.addressLink().click()




