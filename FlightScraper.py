from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
import city_code_helper as c
from datetime import datetime as dt
from datetime import date
import re
# Source: https://towardsdatascience.com/if-you-like-to-travel-let-python-help-you-scrape-the-best-fares-5a1f26213086
chromedriver_path = Path(__file__).parent / "chromedriver/chromedriver.exe"
#chromedriver_path = '/usr/local/bin/chromedriver' # Change this to your own chromedriver path!
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)


def start_kayak(city_from, city_to, date_start, date_end):
    """City codes - it's the IATA codes!
    Date format -  YYYY-MM-DD"""

    kayak = ('https://www.kayak.com/flights/' + city_from + '-' + city_to +
             '/' + date_start + '/' + date_end + '?sort=bestflight_a')
    driver.get(kayak)
    sleep(randint(8, 10))

    # sometimes a popup shows up, so we can use a try statement to check it and close
    try:
        driver.implicitly_wait(10)
        xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
        driver.find_elements_by_xpath(xp_popup_close)[-1].click()
    except:
        pass

    df_flights_best = page_scrape(date_start, date_end)
    return df_flights_best


def page_scrape(date_outbound, date_inbound):
    # This function takes care of the scraping part
    xp_sections = '//*[@class="flights"]'
    price = '//*[@class="price option-text"]'
    sections = driver.find_elements_by_xpath(xp_sections)
    price_sections = driver.find_elements_by_xpath(price)
    sections_list = [value.text for value in sections]
    prices_list = [prices.text for prices in price_sections]
    parsed_prices = []
    for i in prices_list:
        if i != '':
            parsed_prices.append(i)
    parsed_flights = []
    for i in sections_list:
        parsed_flights.append(i.split('\n'))

    # split inbound and outbound flight info
    outbound = []
    inbound = []
    for i in parsed_flights:
        if i[2] == 'nonstop':
            outbound.append(i[0:7])
            inbound.append(i[7::])
        else:
            outbound.append(i[0:8])
            inbound.append(i[8::])
    outbound_time = []
    inbound_time = []
    outbound_airline = []
    inbound_airline = []
    outbound_stops = []
    inbound_stops = []
    outbound_stop_cities = []
    inbound_stop_cities = []
    outbound_flight_duration = []
    inbound_flight_duration = []
    outbound_route = []
    inbound_route = []
    outbound_date = []
    inbound_date = []
    nonstop = "N/A"
    for flights in outbound:
        if flights[2] == 'nonstop':
            # split accordingly
            outbound_date.append(date_outbound)
            outbound_time.append(flights[0])
            outbound_airline.append(flights[1])
            outbound_stops.append(flights[2])
            outbound_stop_cities.append(nonstop)
            outbound_flight_duration.append(flights[3])
            outbound_route.append(flights[4] + flights[5] + flights[6])
        else:
            outbound_date.append(date_outbound)
            outbound_time.append(flights[0])
            outbound_airline.append(flights[1])
            outbound_stops.append(flights[2])
            outbound_stop_cities.append(flights[3])
            outbound_flight_duration.append(flights[4])
            outbound_route.append(flights[5] + flights[6] + flights[7])
    for flights in inbound:
        if flights[2] == 'nonstop':
            # split accordingly
            inbound_date.append(date_inbound)
            inbound_time.append(flights[0])
            inbound_airline.append(flights[1])
            inbound_stops.append(flights[2])
            inbound_stop_cities.append(nonstop)
            inbound_flight_duration.append(flights[3])
            inbound_route.append(flights[4] + flights[5] + flights[6])
        else:
            inbound_date.append(date_inbound)
            inbound_time.append(flights[0])
            inbound_airline.append(flights[1])
            inbound_stops.append(flights[2])
            inbound_stop_cities.append(flights[3])
            inbound_flight_duration.append(flights[4])
            inbound_route.append(flights[5] + flights[6] + flights[7])

    flights_df = pd.DataFrame()
    flights_df['Outbound Day'] = outbound_date
    flights_df['Outbound Time'] = outbound_time
    flights_df['Outbound Route'] = outbound_route
    flights_df['Outbound Airline'] =outbound_airline
    flights_df['Outbound Flight Duration'] = outbound_flight_duration
    flights_df['Outbound Number of Stops'] = outbound_stops
    flights_df['Outbound Stop Cities'] = outbound_stop_cities
    flights_df['Return Day'] = inbound_date
    flights_df['Return Time'] = inbound_time
    flights_df['Return Route'] = inbound_route
    flights_df['Return Airline'] = inbound_airline
    flights_df['Return Flight Duration'] = inbound_flight_duration
    flights_df['Return Number of Stops'] = inbound_stops
    flights_df['Return Stop Cities'] = inbound_stop_cities
    flights_df['Price'] = parsed_prices
    flights_df['Timestamp'] = strftime("%Y-%m-%d-%H:%M")  # so we can know when it was scraped
    return flights_df


