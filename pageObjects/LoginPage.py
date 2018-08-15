#encoding=utf-8
from util.ObjectMap import  *
from util.ParseConfigurationFile import ParseCofigFile
import time
class LoginPage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF=ParseCofigFile()
        self.loginOptions=self.parseCF.getItemsSection('126mail_login')
        print(self.loginOptions)
        #self.wait=WebDriverWait(self.driver,10,0.2)#显示等待
    #跳入frame
    def switchToFrame(self):
        try:
            locatorExpression=self.loginOptions\
            ['loginPage.frame'.lower()].split('>')[1]
            self.driver.switch_to.frame(locatorExpression)
        except Exception as e:
            raise e
    #跳出frame58
    def switchToDefaultFrame(self):

        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise  e


    def userNameObj(self):
        try:
            #获取登录页面的用户名输入框页面对象，并返回给调用者
            locateType,locatorExpression=self.loginOptions\
            ['loginPage.username'.lower()].split('>')
            elementObj=getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            locateType, locatorExpression = self.loginOptions \
                ['loginPage.password'.lower()].split('>')
            elementObj=getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def loginButton(self):
        try:
            locateType, locatorExpression = self.loginOptions \
                ['loginPage.loginbutton'.lower()].split('>')
            elementObj=getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
if __name__ == '__main__':

    from selenium import  webdriver
    driver=webdriver.Firefox()
    url="https://mail.126.com/"
    driver.get(url)
    import sys

    print(sys.getfilesystemencoding())

    login=LoginPage(driver)
    time.sleep(3)

    login.switchToFrame()
    login.userNameObj().send_keys("xiyang198803")
    login.passwordObj().send_keys("guoliping1988")
    login.loginButton().click()
    time.sleep(2)
    assert u'未读邮件' in driver.page_source
    driver.quit()
