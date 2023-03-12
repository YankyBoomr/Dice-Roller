# This is a Dice roller

import random

from PIL import Image



def diceroller():
    roll20 = random.randint(1, 20)
    roll10 = random.randint(1, 10)
    roll8 = random.randint(1, 8)
    roll6 = random.randint(1, 6)
    roll4 = random.randint(1, 4)
    roll100 = random.randint(0, 99)

    print('Which dice do you want to roll? (d20, d10, d8, d6, d4, d100)')

    answer = input()

    if answer == 'd20':
        print(roll20)
    if answer == 'd10':
        print(roll10)
    if answer == 'd8':
        print(roll8)
    if answer == 'd6':
        print(roll6)
    if answer == 'd4':
        print(roll4)
    if answer == 'd100':
        print(roll100)



diceroller()


def rollagain():
    print('Do you want to roll again? y/n')

    answer = input()

    if answer == 'y':
        diceroller()
    else:
        print('Have a nice day!')


#rollagain()
