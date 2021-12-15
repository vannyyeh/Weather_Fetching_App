#import Python built-in function
from datetime import datetime
import os
import csv
import sys

#import custom module for all functions
from api import get_current_weather, restart, get_graph
from his import get_history_weather, get_monthly_weather, choose_the_game
from color import *

#having various options for the input for the cases
exit_answers = ["n", "N", "No", "NO", "no", "exit", "Exit", "EXIT"]
help_answers = ["h", "help", "Help", "H"]

def start_the_Game():
  Api_or_historical = input(Blue + 'Do you want to know historical weather data of Texas of current weather OR all the city in the world?' + Green + '\n\npress [1] Current weather\n\npress [2] Texas historical data from Jan. to Mar.\n\nEnter No or exit to exit the program \n\nEnter Help for help' + Color_Off)
  while True:
    if Api_or_historical == ('1'): #direct to the API
      get_current_weather()
    elif Api_or_historical == ('2'): #direct to the historical data
      choose_the_game()
    elif Api_or_historical in exit_answers:
      print("See you next time!")
      exit() #exit the whole game, not useing quit or break here
    elif Api_or_historical in help_answers:
      print("This game is designed to fetch real-time weather data and analyze historical data. Follow and enter the right input of the guideline.")
      start_the_Game()
    else:
      print('Wrong input! Please check it again!')
      start_the_Game()


#execute the program
print(BIRed + 'Welcome to the Weather Fetching app!' + Color_Off) #Welcoming meessage
start_the_Game()
