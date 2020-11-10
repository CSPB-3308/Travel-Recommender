# Project Title
#### Travel-Recommender

# Team Members' names
#### Bryan Arment
#### Jeff Dank
#### Bryant Hicks
#### Becca Meares

# Automated Test Cases
### ***Step 1. Cone the repository***
##### git clone https://github.com/CSPB-3308/Travel-Recommender.git
#####
### ***Step 2. Navigate into main folder***
##### cd Travel-Recommender\TravelRec
#####
### ***Step 3. Run automated tests***
##### pythong manage.py test
##### These automated tests should check that all the possible urls of our app are working properly

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

