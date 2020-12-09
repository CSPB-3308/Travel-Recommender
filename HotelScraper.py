from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
import os
# Source: https://towardsdatascience.com/if-you-like-to-travel-let-python-help-you-scrape-the-best-fares-5a1f26213086
#         https://medium.com/@mikelcbrowne/running-chromedriver-with-python-selenium-on-heroku-acc1566d161c

# GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'
# CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# sleep(2)
chromedriver_path = '/usr/local/bin/chromedriver' # Change this to your own chromedriver path!
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)


def scrapeForHotels(location, date_start, date_end):
    """City codes - it's the city, state (in US) and city, country for international
    (spaces in city name must be -; and no spaces between city,country)
    Date format -  YYYY-MM-DD"""

    kayak = ('https://www.kayak.com/hotels/' + location + '/' + date_start +
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
        in_date.append(date_start)
        out_date.append(date_end)
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

    # For when you want to accept input from command-line:
    # city = input('Where are you visiting? Format must be city 2-letter state (in USA ex: Denver CO) or city 2-letter country (international ex: London UK) ')
    # date_start = input('When are you checking in? Please use YYYY-MM-DD format only, must leave on/after:' + str(date.today()) + ' ')
    # date_end = input('When are you checking out? Please use YYYY-MM-DD format only, must checkout after check-in date ')

    # kayak = 'https://www.kayak.com/hotels/Los-Angeles,CA-c16078/2020-12-06/2020-12-13/2adults?sort=rank_a&fs=property=hotel'
    # driver.get(kayak)
    # sleep(3)
    #
    # # Closing the popup
    # try:
    #     driver.implicitly_wait(10)
    #     xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
    #     driver.find_elements_by_xpath(xp_popup_close)[-1].click()
    # except:
    #     pass
    result = hotels_df.to_html(index=False)
    driver.close()
    driver.quit()
    return result

