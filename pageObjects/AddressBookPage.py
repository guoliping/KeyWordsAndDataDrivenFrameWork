#encoding=utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseCofigFile
class AddressBookPage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF=ParseCofigFile()
        self.addContacsOptions=self.parseCF.getItemsSection("126mail_addContactsPage")
        print(self.addContacsOptions)
    def createContactPersonButton(self):
        try:
            locateType,locatorExpression=self.addContacsOptions\
            ['addContactsPage.createContactsBtn'.lower()].split('>')
            elementObj=getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def contactPersonName(self):
        try:
            locateType, locatorExpression = self.addContacsOptions \
            ['addContactsPage.contactPersonName'.lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def contactPersonEmail(self):
        try:
            locateType, locatorExpression = self.addContacsOptions \
                ['addContactsPage.contactPersonEmail'.lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def starContacts(self):
        try:
            locateType, locatorExpression = self.addContacsOptions \
                ['addContactsPage.starContacts'.lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def contactPersonMobile(self):
        try:
            locateType, locatorExpression = self.addContacsOptions \
                ['addContactsPage.contactPersonMobile'.lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def contactPersonComment(self):
        try:
            locateType, locatorExpression = self.addContacsOptions \
                ['addContactsPage.contactPersonComment'.lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def savecontactPerson(self):
        try:
            locateType, locatorExpression = self.addContacsOptions \
                ['addContactsPage.savecontactPerson'.lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e





