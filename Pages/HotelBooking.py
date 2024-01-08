import time

from appium.webdriver.common.mobileby import MobileBy
from Utilities.Utilities import readconfigfile


class HotelBooking:
    def __init__(self, driver):
        self.driver = driver


    Hotel_name = (MobileBy.XPATH, "//*[@resource-id='com.goibibo:id/txtPlaceName']")
    Search_hotel = (MobileBy.XPATH, "//*[@class='android.widget.EditText']")
    Search_button = (MobileBy.XPATH, "//*[@text='Search']")
    calendarfield = (MobileBy.XPATH, "//*[@resource-id = 'com.goibibo:id/lytCalendarClick']")
    Calendar_continue_btn = (MobileBy.XPATH, "//*[contains(@text, 'Continue For')]")
    calendar_month = (MobileBy.XPATH, "//*[@resource-id='com.goibibo:id/tvMonthName']")


    def book_hotel(self):
        self.driver.find_element(*HotelBooking.Hotel_name).click()
        hotelname = readconfigfile('/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini', 'goibibo', 'Hotelname')
        time.sleep(3)
        self.driver.find_element(*HotelBooking.Search_hotel).click()
        self.driver.find_element(*HotelBooking.Search_hotel).send_keys(hotelname)
        time.sleep(3)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Mumbai").instance(0))').click()
        self.driver.find_element(*HotelBooking.Search_button).click()



