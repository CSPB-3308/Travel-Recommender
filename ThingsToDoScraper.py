from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from datetime import date
from datetime import datetime as dt
from pathlib import Path
import re
# Source: https://towardsdatascience.com/if-you-like-to-travel-let-python-help-you-scrape-the-best-fares-5a1f26213086

GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
sleep(2)


def start_usnews(city, country):
    """City codes - it's the city, state (in US) and city, country for international
    (spaces in city name and country name must be _) ex: Denver_CO, London_England"""

    usnews = ('https://travel.usnews.com/' + city + '_' + country + '/Things_To_Do/')
    driver.get(usnews)
    sleep(randint(8, 10))

    # sometimes a popup shows up, so we can use a try statement to check it and close
    """try:
        driver.implicitly_wait(10)
        xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
        driver.find_elements_by_xpath(xp_popup_close)[-1].click()
    except:
        pass"""
    df_things_todo = page_scrape(city, country)
    return df_things_todo


def page_scrape(location, country):
    # This function takes care of the scraping part
    place = '// *[ @class="GenericList__ListItemContainer-tjuxmv-1 deINyp"]'
    sections = driver.find_elements_by_xpath(place)

    places_list = [value.text for value in sections]
    parsed_places = []
    for i in places_list:
        parsed_places.append(i.split('\n'))
    place_name = []
    type_place = []
    time_to_spend = []
    summary = []
    for attraction in parsed_places:
        attraction.pop(0)  # remove first val in array
        for info in attraction:
            if info == 'FREE':
                attraction.remove(info)
            if info == 'Find Tours & Tickets':
                attraction.remove(info)
        place_name.append(attraction[0])
        type_place.append(attraction[2])
        time_to_spend.append(attraction[4])
        summary.append(attraction[-1])
    places_df = pd.DataFrame()
    places_df['Attraction Name'] = place_name
    places_df['Type'] = type_place
    places_df['Time To Spend'] = time_to_spend
    places_df['About'] = summary
    places_df['Timestamp'] = strftime("%Y-%m-%d-%H:%M")  # so we can know when it was scraped
    return places_df



"""
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
        return "Incorrect inputs"""


df = start_usnews('London', 'England')
json_file = df.to_json('results.js')
result = df.to_html()
text_file = open('attractions.htm', "w")
text_file.write(result)
text_file.close()
driver.quit()
