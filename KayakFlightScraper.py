from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from IPython.display import HTML
# Source: https://towardsdatascience.com/if-you-like-to-travel-let-python-help-you-scrape-the-best-fares-5a1f26213086


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
    except Exception as e:
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
    flights_df['Price'] = prices_list
    flights_df['timestamp'] = strftime("%Y-%m-%d-%H:%M")  # so we can know when it was scraped
    return flights_df


chromedriver_path = '/usr/local/bin/chromedriver' # Change this to your own chromedriver path!
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

kayak = 'https://www.kayak.com/flights/LIS-SIN/2020-12-01/2020-12-15?sort=bestflight_a'
driver.get(kayak)
sleep(3)

# Closing the popup

driver.implicitly_wait(10)
xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
driver.find_elements_by_xpath(xp_popup_close)[-1].click()

#city_from = input('From which city? ')
#city_to = input('Where to? ')
#date_start = input('Search around which departure date? Please use YYYY-MM-DD format only ')
#date_end = input('Return when? Please use YYYY-MM-DD format only ')

city_from = 'DEN'
city_to = 'LAX'
date_start = '2020-12-21'
date_end = '2020-12-27'

df = start_kayak(city_from, city_to, date_start, date_end)
result = df.to_html(classes='table table-striped')
print(result)
text_file = open("flights.html", "w")
text_file.write(result)
text_file.close()
driver.quit()
