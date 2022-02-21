# Programmer: Charlotte Osburn
# Date 2.21.2022
# Version 3.6

from time import sleep  #Print to one line with time delay between prints
import colorama
from colorama import Fore, Back, Style
# Libraries Imported Here
colorama.init(strip=False, autoreset=True)

import random

# WELCOME BRANCH
# Code Name - Hornet

print(Fore.LIGHTMAGENTA_EX + "Welcome to Hornets InfoTechCenter\n"); sleep(1)

print(Fore.LIGHTCYAN_EX + "Hornet's Operating System Booting Up\n")

# GAS BRANCH

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    curentGasLevel = random.choice(gasLevelList)
    return curentGasLevel

# Variable calls the value of gasLevelGauge Function
gasLevelIndicator = ""
gasLevelIndicator = gasLevelGauge()

# Create If-ELIF-ELSE statements using the Comparative Operator == Equal To in order to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell","BP","Citgo","Circle K","Mobil","Speedway","Marathon","Love's","Meijer","Costco","Sunoco"]
    miles = round(random.uniform(1,25), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\n Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***\n Your gas tank is LOW\n The closest gas station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("You are on a QUARTER TANK of gas\nStart planning a visit to a gas station")
    elif gasLevelIndicator == "Half Tank":
        print("You have a HALF Tank of gas\nYou have 125 more miles to empty")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("You have THREE QUARTER TANK of gas\nYou have 205 more miles to empty")
    else:
        print("You have a FULL Tank of gas, Congratulations.\nYou have 310 more miles to empty")

# Call Functions Here
gasLevelAlert()

