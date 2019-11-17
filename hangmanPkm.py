# -*- coding: utf-8 -*-
import random

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
POKEMON = ['charmander', 'squirtle', 'bulbasaur', 'charizard', 'venusaur']

def title():
    print('''
    ***********************************************************
    ***********************************************************
    *********************   Ahorcado Pkm  *********************
    ***********************************************************
    ***********************************************************
    The player must guess the Pokemon name. Only have the 1 gen
    ***********************************************************''')

def startGame(pokemon):
    fails = 0
    pokemon
    hiddenPkm = ['-'] *len(pokemon)
    isComplete = False
    
    while True:
        indexes = list()
        displayImage(hiddenPkm, fails)
        letter = input('Pick a letter: ')

        for i in range(len(pokemon)):
            if letter == pokemon[i]:
                indexes.append(i)
        if len(indexes) == 0:
            fails += 1
        else:
            isComplete = True
            for i in indexes:
                hiddenPkm[i] = letter
            for i in range(len(pokemon)):
                if pokemon[i] != hiddenPkm[i]:
                    isComplete = False

        if fails == 8: 
            displayImage(hiddenPkm,fails)
            print('You fail, the pokemon was {} :('.format(pokemon))
            break
        elif isComplete == True:
            print('You win :D')
            break

def displayImage(hiddenPkm, index):
    print(GALLOW[index])
    print('')
    print(hiddenPkm)
    print('--- * --- * --- * --- * --- * --- * --- * ---')

if __name__ == "__main__":
    title()

    pkm = random.randint(0, len(POKEMON)-1)

    startGame(POKEMON[pkm])


