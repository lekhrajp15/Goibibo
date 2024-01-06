from appium.webdriver.common.mobileby import MobileBy
from Pages.FlightBooking import FlightBooking
from Pages.HotelBooking import HotelBooking


class HomeScreen:
    def __init__(self, driver):
        self.driver = driver

    flights = (MobileBy.XPATH, "//*[@content-desc='flights']")
    hotels =  (MobileBy.XPATH, "//*[@content-desc='hotels']")


    def click_flight(self):
        self.driver.find_element(*HomeScreen.flights).click()
        FB = FlightBooking(self.driver)
        return FB

    def click_hotel(self):
        self.driver.find_element(*HomeScreen.hotels).click()
        HB = HotelBooking(self.driver)
        return HB



