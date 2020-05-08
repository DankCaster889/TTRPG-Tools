import random

race = [
    "Elf",
    "Dragonborn",
    "Orc",
    "Halfling",
    "Half-elf",
    "Half-orc",
    "Tiefling",
    "Gnome",
    "Dwarf"
]

bpart = [
    "Left Arm",
    "Right Arm",
    "Right Leg",
    "Left Leg",
    "Index Finger",
    "Pointer Finger",
    "Middle Finger",
    "Little Finger",
    "Thumb"
]

color = [
    "Blue",
    "Green",
    "Hazel",
    "Grey"
]

class Gender:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


Male = Gender("He", "Him", "He's", "His")
Female = Gender("She", "Her", "She's", "Her")
Other = Gender("They", "Them", "They're", "Their")

gender = [Male, Female, Other]

purpose = [
    "give a quest",
    "join the party for a while",
    "to deceive the party"
]


class Human:
    def __init__(self, races, gend, eyec, define, purp):
        self.races = races
        self.gend = gend
        self.eyec = eyec
        self.define = define
        self.purp = purp

    def Traits(self):
        self.races = random.choice(race)
        self.eyec = random.choice(color)
        self.gend = random.choice(gender)
        defining = [
            "scarred across " + str(self.gend.fourth) + " ",
            " missing " + str(self.gend.fourth) + " ",
            " got an extra "
        ]
        self.define = str(random.choice(defining)) + str(random.choice(bpart))
        self.purp = random.choice(purpose)

    def InitNPC(self):
        self.Traits()
        letter=list(self.races)
        if letter[0] in ["A", "E", "I", "O", "U"]:
            global x
            x = " an "
        else:
            x = " a "
        print("This is, well, whoever they are. " + str(self.gend.third) + x + str(self.races) + ", and has " + str(
            self.eyec) + " eyes.\n",
              str(self.gend.fourth) + " reason for being here is to " + str(self.purp) + ".",
              "Something unique about " + str(self.gend.second) + " is that " + str(self.gend.third) + " " + str(
                  self.define)
              )


NPC = Human(None, None, None, None, None)

NPC.InitNPC()
