# Fall 2020
# CSCI 3308
# Checkpoint 3
# Testing File for Hotel Scraper and Flight Scraper
# See depencencies and function information in TESTING.md

import unittest
import FlightScraper as flight


class FlightScraperTestCase3(unittest.TestCase):
    def test_flight_denver_to_los_angeles(self):
        result = flight.scrapeForFlights("Denver CO", "Los Angeles CA", "2020-12-12", "2020-12-14", "ftest8.html")
        response = 0
        self.assertEqual(response, result, "Incorrect result testing for flight results")

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()