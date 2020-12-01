#!/usr/local/bin/python3.6
import pandas as pd
import city_code_helper as city
import json

df = pd.read_csv('worldcities.csv', sep=',')
df2 = df[['city', 'country', 'iso2']]
cities = []
for key, city in city.airports.items():
    cities.append(city)

df3 = df2[df2.city.isin(cities)].sort_values('city')  # only have cities with airports
df3.drop_duplicates(inplace=True)
df3.drop(df3[(df3['city'] == 'Amsterdam') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Athens') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Barcelona') & (df3['country'] == 'Venezuela')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Berlin') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Boston') & (df3['country'] == 'United Kingdom')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Buenos Aires') & (df3['country'] == 'Costa Rica')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Cairo') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Burlington') & (df3['country'] == 'Canada')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Dublin') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Geneva') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Glasgow') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Greenville') & (df3['country'] == 'Liberia')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Hamburg') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Houston') & (df3['country'] == 'United Kingdom')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Lima') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'London') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'London') & (df3['country'] == 'Canada')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Lisbon') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Manchester') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Melbourne') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Milan') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Moscow') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Naples') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Ottawa') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Paris') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Perth') & (df3['country'] == 'United Kingdom')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Perth') & (df3['country'] == 'Canada')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Portland') & (df3['country'] == 'Australia')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Richmond') & (df3['country'] == 'United Kingdom')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Richmond') & (df3['country'] == 'Australia')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Richmond') & (df3['country'] == 'Canada')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Richmond') & (df3['country'] == 'New Zealand')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Rome') & (df3['country'] == 'United States')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'San Antonio') & (df3['country'] == 'Puerto Rico')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'San Antonio') & (df3['country'] == 'Chile')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'San Diego') & (df3['country'] == 'Venezuela')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'San Francisco') & (df3['country'] == 'Mexico')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'San Francisco') & (df3['country'] == 'Argentina')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'San Francisco') & (df3['country'] == 'El Salvador')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'San Jose') & (df3['country'] == 'Philippines')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Santa Fe') & (df3['country'] == 'Argentina')].index, inplace=True)
df3.drop(df3[(df3['city'] == 'Vancouver') & (df3['country'] == 'United States')].index, inplace=True)
cities = df3['city'].to_list()
with open('city_list.json', 'w') as outfile:
    json.dump(cities, outfile)



