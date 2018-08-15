#coding=utf-8
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import time
import traceback
class AddContactPerson(object):
    def __init__(self):
        print('add contact person.')
    @staticmethod
    def add(driver,contactName,contactEmail,isStar,contactPhone,contactComment):
        try:
            hp=HomePage(driver)
            hp.addressLink().click()
            time.sleep(2)
            apb=AddressBookPage(driver)
            apb.createContactPersonButton().click()
            if contactName:
                apb.contactPersonName().send_keys(contactName)
                apb.contactPersonEmail().send_keys(contactEmail)
                if isStar==u'是':
                    apb.starContacts().click()
                if contactPhone:
                    apb.contactPersonMobile().send_keys(contactPhone)
                if contactComment:
                    apb.contactPersonComment().send_keys(contactComment)
                apb.savecontactPerson().click()
        except Exception as e:
            print(traceback.print_exc())
            raise e
if __name__ == '__main__':
    from appModules.LoginAction import LoginAction
    import time
    from selenium import webdriver
    driver=webdriver.Firefox()
    url='http://mail.126.com'
    driver.get(url)
    time.sleep(2)
    LoginAction.login(driver,'xiyang198803','guoliping1988')
    AddContactPerson.add(driver,'zhangsan','zhangshan@126.com',u'是','13436202365',u'我是测试')
    time.sleep(3)
    assert 'zhangsan' in driver.page_source
    time.sleep(3)
    driver.quit()

