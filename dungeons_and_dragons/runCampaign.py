import json
from character import Character

def main():
    c = loadCharacter()
    campaignCharacter = Character(c["name"], c["race"], c["class"])

    startCampaign(campaignCharacter)

def loadCharacter():
    f = open('character.txt', 'r')
    characterStr = f.read()
    characterStr = characterStr
    characterJSON = json.loads(characterStr)
    return characterJSON

def startCampaign(campaignCharacter):
    print('So the journey begins for ' + campaignCharacter.getName() + ' the ' + campaignCharacter.getRace() + ' ' + campaignCharacter.getClass() + '...')
    print('\nloading...(not really)\n')

    response = askPlayerResponse('You wake up in your bed, groggy, and feeling like you could get some sleep but you have to use the make kill and make your breakfast and make yourself a morning drink. \nWhere do you want to start(breakfast, drink)? ')

    if (response == 'breakfast'):
        print('Go get breakfast')
    elif (response == 'drink'):
        print('Go make your drink')
    

def askPlayerResponse(q):
    return input(q)

main()
