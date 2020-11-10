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


def test_hotel_city_input_validation(self):
    result = hotel.scrapeForHotels("denver, co", "2020-12-10", "2020-12-15", "htest5.html")
    response = 0
    self.assertEqual(response, result, "Incorrect result testing for airport formating")

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()