def city_input_check(city):
    city_input = city.split(' ')  # make assumption, state/country has been spelled correctly
    city_fixed = []
    for i in city_input:  # rudimentary error checking
        city_fixed.append(i.replace(",", ""))
    city_correct = ''
    if len(city_fixed) > 1:
        city_fixed.pop(-1)
        for i in city_fixed:
            city_correct = city_correct + i + ' '
    iata_code = c.convert_city_to_IATA(city_correct.strip(' '))
    if iata_code == "Not Found":
        print("Invalid City, please try again")
        return ''
    return iata_code


def input_check(date_start, date_end):  # checks if dates are implemented correctly
    # regex match python
    matched_out = re.match("^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", date_start)
    is_match_out = bool(matched_out)
    if not is_match_out:
        print("Invalid Departure Date, please try again")
        return False
    matched_in = re.match("^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", date_end)
    is_match_in = bool(matched_in)
    if not is_match_in:
        print("Invalid Return Date, please try again")
        return False
    # convert to dt object to verify date is in future/not too far in future
    # a must be greater than b (must leave before you return)
    today_str = str(date.today())
    today = dt.strptime(today_str, "%Y-%m-%d")
    a = dt.strptime(date_start, "%Y-%m-%d")
    b = dt.strptime(date_end, "%Y-%m-%d")
    if today > a:
        print("Cannot depart on a past date")
        return False
    if b < a:
        print("Return Date must be after Departure, please try again")
        return False
    return True


def scrapeForFlights(city_to, city_from, date_start, date_end, html_file):
    # For when you want to accept input from command-line:
    # city_from = input('Where are you flying out of? Format must be city 2-letter state (in USA ex: Denver CO) or city 2-letter country (international ex: London UK) ')
    # city_to = input('Where are you visiting? Format must be city 2-letter state (in USA ex: Denver CO) or city 2-letter country (international ex: London UK) ')
    # date_start = input('What is your departure date? Please use YYYY-MM-DD format only, must leave on/after:' + str(date.today()) + ' ')
    # date_end = input('When is your return date? Please use YYYY-MM-DD format only, must checkout after check-in date ')
    correct = input_check(date_start, date_end)
    city_from_formatted = city_input_check(city_from)
    if city_from_formatted == '':
        correct = False
    city_to_formatted = city_input_check(city_to)
    if city_to_formatted == '':
        correct = False
    if correct:
        driver.implicitly_wait(10)
        kayak = 'https://www.kayak.com/flights/LIS-SIN/2020-12-01/2020-12-15?sort=bestflight_a'

        driver.get(kayak)
        sleep(3)

        # Closing the popup
        try:
            driver.implicitly_wait(10)
            xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
            driver.find_elements_by_xpath(xp_popup_close)[-1].click()
        except:
            pass

        df = start_kayak(city_from_formatted, city_to_formatted, date_start, date_end)
        result = df.to_html()
        text_file = open(html_file, "w")
        text_file.write(result)
        text_file.close()
        driver.close()
        driver.quit()
        return 0
    else:
        driver.quit()
        return "Incorrect inputs"
