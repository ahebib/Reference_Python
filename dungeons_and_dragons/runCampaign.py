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
    print('So the journey begins for...')
    print(campaignCharacter.getName() + ' the ' + campaignCharacter.getRace() + ' ' + campaignCharacter.getClass())

main()
