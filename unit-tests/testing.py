#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Team Echo
# Fall 2020
# CSCI 3308
# Checkpoint 3
# Testing File for Hotel Scraper and Flight Scraper
# See depencencies and function information in TESTING.md

import unittest
import FlightScraper as flight
import HotelScraper as hotel


class FlightScraperTestCase(unittest.TestCase):
    # Test function inputs
    def test_return_before_depart(self):
        result = flight.scrapeForFlights("Denver CO", "Los Angeles CA", "2020-12-12", "2020-12-10", "ftest1.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result comparing return/departure dates")

    def test_depart_in_past(self):
        result = flight.scrapeForFlights("Denver CO", "Los Angeles CA", "2020-11-01", "2020-12-10", "ftest2.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result comparing return/departure dates")

    def test_incorrect_date_format(self):
        result = flight.scrapeForFlights("Denver CO", "Los Angeles CA", "2020/12/10", "2020/12/15", "ftest3.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing format of dates")
        result = flight.scrapeForFlights("Denver CO", "Los Angeles CA", "20-12-10", "20-12-15", "ftest3.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing format of dates")
        result = flight.scrapeForFlights("Denver CO", "Los Angeles CA", "12-10-2020", "12-15-2020", "ftest3.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing format of dates")

    def test_home_airport_invalid(self):
        result = flight.scrapeForFlights("Avocado SA", "Los Angeles CA", "2020-12-10", "2020-12-15", "ftest4.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing for airport validity")

    def test_no_airport_available(self):
        result = flight.scrapeForFlights("Aurora CO", "Los Angeles CA", "2020-12-10", "2020-12-15", "ftest5.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing for airport validity")

    def test_city_input_validation(self):
        result = flight.scrapeForFlights(" ", "los angeles ca", "2020-12-10", "2020-12-15", "ftest6.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing for airport formating")


class HotelScraperTestCase(unittest.TestCase):
    # Test function inputs
    def test_checkout_before_checkin(self):
        result = hotel.scrapeForHotels("Los Angeles CA", "2020-12-12", "2020-12-10", "htest1.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result comparing return/departure dates")

    def test_checkin_in_past(self):
        result = hotel.scrapeForHotels("Denver CO", "2020-11-01", "2020-12-10", "htest2.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result comparing return/departure dates")

    def test_incorrect_hotel_date_format(self):
        result = hotel.scrapeForHotels("Los Angeles CA", "2020/12/10", "2020/12/15", "htest3.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing format of dates")
        result = hotel.scrapeForHotels("Denver CO", "20-12-10", "20-12-15", "htest3.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing format of dates")
        result = hotel.scrapeForHotels("Denver CO", "12-10-2020", "12-15-2020", "htest3.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing format of dates")

    def test_hotel_location_invalid(self):
        result = hotel.scrapeForHotels("Los Angeles", "2020-12-10", "2020-12-15", "htest4.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing for hotel location validity")
        result = hotel.scrapeForHotels(" ", "2020-12-10", "2020-12-15", "htest4.html")
        response = "Incorrect inputs"
        self.assertEqual(response, result, "Incorrect result testing for airport validity")

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()

