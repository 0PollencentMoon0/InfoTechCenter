import random

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    curentGasLevel = random.choice(gasLevelList)
    print(curentGasLevel)

gasLevelGauge()
