from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
import os

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


def scrapeForThingsToDo(location):

    """City codes - it's the city, state (in US) and city, country for international
    (spaces in city name and country name must be _) ex: Denver_CO, London_England"""

    usnews = ('https://travel.usnews.com/' + location + '/Things_To_Do/')
    driver.get(usnews)
    sleep(randint(8, 10))

    # sometimes a popup shows up, so we can use a try statement to check it and close
    """try:
        driver.implicitly_wait(10)
        xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
        driver.find_elements_by_xpath(xp_popup_close)[-1].click()
    except:
        pass"""
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
        if attraction[-1] == 'TIME TO SPEND':
            summary.append('')
        else:
            summary.append(attraction[-1])
    places_df = pd.DataFrame()
    places_df['Attraction Name'] = place_name
    places_df['Type'] = type_place
    places_df['Time To Spend'] = time_to_spend
    places_df['About'] = summary

    result = places_df.to_html(index=False)
    driver.close()
    driver.quit()

    return result


#scrapeForThingsToDo('London_England')
