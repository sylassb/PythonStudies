#Melhore o jogo do DESAFIO 28 onde o
# computador vai “pensar” em um número entre
# 0 e 10. Só que agora o jogador vai tentar adivinhar
# até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

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


