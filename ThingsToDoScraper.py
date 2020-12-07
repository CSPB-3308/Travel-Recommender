from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
import os
#from pathlib import Path
# Source: https://towardsdatascience.com/if-you-like-to-travel-let-python-help-you-scrape-the-best-fares-5a1f26213086
# mac chrome driver path:
##chromedriver_path = '/usr/local/bin/chromedriver'
# PC chrome driver path:
# chromedriver_path = Path(__file__).parent / "windows-chromedriver/chromedriver.exe"
#driver = webdriver.Chrome(executable_path=chromedriver_path)
#sleep(2)

def scrapeForThingsToDo(location):
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
    sleep(2)

    """City codes - it's the city, state (in US) and city, country for international
    (spaces in city name and country name must be _) ex: Denver_CO, London_England"""

    usnews = ('https://travel.usnews.com/' + location + '/Things_To_Do/')
    print(usnews)
    driver.get(usnews)
    print(driver.page_source)
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
        summary.append(attraction[-1])
    places_df = pd.DataFrame()
    places_df['Attraction Name'] = place_name
    places_df['Type'] = type_place
    places_df['Time To Spend'] = time_to_spend
    places_df['About'] = summary
    places_df['Timestamp'] = strftime("%Y-%m-%d-%H:%M")  # so we can know when it was scraped
    result = places_df.to_html()
    driver.close()
    driver.quit()
    
    return result

