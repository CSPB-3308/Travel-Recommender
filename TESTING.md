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
##### This component has not been fully built into django yet, but is fully functional within python.
##### Before running the unit tests (from unit-tests folder) you will need to enter into HotelScraper.py and FlightScraper.py
##### and verify that the correct chromedriver path has been selected for your machine: if it is a mac you do not need to do anything,
##### if it is a PC you will need to uncomment the chromedriver path for windows and comment out the mac path (this is temporary will
##### not apply once the functions are launched to heroku) 
##### To test: run each python file in the unit-tests folder
###### testing.py: checks that all values being read into the webscraper have been verified/formatted appropriately; you will see 10 unit-tests (half for web-  ###### scrapping hotels and half for flights)  
###### flighttesting2, flighttesting3: each run and verify that the function will scrape correct flight data: you can see the output in the html files that will be produced
############ must be run one at a time, selenium is not designed to have multiple queries at once (may need to run once or twice, if you've made alot of web ############ connections in a short period of time: Kayak can get overwhelmed) 
###### hoteltesting2, hoteltesting3, hoteltesting4: each run and verify different inputs to scrape hotel data: you can see the output in the html files that will be produced
############ must be run one at a time, selenium is not designed to have multiple queries at once
