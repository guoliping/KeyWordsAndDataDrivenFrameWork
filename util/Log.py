#- * - coding:UTF-8 - * -
import logging
import logging.config
from config.VarConfig import parentDirPath
logging.config.fileConfig(parentDirPath+r'\\config\\Logger.conf')
logger=logging.getLogger('example02')
def debug(message):
    logger.debug(message)
def info(message):
    logger.info(message)
def warning(message):
    logger.warning(message)
