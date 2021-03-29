# Its a guess the number game where the computer 'thinks' about a number between 0 and 10 and the player
# try to guess the number, it also gives a tip to the player saying if the number chose by the computer
# is higher or lower than what was put by the player
# at the end of the game it shows how many tries were necessary to win

from random import randint
computer = randint(0, 10)
print('I am your computer ... Ive just thought about a number between 0 and 10.')
print('Can you guess the number? ')
right = False
guess = 0
while not right:
    player = int(input('What is your guess? '))
    guess += 1
    if player == computer:
        right = True
    else:
        if player < computer:
            print('More ... Try again.')
        elif player > computer:
            print('Less ... Try again.')
print(f'You made it with {guess} tries!')


