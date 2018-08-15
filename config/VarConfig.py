#encoding=utf-8
import  os
#当前文件所在目录的绝对路径
parentDirPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath=parentDirPath+u'\\config\\PagElementLocator.ini'
#126邮箱数据文件的绝对路径
dataFilePath=parentDirPath+u'\\testData\\126邮箱联系人.xlsx'
webCasePath=parentDirPath+u'\\testScripts'
reportPath=parentDirPath+u'\\report\\report.html'
account_username=2
account_password=3
account_dataBook=4
account_isExcute=5
account_testResult=6

contacts_contactPersonName=2
contacts_contactPersonEmail=3
contacts_isStar=4
contacts_contactPersonMobile=5
contacts_contactPersonComment=6
contacts_assertKeyWords=7
contacts_isExecute=8
contacts_runTime=9
contacts_testResult=10
