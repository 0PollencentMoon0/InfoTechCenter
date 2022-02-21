# WELCOME BRANCH

# Code Name - Hornet

from time import sleep  #Print to one line with time delay between prints
import colorama
from colorama import Fore, Back, Style
colorama.init(strip=False, autoreset=True)

print(Fore.LIGHTMAGENTA_EX + Back.BLACK + Style.BRIGHT + "Welcome to Hornets InfoTechCenter\n"); sleep(1)

print(Fore.LIGHTCYAN_EX + Back.WHITE + Style.DIM + "Hornet's Operating System Booting Up\n")

# GAS BRANCH

import random

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
    miles = random.randint(1,25)
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

