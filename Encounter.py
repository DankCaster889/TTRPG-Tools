import random

places = [
    "City",
    "Forest",
    "Cave",
    "Dungeon"
]


def coinflip():
    global x
    x = random.randint(1, 2)


class Location:
    def __init__(self, where, stat):
        self.where = where
        self.stat = stat

    def Place(self):
        self.where = random.choice(places)

    def Status(self):
        coinflip()
        if x == 1:
            self.stat = "Cleared"
        if x == 2:
            self.stat = "Inhabited"


class Encounter:
    def __init__(self, ent, type, loot):
        self.ent = ent
        self.type = type

    def ForF(self):
        coinflip()
        if x == 1:
            self.type = "Friendly"
        if x == 2:
            self.type = "Enemy"

    def GLoot(self):
        coinflip()
        if x == 1:
            self.loot = True
        if x == 2:
            self.loot = False

    def EntNum(self):
        x = random.randint(1, 10)
        self.ent = x


Enc = Encounter(None, None, None)
Loc = Location(None, None)


def EncLocGen():
    Enc.EntNum()
    Enc.ForF()
    Enc.GLoot()
    Loc.Place()
    Loc.Status()


def EncLocDesc():
    print("You are in a " + str(Loc.where) + ".")
    if Loc.stat == "Cleared":
        print("You can't see anybody from where you stand.")
    if Loc.stat == "Inhabited":
        print("You can see " + str(Enc.ent) + " beings from where you stand.")
    if Enc.type == "Enemy":
        print("The vibe is villainous.")
    if Enc.type == "Friendly":
        print("The vibe is friendly.")
    if Enc.loot is True:
        print("You can see valuable items from where you stand.")
    if Enc.loot is False:
        print("You can't see anything of value from where you stand.")


EncLocGen()
EncLocDesc()