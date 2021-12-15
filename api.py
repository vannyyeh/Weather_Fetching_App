import requests
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

#Setting a various possible library that the user might enter
yes_answers = ["Y", "y", "yes", "YES", "Yes"]
no_answers = ["n", "N", "No", "NO", "no"]

#This is the function for getting API data from internet in realtime
def get_current_weather():
  api_key = '0dcd36fffe220d821c4c08c98ab17d5e' #My personal api key
  location = input("Please enter your city name of your location or Zip Code: ")
  api = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
  api_link = requests.get(api)
  api_data = api_link.json()
  if api_data['cod'] == '404': #In case there's an error from server
    print("Sorry, your city's information is not in our data.")
    restart() #Restart the game
  else:
    weather = api_data['weather'][0]['main']
    #This is kelvin to fahrenheit's formula
    temp = int(round(((api_data['main']['temp'])- 273.15) * 9/5 + 32))
    wind_speed = api_data['wind']['speed']
    feel_temp = int(round(((api_data['main']['feels_like'])- 273.15) * 9/5 + 32))
    max_temp = int(round(((api_data['main']['temp_max'])- 273.15) * 9/5 + 32))
    min_temp = int(round(((api_data['main']['temp_min'])- 273.15) * 9/5 + 32))
    # This is a f-String
    print(f"The weather in {location} is {weather} and the temperature is {temp}°F")
    more_info = input("Do you want to read further weather information? Y or N")
    if more_info in yes_answers:
      print(f"The wind speed in {location} is {wind_speed}. \nIt feels like {feel_temp}°F in {location}, the max tempertaure will be {max_temp}°F and the min can be {min_temp}°F\n")
      print("Below is a bar chart of the temp at the location")
      get_graph(temp,feel_temp,max_temp,min_temp)
      restart()
    elif more_info in no_answers:
      restart()

#Showing the temp graph of the location
def get_graph(a,b,c,d):
  objects = ('Temp', 'Feeling Temp', 'Max Temp', 'Min Temp')
  y_pos = np.arange(len(objects))
  performance = [a,b,c,d]
  plt.bar(y_pos, performance, align='center', alpha=0.5)
  plt.xticks(y_pos, objects)
  plt.ylabel('°F')
  plt.title('Temperature')
  plt.show()

#Loop and ask the user to join the game agian
def restart():
  restart = input("Do you want to know more about other city? Y or N")
  if restart in yes_answers:
    get_current_weather()
  else:
    print("\n\n\n-----------Welcome back to the homepage!-----------\n")
    from main import start_the_Game
    start_the_Game()
