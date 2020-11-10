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


class HotelScraperTestCase3(unittest.TestCase):
    def test_hotel_search_new_york(self):
        result = hotel.scrapeForHotels("New York NY", "2020-12-12", "2020-12-14", "htest7.html")
        response = 0
        self.assertEqual(response, result, "Incorrect result testing for flight results")

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()