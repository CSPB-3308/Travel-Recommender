# Project Title
#### Travel-Recommender

# Team Members' names
#### Bryan Arment
#### Jeff Dank
#### Bryant Hicks
#### Becca Meares

# Automated Test Cases
### 1)Name: Test URLs
###   Description: Ensure possible urls are working for app
###   Pre-conditions: None
###   Test steps
####     a. Clone the repository: git clone https://github.com/CSPB-3308/Travel-Recommender.git
####     b. Navigate into main folder: cd Travel-Recommender\TravelRec
####     c. Run automated tests: python manage.py test
###   Expected result
####       all tests should pass
###   Actual result
####       print to the command prompt of how many tests pass / fail
###   Status
####       pass / fail display in the command prompt
###   Notes
####       none
###   Post-conditions
####       The user is then free to start running the app with python manage.py runserver
### 2) Name:
####     Test flight scraper
###    Description:
####     Ensure that scraping the data off the web works for flights
###    Preconditions: 
####      Required software: numpy 1.19.3, selerium, pandas. These can all be installed with "pip install ". Appears to only be working on a mac at the moment. Otherwise Before running the unit tests (from unit-tests folder) you will need to enter into HotelScraper.py and FlightScraper.py and verify that the correct chromedriver path has been selected for your machine: if it is a mac you do not need to do anything, if it is a PC you will need to uncomment the chromedriver path for windows and comment out the mac path (this is temporary will not apply once the functions are launched to heroku) 
###    Test steps
####       a. Navigate to Travel-Recommender\unit-tests
####       b. python flighttest2.py
####       c. python flighttest3.py
###    Expected results
####       If you are using a mac, then all tests should pass
###    Status
####       pass / fail will be displayed to the command prompt
###    Notes
####       This is still being debugged. flighttesting2, flighttesting3: each run and verify that the function will scrape correct flight data: you can see the output in the html files that will be produced --- must be run one at a time, selenium is not designed to have multiple queries at once (may need to run once or twice, if you've made alot of web connections in a short period of time: Kayak can get overwhelmed) 
###    Post conditions
####        The user will be able to get the most up to date flight info

### 3) Name: Hotel flight scraper
###    Description:
####     Ensure that scraping the data off the web works for hotels
###    Preconditions:
####     Required software: numpy 1.19.3, selerium, pandas. These can all be installed with "pip install " Appears to only be working on a mac at the moment.
###    Test steps
####       a. Navigate to Travel-Recommender\unit-tests
####       b. python hoteltesting1.py
####       c. python hoteltesting2.py
####       d. python hoteltesting3.py
###    Expected results
####       If you are using a mac, then all tests should pass
###    Status
####       pass / fail will be displayed to the command prompt
###    Notes
####       This is still being debugged. hoteltesting2, hoteltesting3, hoteltesting4: each run and verify different inputs to scrape hotel data: you can see the output in the html files that will be produced -- must be run one at a time, selenium is not designed to have multiple queries at once. testing.py: checks that all values being read into the webscraper have been verified/formatted appropriately; you will see 10 unit-tests (half for web-scraping hotels and half for flights) 
###    Post conditions
####        The user will be able to get the most up to date hotel info

# User Acceptance Testing
### ***Step 4. Start local server***
##### python manage.py runserver
#####
### ***Step 5. Navigate to URL shown in command window***
##### Example output from step 3: Starting development server at http://127.0.0.1:8000/
##### Open a web browser and navigate to that url
#####
### ***Step 6. Fill in your information***
##### Enter your name in the name box
##### Enter your email in the email box
##### Select your destination from drop down
##### Click "Get Recommendations" button
#####
### ***Step 7. Ensure that recommendations page comes up***
##### The url should now be: http://127.0.0.1:8000/recommendations/ or whatever base url you are given + "/recommendations/"
#####
### ***Step8. Testing Web Scraping***
##### Required software: numpy 1.19.3, selerium, pandas. These can all be installed with "pip install "

