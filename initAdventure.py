from character import Character

#Start creating a Dungeon and Dragon Character
def main():
    newCharacter = Character('Ammar', 'Half Elf', 'Sorcerer')
    print('Character name: ' + newCharacter.getName())
    print('Character race: ' + newCharacter.getRace())
    print('Character class: ' + newCharacter.getClass())

main()
