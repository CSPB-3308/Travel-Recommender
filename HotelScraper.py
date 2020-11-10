from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from datetime import date
from datetime import datetime as dt
import re
# Source: https://towardsdatascience.com/if-you-like-to-travel-let-python-help-you-scrape-the-best-fares-5a1f26213086

chromedriver_path = Path(__file__).parent / "chromedriver/chromedriver.exe"
#chromedriver_path = '/usr/local/bin/chromedriver' # Change this to your own chromedriver path!
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)


def start_kayak(city, date_start, date_end):
    """City codes - it's the city, state (in US) and city, country for international
    (spaces in city name must be -; and no spaces between city,country)
    Date format -  YYYY-MM-DD"""

    kayak = ('https://www.kayak.com/hotels/' + city + '/' + date_start +
             '/' + date_end + '/2adults?sort=rank_a&fs=property=hotel')
    driver.get(kayak)
    sleep(randint(8, 10))

    # sometimes a popup shows up, so we can use a try statement to check it and close
    try:
        driver.implicitly_wait(10)
        xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
        driver.find_elements_by_xpath(xp_popup_close)[-1].click()
    except:
        pass

    df_flights_best = page_scrape(city, date_start, date_end)
    return df_flights_best


def page_scrape(location, date_outbound, date_inbound):
    # This function takes care of the scraping part
    hotel = '// *[ @class="Hotels-Results-HotelResultInfoColumn"]'
    price = '//*[@class="col col-booking"]'

    sections = driver.find_elements_by_xpath(hotel)
    price_sections = driver.find_elements_by_xpath(price)

    hotels_list = [value.text for value in sections]
    prices_list = [prices.text for prices in price_sections]

    parsed_hotels = []
    parsed_prices = []

    for i in hotels_list:
        parsed_hotels.append(i.split('\n'))
    for i in prices_list:
        parsed_prices.append(i.split('\n'))
    parsed_prices.pop(0)

    hotel_name = []
    rating = []
    price = []  # price per night
    vendor = []
    amenities = []
    in_date = []
    out_date = []
    city = []
    for hotel in parsed_hotels:
        city.append(location)
        in_date.append(date_outbound)
        out_date.append(date_inbound)
        if hotel[0] == 'Recommended':
            hotel.pop(0)
        hotel_name.append(hotel[0])
        rating.append(hotel[1] + ' ' + hotel[2])
    for p in parsed_prices:
        if '$' not in p[0]:
            p.pop(0)
        p.remove('View Deal')
        price.append(p[0])
        vendor.append(p[1])
        amenity = ""
        for val in range(2, len(p)):
            amenity = amenity + ' ' + p[val]
        amenities.append(amenity)
    hotels_df = pd.DataFrame()
    hotels_df['Location'] = city
    hotels_df['Check-In Date'] = in_date
    hotels_df['Check-Out Date'] = out_date
    hotels_df['Hotel Name'] = hotel_name
    hotels_df['Rating'] = rating
    hotels_df['Amenities'] = amenities
    hotels_df['Price per Night'] = price
    hotels_df['View Deal At'] = vendor
    hotels_df['Timestamp'] = strftime("%Y-%m-%d-%H:%M")  # so we can know when it was scraped
    return hotels_df


def city_input_check(city):
    city_input = city.split(' ')  # make assumption, state/country has been spelled correctly
    city_fixed = []
    for i in city_input:  # rudimentary error checking
        city_fixed.append(i.replace(",", ""))
    city_correct = ''
    if len(city_fixed[-1]) == 2:
        for i in range(len(city_fixed) - 1):
            city_correct = city_fixed[i].capitalize() + '-'
        city_correct = city_correct + city_input[-1]
        return city_correct
    else:
        print("2-letter state/country missing/incorrect")
    return ''


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
        print("Can not check-in on a past day")
        return False
    if b < a:
        print("Return Date must be after Departure, please try again")
        return False
    return True


def scrapeForHotels(city, date_start, date_end, html_file):
    # For when you want to accept input from command-line:
    # city = input('Where are you visiting? Format must be city 2-letter state (in USA ex: Denver CO) or city 2-letter country (international ex: London UK) ')
    # date_start = input('When are you checking in? Please use YYYY-MM-DD format only, must leave on/after:' + str(date.today()) + ' ')
    # date_end = input('When are you checking out? Please use YYYY-MM-DD format only, must checkout after check-in date ')
    correct = input_check(date_start, date_end)
    city_formatted = city_input_check(city)
    if city_formatted == '':
        correct = False
    if correct:

        kayak = 'https://www.kayak.com/hotels/Los-Angeles,CA-c16078/2020-12-06/2020-12-13/2adults?sort=rank_a&fs=property=hotel'
        driver.get(kayak)
        sleep(3)

        # Closing the popup
        try:
            driver.implicitly_wait(10)
            xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
            driver.find_elements_by_xpath(xp_popup_close)[-1].click()
        except:
            pass

        df = start_kayak(city_formatted, date_start, date_end)
        result = df.to_html()
        text_file = open(html_file, "w")
        text_file.write(result)
        text_file.close()
        driver.quit()
        return 0
    else:
        driver.quit()
        return "Incorrect inputs"
