#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Team Echo
# Fall 2020
# CSCI 3308
# Checkpoint 3
# Testing File for Hotel Scraper and Flight Scraper
# See depencencies and function information in TESTING.md

import unittest
import HotelScraper as hotel


class HotelScraperTestCase2(unittest.TestCase):
    def test_hotel_search_london(self):
        result = hotel.scrapeForHotels("London UK", "2020-12-10", "2020-12-15", "htest6.html")
        response = 0
        self.assertEqual(response, result, "Incorrect result testing for flight results")

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()