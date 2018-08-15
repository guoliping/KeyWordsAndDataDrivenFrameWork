#encoding=utf-8
from configparser import ConfigParser
from config.VarConfig import pageElementLocatorPath
class ParseCofigFile(object):
    def __init__(self):
        self.cf=ConfigParser()#生成解析器
        self.cf.read(pageElementLocatorPath)
    def getItemsSection(self,sectionName):
        #使用self.cf.items(sectionName)此种方法获取到的配置文件中的options内容均被转化成小写
        optionsDict=dict(self.cf.items(sectionName))
        return optionsDict
    def getOptionValue(self,sectionName,optionName):
        value=self.cf.get(sectionName,optionName)
        return value
if __name__ == '__main__':
    pc=ParseCofigFile()
    print(pc.getItemsSection('126mail_login'))
    print(pc.getOptionValue('126mail_login','loginPage.frame'))