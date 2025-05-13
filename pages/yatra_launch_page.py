from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from base.base_driver import BaseDriver
from pages.search_flights_results_page import SearchFlightResults


class LaunchPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

    #Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepatureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER) #if it doesn't work, old code is down below the new code

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        time.sleep(2)
        self.getGoingToField().send_keys(goingtolocation)
        time.sleep(2)
        search_results = self.getGoingToResults()
        for results in search_results:
            if goingtolocation in results.text:
                results.click()
                break

    def enterDepartureDate(self, departuredate):
        self.getDepatureDateField().click()
        all_dates = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def clickSearchFlightsButton(self):
        self.getSearchButton().click()
        time.sleep(4)

    #the logic of searchingflights from test page:
    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.clickSearchFlightsButton()
        search_flights_result = SearchFlightResults(self.driver)
        return search_flights_result

    # def departfrom(self, departlocation):
    #     depart_from = self.wait_until_element_is_clickable(By.XPATH, "//p[@title='New Delhi']")
    #     depart_from.click()
    #     #time.sleep(2)
    #     depart_from0 = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='input-with-icon-adornment']")
    #     depart_from0.send_keys("Mumbai") #should be departlocation but for now it's hardcoded
    #     time.sleep(2)
    #     depart_from1 = self.wait_until_element_is_clickable(By.CSS_SELECTOR, "div[class='MuiBox-root css-134xwrj'] div[class='MuiBox-root css-0']")
    #     depart_from1.click()
    #     #time.sleep(2)

    # def goingto(self, goingtolocation):
    #     going_to = self.wait_until_element_is_clickable(By.XPATH, "//div[@aria-label='Going To Mumbai inputbox']//p[@title='Mumbai'][normalize-space()='mumbai']")
    #     going_to.click()
    #     #time.sleep(2)
    #     going_to0 = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='input-with-icon-adornment']")
    #     going_to0.send_keys("New York") #should be goingtolocation but for now it's hardcoded
    #     time.sleep(2)
    #     going_to1 = self.wait_until_element_is_clickable(By.CSS_SELECTOR, "div[class='MuiBox-root css-134xwrj'] div:nth-child(1) li:nth-child(1) div:nth-child(1) div:nth-child(1) div:nth-child(1)")
    #     going_to1.click()
    #     #time.sleep(2)
    #
    # def selectdate(self, departuredate):
    #     travel_date = self.wait_until_element_is_clickable(By.CSS_SELECTOR, ".css-w7k25o")
    #     travel_date.click()
    #     travel_date0 = self.wait_until_element_is_clickable(By.XPATH, "//div[@aria-label='Choose Thursday, April 17th, 2025']//span[@aria-label='MAHA SHIVARATHIRI']")
    #     travel_date0.click()
    #
    #
    # def clicksearch(self):
    #     click_search = (self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']"))
    #     click_search.click()
    #     time.sleep(4)


