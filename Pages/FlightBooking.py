import time

from appium.webdriver.common.mobileby import MobileBy
from Utilities.Utilities import readconfigfile


class FlightBooking:
    def __init__(self, driver):
        self.driver = driver

    From_place = (MobileBy.XPATH, "//*[@resource-id='com.goibibo:id/textFlightFromCode']")
    Destn_place = (MobileBy.XPATH, "//*[@resource-id='com.goibibo:id/flightTo']")
    Search_field = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.EditText")
    Search_location= (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.EditText")
    Search_button = (MobileBy.XPATH, "//*[@text='Search']")
    departure_click = (MobileBy.XPATH, "//*[@resource-id ='com.goibibo:id/odate']")
    continue_button = (MobileBy.XPATH, "//*[@text='Continue']")
    # calendar_elements = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.GridView/android.view.ViewGroup")
    return_click = (MobileBy.XPATH, "//*[@resource-id ='com.goibibo:id/textFlightRetDate']")
    calendar_month = (MobileBy.XPATH, "//*[@resource-id='com.goibibo:id/calendar_date_display']")

    def from_place(self):

        #Click From Place
        self.driver.find_element(*FlightBooking.From_place).click()
        from_place = readconfigfile("/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini", "goibibo", "from")
        from_dropdown = readconfigfile("/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini", "goibibo",
                                    "from_dropdown")

        #Searching the city name in the Search Field
        self.driver.find_element(*FlightBooking.Search_field).click()
        self.driver.find_element(*FlightBooking.Search_location).send_keys(from_place)

        #Selecting the particular city from the dropdown search result
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                            value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("'+from_dropdown+'").instance(0))').click()
        time.sleep(2)

        #Click on Destination Field in the Search Field
        self.driver.find_element(*FlightBooking.Destn_place).click()
        destination_place = readconfigfile("/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini", "goibibo", "destination")
        destn_dropdown = readconfigfile("/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini", "goibibo",
                                    "destn_dropdown")

        # Searching the destination city in the Search Field
        self.driver.find_element(*FlightBooking.Search_location).send_keys(destination_place)
        # Selecting the destination city from the dropdown search result
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("' + destn_dropdown + '").instance(0))').click()
        time.sleep(2)

        #Click on Departure Date field
        self.driver.find_element(*FlightBooking.departure_click).click()
        dep_date = readconfigfile('/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini', 'goibibo',
                                  'departure_date')
        dep_month = readconfigfile('/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini', 'goibibo',
                                   'departure_month')

        for i in range(0, 11):
            value = self.driver.find_element(*FlightBooking.calendar_month).text
            print(value)
            if value != str(dep_month):
                self.driver.swipe(380,1050,370,620,1000)
            else:
                break

        self.driver.find_element(MobileBy.XPATH, "//*[@text='"+dep_date+"']").click()
        self.driver.find_element(*FlightBooking.continue_button).click()

        # Click on Return Date field
        self.driver.find_element(*FlightBooking.return_click).click()
        return_date = readconfigfile('/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini', 'goibibo',
                                  'return_date')
        return_month = readconfigfile('/Users/lekhraj/PycharmProjects/AppiumFramework/TestData/config.ini', 'goibibo',
                                   'return_month')

        for i in range(0, 11):
            value = self.driver.find_element(*FlightBooking.calendar_month).text
            print(value)
            if value != str(return_month):
                self.driver.swipe(380,1123,370,620,1000)
            else:
                break

        self.driver.find_element(MobileBy.XPATH, "//*[@text='"+return_date+"']").click()
        self.driver.find_element(*FlightBooking.continue_button).click()
        self.driver.find_element(*FlightBooking.Search_button).click()
        time.sleep(10)







