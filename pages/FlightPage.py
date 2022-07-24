from base.BasePage import BasePage
import utilities.CustomLogger as cl


class FlightPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _flightButton = "com.nusatrip.android:id/flightButton"
    _titleText = "com.nusatrip.android:id/titletext"

    _asal = "com.nusatrip.android:id/departureCodeLayout"
    _tujuan = "com.nusatrip.android:id/arrivalCodeLayout"

    _jakarta = "Jakarta (CGK)"
    _denpasar = "Denpasar (DPS)"

    _tanggalBerangkat = "com.nusatrip.android:id/departingDateLayout"
    _inputTanggal = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView[4]"
    _doneButton = "com.nusatrip.android:id/done"

    _jumlahPenumpang = "com.nusatrip.android:id/PassengerLayout"
    _adultCount = "com.nusatrip.android:id/adultsCount"
    _two = "com.nusatrip.android:id/two"

    _searchButton = "com.nusatrip.android:id/search_flight"
    _codeAsal = "com.nusatrip.android:id/departairport"
    _codeTujuan = "com.nusatrip.android:id/arrivalCode"

    def clickFlightButton(self):
        self.clickElement(self._flightButton, "id")
        cl.allureLogs("Click on Flight Button")

    def getTitlePageText(self):
        element = self.getElement(self._titleText, "id")
        cl.allureLogs("Get page title text: " + element.text)
        return element.text

    def setAsal(self):
        self.clickElement(self._asal, "id")
        self.clickElement(self._jakarta, "text")
        cl.allureLogs("Set asal penerbangan")

    def setTujuan(self):
        self.clickElement(self._tujuan, "id")
        self.clickElement(self._denpasar, "text")
        cl.allureLogs("Set tujuan penerbangan")

    def setTanggalBerangkat(self):
        self.clickElement(self._tanggalBerangkat, "id")
        self.clickElement(self._inputTanggal, "xpath")
        cl.allureLogs("Set tanggal penerbangan")

    def setJumlahPenumpang(self):
        self.clickElement(self._jumlahPenumpang, "id")
        self.clickElement(self._adultCount, "id")
        self.clickElement(self._two, "id")
        self.clickElement(self._doneButton)
        cl.allureLogs("Set jumlah penumpang dewasa")

    def clickSearchButton(self):
        self.clickElement(self._searchButton, "id")
        elementAsal = self.getElement(self._codeAsal, "id")
        elementTujuan = self.getElement(self._codeTujuan, "id")
        cl.allureLogs("Get rute : " + elementAsal.text + ' - ' + elementTujuan.text)
        return elementAsal.text + ' to ' + elementTujuan.text
