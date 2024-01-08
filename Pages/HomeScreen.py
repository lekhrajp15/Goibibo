from appium.webdriver.common.mobileby import MobileBy

from Pages.BusBooking import BusBooking
from Pages.FlightBooking import FlightBooking
from Pages.HotelBooking import HotelBooking


class HomeScreen:
    def __init__(self, driver):
        self.driver = driver

    flights = (MobileBy.XPATH, "//*[@content-desc='flights']")
    hotels =  (MobileBy.XPATH, "//*[@content-desc='hotels']")
    bus = (MobileBy.XPATH, "//*[@content-desc='bus']")


    def click_flight(self):
        self.driver.find_element(*HomeScreen.flights).click()
        FB = FlightBooking(self.driver)
        return FB

    def click_hotel(self):
        self.driver.find_element(*HomeScreen.hotels).click()
        HB = HotelBooking(self.driver)
        return HB

    def click_bus(self):
        self.driver.find_element(*HomeScreen.bus).click()
        BB= BusBooking(self.driver)
        return BB



