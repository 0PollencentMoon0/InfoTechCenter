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
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\n Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***\n Your gas tank is LOW\n The closest gas station is " + random.choice(gasStations))
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

