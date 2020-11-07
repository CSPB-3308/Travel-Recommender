from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
# Source: https://towardsdatascience.com/if-you-like-to-travel-let-python-help-you-scrape-the-best-fares-5a1f26213086


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
    except Exception as e:
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

    print(hotels_list)
    print(prices_list)

    parsed_hotels = []
    parsed_prices = []

    for i in hotels_list:
        parsed_hotels.append(i.split('\n'))
    for i in prices_list:
        parsed_prices.append(i.split('\n'))
    parsed_prices.pop(0)
    print(parsed_hotels)
    print(parsed_prices)

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

    print(len(hotel_name), hotel_name)
    print(len(rating), rating)
    print(len(price), price)
    print(len(vendor), vendor)
    print(len(amenities), amenities)

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


chromedriver_path = '/usr/local/bin/chromedriver' # Change this to your own chromedriver path!
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

kayak = 'https://www.kayak.com/hotels/Los-Angeles,CA-c16078/2020-12-06/2020-12-13/2adults?sort=rank_a&fs=property=hotel'
driver.get(kayak)
sleep(3)

# Closing the popup

#driver.implicitly_wait(10)
#xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close")]'
#driver.find_elements_by_xpath(xp_popup_close)[-1].click()

#city_from = input('From which city? ')
#city_to = input('Where to? ')
#date_start = input('Search around which departure date? Please use YYYY-MM-DD format only ')
#date_end = input('Return when? Please use YYYY-MM-DD format only ')


city = 'Los-Angeles,CA'
date_start = '2020-12-21'
date_end = '2020-12-27'

df = start_kayak(city, date_start, date_end)
result = df.to_html()
print(result)
text_file = open("hotels.html", "w")
text_file.write(result)
text_file.close()
driver.quit()