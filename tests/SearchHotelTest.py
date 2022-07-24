import unittest

import pytest

from pages.HotelPage import HotelPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class SearchHotelTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.searchHotelPage = HotelPage(self.driver)

    def test_openSearchHotelPage(self):
        self.searchHotelPage.clickHotelButton()
        expectedResult = "HOTEL BOOKING"
        actualResult = self.searchHotelPage.getTitlePageText()
        assert actualResult == expectedResult, self.searchHotelPage.takeScreenShot(self.searchHotelPage.driver.current_activity)
