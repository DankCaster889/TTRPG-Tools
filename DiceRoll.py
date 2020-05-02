import random

rolls=[]

def Dice(x, y):
    for i in range(int(y)):
        rolls.append(random.randint(1, int(x)))
    print(rolls)

x = input("Sides: ")

y = input("Number of dice: ")

Dice(x, y)
