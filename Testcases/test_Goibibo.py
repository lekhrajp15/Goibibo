import time

import pytest

from Pages.HomeScreen import HomeScreen
from Utilities.BaseClass import BaseClass


class TestGoibibo(BaseClass):


    @pytest.mark.usefixtures('appiumdriver')
    def test_BookFlight(self):
        log = self.getlog()
        log.info("Testcase: Flight Booking")
        Home_Screen = HomeScreen(self.driver)
        Flight_Booking = Home_Screen.click_flight()
        Flight_Booking.from_place()
        log.info("Testcase: Flight Booking")

    @pytest.mark.usefixtures('appiumdriver')
    def test_BookHotel(self):
        log = self.getlog()
        log.info("Testcase: Hotel Booking")
        Home_Screen=  HomeScreen(self.driver)
        Hotel_Booking = Home_Screen.click_hotel()
        Hotel_Booking.book_hotel()
        log.info("Testcase: Hotel Booking")


