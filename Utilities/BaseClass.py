import inspect
import logging

import pytest
from appium.webdriver.common.mobileby import MobileBy


@pytest.mark.usefixtures("appiumdriver")
class BaseClass:

    def getlog(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('/Users/lekhraj/PycharmProjects/AppiumFramework/Logs/logfile.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s:%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def scrollIntoView(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("' + text + '").instance(0))').click()

