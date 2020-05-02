from CSGv2 import StatR

# holds all races + stat mods available in base D&D 5e
races = {
    "Dragonborn": [StatR.stats2["STR:"] + 2, StatR.stats2["CHA:"] + 1],
    "Dwarf": 2,
    "Elf": 2,
    "Gnome": 2,
    "Half-elf": [2, 1],
    "Half-orc": [2, 1],
    "Halfling": 2,
    "Human": 1,
    "Tiefling": [2, 1]
}

# holds all classes available in base D&D 5e
classes = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]
