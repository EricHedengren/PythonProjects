import random
import time

def roll():
    return random.randint(1,6)

#d = {1:"1", 2:"2", 3:"A", 4:"G", 5:"M", 6:"D"}

number = 0
dieList = [None]*5
dieList[0] = 0

#timesPlayed = 0
#totalRolls = 0
wow = 0
x = True

while (x == True):
    while not all(x == dieList[0] for x in dieList[1:]):
        for i in range(5):
            dieList[i] = roll()
        number += 1
    if number == 1:
        wow += 1
        print(wow)
    #timesPlayed += 1
    #totalRolls += number
    #number = str(number)
    #print("average:", int(totalRolls/timesPlayed), "rolls:", number.zfill(5), "rolled:", d[dieList[0]], "wow:", wow)
    number = 0
    dieList[0] = 0