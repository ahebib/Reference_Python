from random import randrange
import json
from character import Character

#Start creating a Dungeon and Dragon Character
def main():
    newCharacter = Character(generateName(), generateRace(), generateClass())
    characterObject = {
        "name": newCharacter.getName(),
        "race": newCharacter.getRace(),
        "class": newCharacter.getClass()
    }
    f = open('character.txt', 'w')
    json.dump(characterObject, f)
    f.close()

def generateName():
    names = ['Edward', 'Alphonse', 'Luck', 'Grainlore', 'Magma', 'Yuki', 'Lev', 'Circ', 'Morrigan', 'Nyx', 'Chronos', 'Claudius', 'Greybeard', 'Astra', 'Zero', 'Uwu', 'Ara-ara', 'Yggdrasil', 'Lloyd', 'Colette', 'Raine', 'Genis', 'Kratos', 'Axe', 'Axel', 'Orion']
    return names[randrange(len(names))]

def generateRace():
    races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling'];
    return races[randrange(len(races))]

def generateClass():
    classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
    return classes[randrange(len(classes))]

main()
