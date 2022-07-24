import unittest

import pytest

from pages.HotelPage import HotelPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class SearchHotelTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.searchHotelPage = HotelPage(self.driver)

    @pytest.mark.run(order=1)
    def test_openSearchHotelPage(self):
        self.searchHotelPage.clickHotelButton()
        expectedResult = "HOTEL BOOKING"
        actualResult = self.searchHotelPage.getTitlePageText()
        assert actualResult == expectedResult, self.searchHotelPage.takeScreenShot(self.searchHotelPage.driver.current_activity)

    @pytest.mark.run(order=2)
    def test_searchHotel(self):
        self.searchHotelPage.setHotelLocationToJakarta()
        self.searchHotelPage.setCheckinCheckoutDate()
        self.searchHotelPage.setAdultCount()
        expectedResult = "HOTELS IN BANDUNG"
        actualResult = self.searchHotelPage.clickSearchButton()
        assert actualResult == expectedResult, self.searchHotelPage.takeScreenShot(
            self.searchHotelPage.driver.current_activity)
