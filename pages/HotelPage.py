from base.BasePage import BasePage
import utilities.CustomLogger as cl


class HotelPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _hotelButton = "com.nusatrip.android:id/hotelButton"
    _titleText = "com.nusatrip.android:id/titletext"

    _hotelLocation = "com.nusatrip.android:id/searchHotelLocationText"
    _textJakarta = "Jakarta"
    _checkinDate = "com.nusatrip.android:id/checkInDateLayout"
    _startDate = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[3]"
    _endDate = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[5]"
    _doneButton = "com.nusatrip.android:id/done"
    _adultCount = "com.nusatrip.android:id/adultsCount"
    _one = "com.nusatrip.android:id/one"
    _searchButton = "com.nusatrip.android:id/search_hotel"

    def clickHotelButton(self):
        self.clickElement(self._hotelButton, "id")
        cl.allureLogs("Click on Hotel Button")

    def getTitlePageText(self):
        element = self.getElement(self._titleText, "id")
        cl.allureLogs("Get page title text: " + element.text)
        return element.text

    def setHotelLocationToJakarta(self):
        self.clickElement(self._hotelLocation, "id")
        self.clickElement(self._textJakarta, "text")
        cl.allureLogs("Set Hotel Location Jakarta")

    def setCheckinCheckoutDate(self):
        self.clickElement(self._checkinDate, "id")
        self.clickElement(self._startDate, "xpath")
        self.clickElement(self._endDate, "xpath")
        self.clickElement(self._doneButton, "id")
        cl.allureLogs("Set Checkin & Checkout Date")

    def setAdultCount(self):
        self.clickElement(self._adultCount, "id")
        self.clickElement(self._one, "id")
        cl.allureLogs("Set Adult count to one")

    def clickSearchButton(self):
        self.clickElement(self._searchButton, "id")
        cl.allureLogs("Click on Search Hotel Button")
        element = self.getElement(self._titleText, "id")
        cl.allureLogs("Get Title Search Result: "+ element.text)
        return element.text

