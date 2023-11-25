import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print('')

playerChoice = input(
    'Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n')
player = int(playerChoice)  # cast str to int

if player < 1 or player > 3:
    sys.exit('You did not enter a number between 1-3, try again!\n')

computerChoice = random.choice('123')
computer = int(computerChoice)

print('')
print('You chose ' + str(RPS(player)).replace('RPS.', '') + '!')
print('Python chose ' + str(RPS(computer)).replace('RPS.', '') + '!\n')

if player == 1 and computer == 3:
    print('🥳 You win!\n')
elif player == 2 and computer == 1:
    print('🥳 You win!\n')
elif player == 3 and computer == 2:
    print('🥳 You win!\n')
elif player == computer:
    print('🤯 You tied Python!\n')
else:
    print('🐍 Python wins!\n')
