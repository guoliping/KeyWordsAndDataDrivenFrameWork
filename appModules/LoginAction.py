#coding=utf-8
from pageObjects.LoginPage import LoginPage
from selenium import  webdriver
import time
class LoginAction(object):
    def __init__(self,driver,username,password):
        driver=self.driver
        username=self.username
        password=self.password
        print('Login...')
    @staticmethod
    def login(driver,username,password):
        try:
            login=LoginPage(driver)
            time.sleep(2)
            login.switchToFrame()
            time.sleep(2)
            login.userNameObj().send_keys(username)
            login.passwordObj().send_keys(password)
            login.loginButton().click()
            #login.switchToDefaultFrame()
            time.sleep(2)
            assert u'未读邮件' in driver.page_source
        except Exception as  e:
            raise e
if __name__ == '__main__':
    from pageObjects.LoginPage import LoginPage
    from selenium  import  webdriver
    driver=webdriver.Firefox()
    url="http://mail.126.com"
    driver.get(url)
    LoginAction.login(driver,'xiyang198803','guoliping1988')
    time.sleep(2)
    driver.find_element_by_xpath("//div[text()='通讯录']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[text()='新建联系人']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[text()='确 定']").click()





