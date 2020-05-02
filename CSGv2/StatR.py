import random
from CSGv2 import RC

stats1 = []  # where all the numbers rolled are stored

stats2 = {
    "STR:": 0,
    "DEX:": 0,
    "CON:": 0,
    "INT:": 0,
    "WIS:": 0,
    "CHA:": 0
}

# stats2 holds the values from stats1 as dictionary values
# stats3 allows for easier printing of all values along with what key the value is assigned to

stats3 = [
    "STR:",
    "DEX:",
    "CON:",
    "INT:",
    "WIS:",
    "CHA:"
]


# Rolls all the values
def StatRoller():
    global stats1, stats2, stats3

    # appends stats1 with rolled values
    for i in range(6):
        stats1.append(random.randint(1, 20))

    x = 0
    y = 0

    # assigns each value to a dictionary key
    while x <= 5 and y <= 5:
        stats2[stats3[x]] = stats1[y]
        x += 1
        y += 1

    x = 0

    # prints all values along with their specified key
    for x in range(6):
        y = stats3[x]
        print(str(y) + str(stats2[y]))


# supposed to add Race modifiers to rolls, doesn't work atm
def Modify():
    if bcgen.race in RC.races:
        stats2["STR:"] += RC.races[bcgen.race][0]
        stats2["CHA:"] += RC.races["Dragonborn"][1]


# supposed to print the modified values, also doesn't work
def ModRoll():
    StatRoller()
    Modify()
    print("These are your modified stats.")
    print("~~~~~~~~~")


# prints all values alonside their respective keys + allows you to reroll values
def Roll():
    global stats1
    print("~~~~~~~~~")
    StatRoller()
    print("These are your unmodified rolls.")
    x = input("Reroll? [Y/N]\n")
    if x == "y":
        stats1.clear()
        Roll()
    if x == "n":
        return


def bcgen():
    print("~~~~~~~~~")
    print("Please type out the full name of your\ncharacter and the race/class you wish to\nplay as.")
    bcgen.name = input("Name: ")
    bcgen.race = input("Race: ")
    bcgen.cclass = input("Class: ")
    print("~~~~~~~~~")
    print(
        "Name: " + str(bcgen.name) + "\n",
        "\r" + "Race: " + str(bcgen.race) + "\n",
        "\r" + "Class: " + str(bcgen.cclass)
    )

    a = input("Is this accurate? [Y/N]\n")
    if a == "n":
        bcgen()
    if a == "y":
        return
