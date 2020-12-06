from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
import os
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
    df_things_todo = page_scrape()
    return df_things_todo


def page_scrape():
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


def scrapeForThingsToDo(location, country):
    df = start_usnews(location, country)
    df.to_json('results.js')
    result = df.to_html()
    text_file = open('attractions.htm', "w")
    text_file.write(result)
    text_file.close()
    driver.quit()
