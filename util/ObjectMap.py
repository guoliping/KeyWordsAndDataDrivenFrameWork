#coding=utf-8
from  selenium.webdriver.support.ui import WebDriverWait
#获取单个页面元素对象
def getElement(driver,locateType,locatorExpression):
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e
#获取多个页面元素对象，以list返回
def getElements(driver,locateTye,locatorExpression):
    try:
        elements=WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locateTye,value=locatorExpression))
        return elements
    except Exception as e:
         raise  e
if __name__ == '__main__':
    from selenium import webdriver
    driver=webdriver.Firefox()
    url="http://baidu.com"
    driver.get(url)
    serchBox=getElement(driver,'id','kw')
    print(serchBox.tag_name)
    aList=getElements(driver,'tag name','a')
    print(len(aList))
    driver.quit()

