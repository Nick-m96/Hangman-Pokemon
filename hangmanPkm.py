# -*- coding: utf-8 -*-
import random
import requests

GALLOW = ['''   

        +---+
        |   |
            |
            |
            |
            |
            =========''','''   

        +---+
        |   |
        0   |
            |
            |
            |
            =========''','''   

        +---+
        |   |
        0   |
        |   |
            |
            |
            =========''','''   

        +---+
        |   |
        0   |
       /|   |
            |
            |
            =========''','''   

        +---+
        |   |
        0   |
       /|\  |
            |
            |
            =========''','''   

        +---+
        |   |
        0   |
       /|\  |
        |   |
            |
            =========''','''   

        +---+
        |   |
        0   |
       /|\  |
        |   |
       /    |
            =========''','''   

        +---+
        |   |
        0   |
       /|\  |
        |   |
       / \  |
            =========''','''   

        +---+
        |   |
        0   |
        .   |
       /|\  |
        |   |
       / \  =========''']
POKEMON = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(random.randint(1,151))).json()['name']

def title():
    print('''
    ***********************************************************
    ***********************************************************
    *********************   Ahorcado Pkm  *********************
    ***********************************************************
    ***********************************************************
    The player must guess the Pokemon name. Only have the 1 gen
    ***********************************************************''')

def startGame():
    fails = 0
    hiddenPkm = ['-'] *len(POKEMON)
    isComplete = False
    
    while fails < 8 and isComplete == False:
        indexes = list()
        displayImage(hiddenPkm, fails)
        letter = input('Pick a letter: ')

        for i in range(len(POKEMON)):
            if letter == POKEMON[i]:
                indexes.append(i)
        if len(indexes) == 0:
            fails += 1
        else:
            isComplete = True
            for i in indexes:
                hiddenPkm[i] = letter
            for i in range(len(POKEMON)):
                if POKEMON[i] != hiddenPkm[i]:
                    isComplete = False

    if fails == 8: 
        print('You fail, the pokemon was {} :('.format(POKEMON))
    else:
        displayImage(hiddenPkm, fails)
        print('You win :D')

def displayImage(hiddenPkm, index):
    print(GALLOW[index])
    print('')
    print(hiddenPkm)
    print('--- * --- * --- * --- * --- * --- * --- * ---')

if __name__ == "__main__":
    title()
    startGame()


