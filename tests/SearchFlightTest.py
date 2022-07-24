import unittest

import pytest

from pages.FlightPage import FlightPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class SearchFlightTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.searchFlightPage = FlightPage(self.driver)

    def test_openSearchFlightPage(self):
        self.searchFlightPage.clickFlightButton()
        expectedResult = "FLIGHT BOOKING"
        actualResult = self.searchFlightPage.getTitlePageText()
        assert actualResult == expectedResult, self.searchFlightPage.takeScreenShot(
            self.searchFlightPage.driver.current_activity)

    def test_searchFlight(self):
        self.searchFlightPage.setAsal()
        self.searchFlightPage.setTujuan()
        self.searchFlightPage.setTanggalBerangkat()
        self.searchFlightPage.setJumlahPenumpang()
        expectedResult = "CGK to DPS"
        actualResult = self.searchFlightPage.clickSearchButton()
        assert actualResult == expectedResult, self.searchFlightPage.takeScreenShot(
            self.searchFlightPage.driver.current_activity)
