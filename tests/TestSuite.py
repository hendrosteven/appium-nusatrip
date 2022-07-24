import unittest
from tests.SearchFlightTest import SearchFlightTest
from tests.SearchHotelTest import SearchHotelTest

searchHotelTest = unittest.TestLoader().loadTestsFromTestCase(SearchHotelTest)
searchFlightTest = unittest.TestLoader().loadTestsFromTestCase(SearchFlightTest)

testSuite = unittest.TestSuite([searchHotelTest, searchFlightTest])

unittest.TextTestRunner(verbosity=1).run(testSuite)