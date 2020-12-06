# import HotelScraper as hotel
# import FlightScraper as flight
# import ThingsToDoScraper as to do

city_info = {"Abu Dhabi": ["United Arab Emirates", "AE", "AUH"], "Adelaide": ["Australia", "AU", "ADL"],
             "Albuquerque": ["United States", "NM", "ABQ"], "Alicante": ["Spain", "ES", "ALC"],
             "Amsterdam": ["Netherlands", "NL", "AMS"], "Anaheim": ["United States", "CA", "ANA"],
             "Anchorage": ["United States", "AK", "ANC"], "Annapolis": ["United States", "MD", "ANN"],
             "Asheville": ["United States", "NC", "AVL"], "Athens": ["Greece", "GR", "ATH"],
             "Atlanta": ["United States", "GA", "ATL"], "Auckland": ["New Zealand", "NZ", "AKL"],
             "Austin": ["United States", "TX", "AUS"], "Baltimore": ["United States", "MD", "BWI"],
             "Bangkok": ["Thailand", "TH", "BKK"], "Barcelona": ["Spain", "ES", "BCN"],
             "Baton Rouge": ["United States", "LA", "BTR"], "Beijing": ["China", "CN", "PEK"],
             "Berlin": ["Germany", "DE", "BER"], "Boca Raton": ["United States", "FL", "BOC"],
             "Boston": ["United States", "MA", "BOS"], "Brisbane": ["Australia", "AU", "BNE"],
             "Brussels": ["Belgium", "BE", "BRU"], "Budapest": ["Hungary", "HU", "BUD"],
             "Buenos Aires": ["Argentina", "AR", "BUE"], "Burlington": ["United States", "VT", "BTV"],
             "Cabo San Lucas": ["Mexico", "MX", "CBS"], "Cairo": ["Egypt", "EG", "CAI"],
             "Calgary": ["Canada", "CA", "YYC"], "Cannes": ["France", "FR", "JCA"],
             "Cape Town": ["South Africa", "ZA", "CPT"], "Charleston": ["United States", "SC", "CRW"],
             "Charlotte": ["United States", "NC", "CLT"], "Chicago": ["United States", "IL", "CHI"],
             "Copenhagen": ["Denmark", "DK", "CPH"], "Cozumel": ["Mexico", "MX", "CZM"],
             "Dallas": ["United States", "TX", "DFW"], "Denver": ["United States", "CO", "DEN"],
             "Dubai": ["United Arab Emirates", "AE", "DXB"], "Dublin": ["Ireland", "IE", "DUB"],
             "Edinburgh": ["Scotland", "GB", "EDI"], "Fairbanks": ["United States", "AK", "FAI"],
             "Flagstaff": ["United States", "AZ", "FLG"], "Fort Lauderdale": ["United States", "FL", "FLL"],
             "Fort Myers": ["United States", "FL", "FMY"], "Galveston": ["United States", "TX", "GLS"],
             "Galway": ["Ireland", "IE", "GWY"], "Geneva": ["Switzerland", "CH", "GVA"],
             "Glasgow": ["Scotland", "GB", "GLA"], "Greenville": ["United States", "SC", "GSP"],
             "Hamburg": ["Germany", "DE", "HAM"], "Havana": ["Cuba", "CU", "HAV"],
             "Hong Kong": ["Hong Kong", "HK", "HKG"], "Honolulu": ["United States", "HI", "HNL"],
             "Houston": ["United States", "TX", "HOU"], "Ibiza": ["Spain", "ES", "IBZ"],
             "Indianapolis": ["United States", "IN", "IND"], "Istanbul": ["Turkey", "TR", "IST"],
             "Johannesburg": ["South Africa", "ZA", "JNB"], "Kansas City": ["United States", "MO", "MKC"],
             "Las Vegas": ["United States", "NV", "LAS"], "Lima": ["Peru", "PE", "LIM"],
             "Lisbon": ["Portugal", "PT", "LIS"], "London": ["England", "GB", "LON"],
             "Los Angeles": ["United States", "CA", "LAX"], "Madison": ["United States", "WI", "MSN"],
             "Madrid": ["Spain", "ES", "MAD"], "Manchester": ["England", "GB", "MAN"],
             "Marrakech": ["Morocco", "MA", "RAK"], "Melbourne": ["Australia", "AU", "MEL"],
             "Memphis": ["United States", "TN", "MEM"], "Mexico City": ["Mexico", "MX", "MEX"],
             "Miami": ["United States", "FL", "MIA"], "Milan": ["Italy", "IT", "MIL"],
             "Milwaukee": ["United States", "WI", "MKE"], "Moscow": ["Russia", "RU", "MOW"],
             "Myrtle Beach": ["United States", "SC", "MYR"], "Naples": ["Italy", "IT", "NAP"],
             "Nashville": ["United States", "TN", "BNA"], "New Orleans": ["United States", "LA", "MSY"],
             "New York": ["United States", "US", "JFK"], "Nice": ["France", "FR", "NCE"],
             "Oklahoma City": ["United States", "OK", "OKC"], "Omaha": ["United States", "NE", "OMA"],
             "Orlando": ["United States", "FL", "ORL"], "Oslo": ["Norway", "NO", "OSL"],
             "Ottawa": ["Canada", "CA", "YOW"], "Palm Springs": ["United States", "CA", "PSP"],
             "Panama City Beach": ["United States", "FL", "PCB"], "Paris": ["France", "FR", "PAR"],
             "Pensacola": ["United States", "FL", "PNS"], "Perth": ["Australia", "AU", "PER"],
             "Phoenix": ["United States", "AZ", "PHX"], "Phuket": ["Thailand", "TH", "HKT"],
             "Pittsburgh": ["United States", "PA", "PIT"], "Portland": ["United States", "OR", "PDX"],
             "Prague": ["Czechia", "CZ", "PRG"], "Puerto Vallarta": ["Mexico", "MX", "PVR"],
             "Quebec City": ["Canada", "CA", "YQB"], "Raleigh": ["United States", "NC", "RDU"],
             "Reno": ["United States", "NV", "RNO"], "Richmond": ["United States", "VA", "RIC"],
             "Rio de Janeiro": ["Brazil", "BR", "RIO"], "Rome": ["Italy", "IT", "ROM"],
             "Sacramento": ["United States", "CA", "SMF"], "Salt Lake City": ["United States", "UT", "SLC"],
             "Salzburg": ["Austria", "AT", "SZG"], "San Antonio": ["United States", "TX", "SAT"],
             "San Diego": ["United States", "CA", "SAN"], "San Francisco": ["United States", "CA", "SFO"],
             "San Jose": ["United States", "CA", "SJC"], "Santa Barbara": ["United States", "FL", "SBA"],
             "Santa Fe": ["United States", "NM", "SAF"], "Santo Domingo": ["Dominican Republic", "DO", "SDQ"],
             "Savannah": ["United States", "GA", "SAV"], "Seattle": ["United States", "WA", "SEA"],
             "Seoul": ["Korea, South", "KR", "SEL"], "Shanghai": ["China", "CN", "SHA"],
             "Singapore": ["Singapore", "SG", "SIN"], "Stockholm": ["Sweden", "SE", "ARN"],
             "Sydney": ["Australia", "AU", "SYD"], "Tallahassee": ["United States", "FL", "TLH"],
             "Tampa": ["United States", "FL", "TPA"], "Tokyo": ["Japan", "JP", "TYO"],
             "Toronto": ["Canada", "CA", "YYZ"], "Tucson": ["United States", "AZ", "TUS"],
             "Tulsa": ["United States", "OK", "TUL"], "Vancouver": ["Canada", "CA", "YVR"]}

# from form data read in travel information
# variables to store the data
home_city = "Mexico City"
destination = "Santo Domingo"
outbound_date = "2020-12-06"
inbound_date = "2020-12-24"

# select correct data to be imported into each correct scrapper
# flight data: need airport codes, to/from and dates
# hotel data: city/state or city/international country, format: Los-Angeles,CA, and dates
# things to do data: city/international country or city/state, format: Denver_CO, London_England
# flight parameters
home_iata = city_info[home_city][2]
destination_iata = city_info[destination][2]
# hotel parameters
hotel_city_temp = destination.replace(' ', '-')
if city_info[destination][0] != 'United States':
    hotel_location = hotel_city_temp + ',' + city_info[destination][0].replace(' ', '-')
else:
    hotel_location = hotel_city_temp + ',' + city_info[destination][1].replace(' ', '-')
# things to do parameters
todo_temp = destination.replace(' ', '_')
if city_info[destination][0] != 'United States':
    todo_location = todo_temp + '_' + city_info[destination][0].replace(' ', '_')
else:
    todo_location = todo_temp + '_' + city_info[destination][1].replace(' ', '_')

print(home_iata, destination_iata)
print(hotel_location)
print(todo_location)
