#!/usr/bin/python3
import requests
import sqlite3
# quote is for one way flights from origin to destination
# get input from user (on UI for the variables
# TO DO: figure out how to read data from HTML page; implement error checking for data
# current error: flight time is not pulled in API call (all flights leave at 00:00:00)

def callFlightApi(country, currency, locale, originplace, destinationplace, outbounddate):
    url = "https://rapidapi.p.rapidapi.com/apiservices/browsedates/v1.0/"+str(country)+"/"+str(currency)+"/"+str(locale)+"/"+str(originplace)+"/"+str(destinationplace)+"/"+str(outbounddate)

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "7b2eddb092msh072319716969884p1ddce0jsne5b5ae71c1d7"
    }

    response = requests.request("GET", url, headers=headers)

    if (response.status_code == 200):
        parse = response.json()
        parsed_responses = parseResponse(parse)
        return parsed_responses
    else:
        return "Error Flight Data Could Not Be Collected!"

def parseResponse(parse):
    quotes = parse['Quotes']
    outbound_flight = []
    for i in quotes:
        flight_info = []
        flight_price = int(i['MinPrice'])
        flight_info.append(flight_price)
        if i['Direct'] == True:
            direct_flight = 'Direct'
        else:
            direct_flight = 'In-Direct'
        flight_info.append(direct_flight)
        outbound_leg = i['OutboundLeg']
        carrier_ids = outbound_leg.pop('CarrierIds')
        flight_info.append(carrier_ids)
        origin_id = outbound_leg.pop('OriginId')
        flight_info.append(origin_id)
        destination_id = outbound_leg.pop('DestinationId')
        flight_info.append(destination_id)
        departure_date_time = outbound_leg.pop('DepartureDate')
        departure_date = ""
        departure_time = ""
        T_found = False
        for letter in departure_date_time:
            if letter != 'T' and T_found == False:
                departure_date = departure_date + letter
            elif letter == 'T':
                T_found = True
                continue
            if T_found == True:
                departure_time = departure_time + letter
        flight_info.append(departure_date)
        flight_info.append(departure_time)
        quote_date_time = i['QuoteDateTime']
        quote_date = ""
        quote_time = ""
        T_found = False
        for letter in quote_date_time:
            if letter != 'T' and T_found == False:
                quote_date = quote_date + letter
            elif letter == 'T':
                T_found = True
                continue
            if T_found == True:
                quote_time = quote_time + letter
        flight_info.append(quote_date)
        flight_info.append(quote_time)
    outbound_flight.append(flight_info)

    places = parse['Places']
    airports = {}
    for i in places:
        list_place = []
        place_id = i['PlaceId']
        airport_iata_code = i['IataCode']
        list_place.append(airport_iata_code)
        airport_name = i['Name']
        list_place.append(airport_name)
        city_name = i['CityName']
        list_place.append(city_name)
        country_name = i['CountryName']
        list_place.append(country_name)
        airports[place_id] = list_place

    carriers = parse['Carriers']
    carrier_list = {}
    for i in carriers:
        carrier_id = i['CarrierId']
        carrier_name = i['Name']
        carrier_list[carrier_id] = carrier_name

    currencies = parse['Currencies']
    for i in currencies:
        currency_code = i['Code']
        currency_symbol = i['Symbol']

    overall_flight_info = []  # combine all info to push to sql db
    for flight in outbound_flight:
        overall_flight_info.append(currency_code)  # not sure if I want to add this to SQL dashboard
        overall_flight_info.append(currency_symbol + str(flight[0]))  # price of flight
        overall_flight_info.append(flight[1])  # Direct/InDirect
        if len(carrier_list) == 1:
            for i in flight[2]:
                overall_flight_info.append(carrier_list[i])
        else:
            flight_carrier_list = []
            for key in carrier_list:  # add carriers to SQL dashboard
                flight_carrier_list.append(carrier_list[key])
            overall_flight_info.append(", ".join(flight_carrier_list))
        # add airport info to SQL dashboard
        # Departure Airport
        airport_ls = airports[flight[3]]
        overall_flight_info.append(airport_ls[1] + " Airport (" + airport_ls[0] + ")")
        overall_flight_info.append(airport_ls[2] + ", " + airport_ls[3])
        # Arrival Airport
        airport_ls = airports[flight[4]]
        overall_flight_info.append(airport_ls[1] + " Airport (" + airport_ls[0] + ")")
        overall_flight_info.append(airport_ls[2] + ", " + airport_ls[3])
        # date and time of flight
        overall_flight_info.append(flight[5])
        overall_flight_info.append(flight[6])
        # quote info
        overall_flight_info.append(flight[7])
        overall_flight_info.append(flight[8])
    return overall_flight_info

# Testing In-Bound/Out-Bound Flight Search
d_country = "US"
d_currency = "USD"
d_locale = "en-US"
d_originplace = "DEN-sky"
d_destinationplace = "JFK-sky"
d_outbounddate = "2020-12-01"

flight_data = []
departure_flight_data = callFlightApi(d_country, d_currency, d_locale, d_originplace, d_destinationplace, d_outbounddate)
print(departure_flight_data)

r_country = "US"
r_currency = "USD"
r_locale = "en-US"
r_originplace = "JFK-sky"
r_destinationplace = "DEN-sky"
r_outbounddate = "2020-12-22"
return_flight_data = callFlightApi(r_country, r_currency, r_locale, r_originplace, r_destinationplace, r_outbounddate)
print(return_flight_data)

inbound_outbound_flightdata = []
inbound_outbound_flightdata.append(departure_flight_data)
inbound_outbound_flightdata.append(return_flight_data)


def createDB(dbname, flight_data):
    conn = sqlite3.connect(dbname) # connect database to file dbname
    c = conn.cursor()  # cursor in vim, points to place in db
    c.execute('''CREATE TABLE Flights(Currency TEXT, Price TEXT, Direct TEXT, AirCarriers TEXT, DepartureAirport TEXT, DepartureCity TEXT, ArrivalAirport TEXT, ArrivalCity TEXT, FlightDate TEXT, FlightTime TEXT, QuoteDate TEXT, QuoteTime TEXT);''')
    for i in flight_data:
        c.execute("INSERT INTO Flights VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (i))
    c.execute("SELECT * FROM Flights")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

createDB('Flights2', inbound_outbound_flightdata)