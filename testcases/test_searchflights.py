import pytest
import softest

from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt,data,unpack,file_data

"""
Manual steps:
launch the travel website
provide going from location
provide going to location
select the departure date
click on flight search button
select the filter 1 stop
verify that the filtered results show flights having only 1 stop
"""

@pytest.mark.usefixtures("setup")
@ddt()
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

        #DDT for small tests:
    #@data(("Mumbai","New York", "24/04/2025", "1 Stop"),("New Delhi","London", "25/04/2025", "2 Stops"))
    #@unpack

        #for reading from the file:
    #@file_data("../testdata/testdata.json") #../ - one level higher
    #@file_data("../testdata/testyaml.yaml") #for yaml you need PyYAML

        #for reading from excel (don't forget * before Utils!) And you need to write a util to read from xlsx
    #@data(*Utils.read_data_from_excel("C:\\python-selenium\\TestFrameworkDemo\\testdata\\tdataexcel.xlsx","Sheet1"))

        #for reading from csv: (also * for reading the list)
    @data(*Utils.read_data_from_csv("C:\\python-selenium\\TestFrameworkDemo\\testdata\\tdatacsv.csv"))
    @unpack
    def test_search_flights_1_stop(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stop(stops)
        allstops1 = search_flight_result.get_search_flight_results()
        self.log.onfo(len(allstops1))
        self.ut.assertListItemText(allstops1, stops)

    # def test_search_flights_2_stop(self):
    #     search_flight_result = self.lp.searchFlights("Mumbai", "New York", "24/04/2025")
    #     self.lp.page_scroll()
    #     search_flight_result.filter_flights_by_stop("2 Stop")
    #     allstops1 = search_flight_result.get_search_flight_results()
    #     print(len(allstops1))
    #     self.ut.assertListItemText(allstops1, "2 Stops")

        # lp.enterDepartFromLocation("Mumbai")
        # #Provide going to location
        # lp.enterGoingToLocation("New York")
        # #Select the departure date
        # lp.enterDepartureDate("24/04/2025") #hardcode right now
        # #Click on search button
        # lp.clickSearchFlightsButton()
        # #to handle dinamic scroll

        # #Launching browser and opening the travel website
        # #provide going from location
        # lp = LaunchPage(self.driver)
        # lp.enterDepartFromLocation("Mumbai")
        # #Provide going to location
        # lp.goingto("New York")
        # #Select the departure date
        # lp.selectdate("24/04/2025") #hardcode right now
        # #Click on search button
        # lp.clicksearch()
        # #to handle dinamic scroll
        # lp.page_scroll()
        #
        # #second page, selection of the filter 1 stop
        # sf = SearchFlightResults(self.driver)
        # sf.filter_flights()
        # time.sleep(3)
        #
        # #return the list of elements that contains only 1 stop
        # allstops1 = lp.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        # print(len(allstops1))
        #
        # ut = Utils()
        # ut.assertListItemText(allstops1, "1 Stop")




