import csv
import pandas as pd
import numpy as np
from datetime import datetime
from color import *

#grouping months by using datetime from csv
records = pd.read_csv(r'Texas_weather_2020.csv')
records['time'] = pd.to_datetime(records.time) #get the 'time' column
ts1 = pd.to_datetime('2020-01-01') and pd.to_datetime('2020-01-31') #setting the range for the Jan
ts2 = pd.to_datetime('2020-02-01') and pd.to_datetime('2020-02-29')#setting the range for the Feb
ts3 = pd.to_datetime('2020-03-01') and pd.to_datetime('2020-03-31')#setting the range for the March
sum_lt_1 = records.loc[records.time <= ts1, :]['temperatureLow'].sum()
sum_ht_1 = records.loc[records.time <= ts1, :]['temperatureHigh'].sum()
sum_dp_1 = records.loc[records.time <= ts1, :]['dewPoint'].sum() #sum of temp of Jan
sum_lt_2 = records.loc[records.time <= ts2, :]['temperatureLow'].sum()
sum_ht_2 = records.loc[records.time <= ts2, :]['temperatureHigh'].sum()
sum_dp_2 = records.loc[records.time <= ts2, :]['dewPoint'].sum()#sum of temp of Feb
sum_lt_3 = records.loc[records.time <= ts3, :]['temperatureLow'].sum()
sum_ht_3 = records.loc[records.time <= ts3, :]['temperatureHigh'].sum()
sum_dp_3 = records.loc[records.time <= ts3, :]['dewPoint'].sum()#sum of temp of March


with open('Texas_weather_2020.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)

#Months data structure
months = {
  "2020-01" : {
    "Average of the highest temp": round(sum_ht_1/31),
    "Average of the lowest temp": round(sum_lt_1/31),
    "Average of the dew point": round(sum_dp_1/31),
  },
  "2020-02" : {
    "Average of the highest temp": round(sum_ht_2/29),
    "Average of the lowest temp": round(sum_lt_2/29),
    "Average of the dew point": round(sum_dp_2/29),
  },
  "2020-03" : {
    "Average of the highest temp": round(sum_ht_3/31),
    "Average of the lowest temp": round(sum_lt_3/31),
    "Average of the dew point": round(sum_dp_3/31),
  }
}

#This is the function for getting historical data of Texas
def choose_the_game():
  print('Pick your own way to read the data!')
  answer2 = input('Press [1] Organized data by monthly \nPress [2] Manually check')
  while True:
    if answer2 == ('1'):
      get_monthly_weather()
    elif answer2 == ('2'):
      get_history_weather()
    else:
      print('Wrong input! Please check it again!')
      choose_the_game()

#This function gets the exact month input from user and it use the dictionary to loop the value from the csv
def get_monthly_weather():
  print('Please follow the format of YYYY-MM')
  print("Choose a month:")
  for month in ["2020-01", "2020-02", "2020-03"]:
    print(month)
  month = input()
  if month in ["2020-01", "2020-02", "2020-03"]:
    print(Purple + "For the month of", month +":" + Color_Off)
    stat = months[month]
    for stat_name, value in stat.items():
      print(stat_name, "is", value, "°F")
  else:
    print('Wrong input! Please check it again!')
  restart2() #loop again the game

#This function output directly when it received the index od the row number from csv
def get_history_weather():
  answer = input(Blue + 'Welcome to the Texas Dic of Weather!' + Color_Off +'\nWhat date do you want to know from Jan to Mar?\n\nPlease follow the format of YYYY-MM-DD')
  with open('Texas_weather_2020.csv', 'r') as csv_file:
    date = csv.reader(csv_file)
    for row in date:
      if row[3] == (answer):
        print(Purple + "The summary of the day is: " + row[4])
        print("The highest temp of the day is: " + row[9] + "°F")
        print("The lowest temp of the day is: " + row[10] + "°F")
        print("The dew point of the day is: " + row[11] + "°F")
        print("The humidity of the day is: " + row[12] + Color_Off)

    restart2() #loop again the game


#Loop and ask the user to join the game agian
def restart2():
  answer = input("\n\nPress [1] Organized monthly weather data \nPress [2] Manually data check \n" + Cyan + "Press anything to return back to homepage" + Color_Off)
  while True:
    if answer == ('1'):
      get_monthly_weather()
    elif answer == ('2'):
      get_history_weather()
    else:
      print("\n\n\n-----------Welcome back to the homepage!-----------\n")
      from main import start_the_Game
      start_the_Game()
      
