#coding=utf-8
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from util.ParseExcel import  ParseExcel
from config.VarConfig import *
from appModules.LoginAction import LoginAction
from  appModules.AddContactPersonAction import AddContactPerson
import traceback
import time
import logging
import unittest
logging.basicConfig(level=logging.INFO,
                    #输出格式
                    format='%(asctime)s %(filename)s[line:%(lineno)d)]%(levelname)s %(message)s',
                    #日期格式
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    #输出日志
                    filename='H:\\DataDrivenFrameWork\\log\\report.log',
                    filemode='w')
excelObj=ParseExcel()
excelObj.loadWorkBook(dataFilePath)


def LaunchBrowser():
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path='G:\Python\Scripts\chromedriver', chrome_options=chrome_options)
    driver.get("http://mail.126.com")
    time.sleep(2)
    return driver


def test126MailAddContacts():
        logging.info(u'126邮箱添加联系人的数据驱动测试开始。。。')
        try:
            userSheet=excelObj.getSheetByName(u'126账号')
            #获取126账号表格中的是否执行列
            isExecuteUser=excelObj.getColumn(userSheet,account_isExcute)
            #获取数据表那一列
            dataBookColumn=excelObj.getColumn(userSheet,account_dataBook)
            print(u'测试为126邮箱添加联系人执行开始')
            #取到是否执行那一列的所有内容
            for idx,i in enumerate(isExecuteUser[1:]):
                if i.value=='y':
                    #idx是从0开始，真实数据需要到第二行才是，取到的是第i行的内容
                    userRow=excelObj.getRow(userSheet,idx+2)
                    #第i行的用户名
                    username=userRow[account_username-1].value
                    #第i行的密码
                    password=str(userRow[account_password-1].value)
                    print(username,password)
                    driver=LaunchBrowser()
                    logging.info(u'启动浏览器，访问126邮箱主页')
                    LoginAction.login(driver,username,password)
                    time.sleep(2)
                    try:
                        assert u'收信' in driver.page_source
                        logging.info(u'用户%s登陆后，断言页面关键字“收信”成功'%username)
                    except AssertionError as e:
                        logging.debug(u'用户%s登录后，断言页面关键字“收信”失败' u'异常信息：%s'%(username,str(traceback.format_exc())))
                    dataBookName=dataBookColumn[idx+1].value
                    dataSheet=excelObj.getSheetByName(dataBookName)
                    isExecuteData=excelObj.getColumn(dataSheet,contacts_isExecute)
                    contactNum=0
                    isExecuteNum=0
                    for id,data in enumerate(isExecuteData[1:]):
                        if data.value=='y':
                            isExecuteNum+=1
                            rowContent=excelObj.getRow(dataSheet,id+2)
                            contactPersonName=rowContent[contacts_contactPersonName-1].value
                            contactPersonEmail=rowContent[contacts_contactPersonEmail-1].value
                            contactPersonPhone=rowContent[contacts_contactPersonMobile-1].value
                            isStar=rowContent[contacts_isStar-1].value
                            contactPersonComment=rowContent[contacts_contactPersonComment-1].value
                            assertKeyWord=rowContent[contacts_assertKeyWords-1].value
                            print(contactPersonName,contactPersonEmail,assertKeyWord)
                            print(contactPersonPhone,contactPersonComment,isStar)
                            AddContactPerson.add(driver,contactPersonName,
                                                 contactPersonEmail,
                                                 isStar,
                                                 contactPersonPhone,
                                                 contactPersonComment)
                            time.sleep(2)
                            logging.info(u'添加联系人%s成功'%contactPersonEmail)
                            excelObj.writeCellCurrnetTime(dataSheet,rowNo=id+2,colsNo=contacts_runTime)
                            try:
                                assert assertKeyWord in driver.page_source
                            except AssertionError as e:
                                excelObj.writeCell(dataSheet,"faild",rowNo=id+2,colsNo=contacts_testResult,style="red")
                                logging.info(u'断言关键字%s失败'%assertKeyWord)
                            else:
                                excelObj.writeCell(dataSheet,"pass",rowNo=id+2,colsNo=contacts_testResult,style="green")
                                contactNum+=1
                                logging.info(u'断言关键字%s成功'%assertKeyWord)
                        print("contactNum=%s,isExecuteNum=%s" %(contactNum,isExecuteNum))
                        if contactNum==isExecuteNum:
                            excelObj.writeCell(userSheet,'pass',rowNo=idx+2,colsNo=account_testResult,style='green')
                            print(u"为用户%s添加%d个联系人，测试通过！" %(username,contactNum))
                            logging.info(u"为用户%s添加%d个联系人，测试通过！" %(username,contactNum))
                        else:
                            excelObj.writeCell(userSheet,'faild',rowNo=idx+2,colsNo=account_testResult,style='red')
                elif i.value=='n':
                    print("u用户%s被设置为忽略执行！"%excelObj.getCellOfValue(userSheet,rowNo=idx+2,colsNo=account_username))
                    logging.info((u'联系人%s被忽略执行'%contactPersonEmail))
                else:
                    print(u'执行完毕')
                #driver.quit()
        except Exception as e:
            print(u'数据驱动框架助程序发生异常，异常信息为：')
            logging.debug(u'数据驱动框架助程序发生异常，异常信息为：%s'%str(traceback.format_exc()))

if __name__ == '__main__':
    test126MailAddContacts()
    print(u'登录126邮箱成功')








