
import random
import sys

def roller(string):
    """
    Generate a string.

    Args:
        string: (str): write your description
    """
    plus_or_minus = None
    modifier = 0
    d_index = string.find('d')
    die_amount = int(string[:d_index])

    if '+' in string:
        mod_index = string.find('+')
        die = int(string[d_index+1:mod_index])
        modifier = int(string[mod_index+1:])
        plus_or_minus = True
    elif '-' in string:
        mod_index = string.find('-')
        die = int(string[d_index+1:mod_index])
        modifier = int(string[mod_index+1:])
        plus_or_minus = False
    else:
        die = int(string[d_index+1:])

    # list of rolls
    dice = [random.randint(1, die) for _ in range(die_amount)]
    roll = sum(dice)

    if die == 20 and die_amount > 1:
        high = max(dice)
        low = min(dice)

        if modifier > 0 and plus_or_minus == True:
            high += modifier
            low += modifier
        else:
            high -= modifier
            low -= modifier

    if plus_or_minus == True:
        roll += modifier
    elif plus_or_minus == False:
        roll -= modifier

    if die_amount == 1 and die == 20:
        if 20 in dice:
            roll = 'Natural 20'
        elif 1 in dice:
            roll = 'Natural 1'    

    if die_amount == 2 and die == 20:
        print(f'You rolled: {dice}')
        print(f'High: {high}')
        print(f'Low: {low}')
    elif die_amount > 1:
        print(f'You rolled: {dice}')
        print(f'Total: {roll}')
    elif plus_or_minus == True or plus_or_minus == False:
        print(f'You rolled: {dice}')
        print(f'You rolled a total of: {roll}')
    else:
        print(f'You rolled: {roll}')

if __name__ == '__main__':
    # python dice.py 1d20, 2d20+2 or 1d20-2 
    roller(sys.argv[-1])



