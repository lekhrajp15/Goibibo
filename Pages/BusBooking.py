import time

from appium.webdriver.common.mobileby import MobileBy

from Utilities.Utilities import readconfigfile


class BusBooking:

    def __init__(self,driver):
        self.driver = driver

    from_place = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='FromTextField']/android.widget.TextView[2]")
    dep_search_field = (MobileBy.XPATH, "//*[@text='Departure city/ bus stop']")
    arrival_search_field = (MobileBy.XPATH, "//*[@text='Arrival city/ bus stop']")

    to_place = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='ToTextField']/android.widget.TextView[2]")
    depart_click = (MobileBy.XPATH, "//*[@content-desc ='DepartDate']")
    search_bus_click = (MobileBy.XPATH, "//*[@text='SEARCH BUSES']")
    calendar_month = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]")

    def bus_booking(self):
        self.driver.find_element(*BusBooking.from_place).click()
        from_place = readconfigfile("/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini", "goibibo",
                                    "from")
        from_dropdown = readconfigfile("/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini", "goibibo",
                                       "from_dropdown")

        self.driver.find_element(*BusBooking.dep_search_field).click()
        self.driver.find_element(*BusBooking.dep_search_field).send_keys(from_place)


        # Selecting the particular city from the dropdown search result
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("' + from_dropdown + '").instance(0))').click()
        time.sleep(2)

        # Click on Destination Field in the Search Field
        self.driver.find_element(*BusBooking.to_place).click()
        destination_place = readconfigfile("/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini",
                                           "goibibo", "destination")
        destn_dropdown = readconfigfile("/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini", "goibibo",
                                        "destn_dropdown")

        # Searching the destination city in the Search Field
        # self.driver.find_element(*BusBooking.arrival_search_field).click()
        self.driver.find_element(*BusBooking.arrival_search_field).send_keys(destination_place)
        # Selecting the destination city from the dropdown search result
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("' + destn_dropdown + '").instance(0))').click()
        time.sleep(2)


        #  Click on Departure Date field
        self.driver.find_element(*BusBooking.depart_click).click()
        dep_date = readconfigfile('/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini', 'goibibo',
                                  'departure_date')
        dep_month = readconfigfile('/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini', 'goibibo',
                                   'departure_month')

        for i in range(0, 11):
            value = self.driver.find_element(*BusBooking.calendar_month).text
            print(value)
            if value != str(dep_month):
                self.driver.swipe(380,1050,370,620,1000)
            else:
                break

        self.driver.find_element(MobileBy.XPATH, "//*[@text='"+dep_date+"']").click()


        self.driver.find_element(*BusBooking.search_bus_click).click()
