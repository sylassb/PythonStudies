# It reads two values and show a menu screen:
# [1] Addition
# [2] Multiplication
# [3] Greater Number
# [4] New Numbers
# [5] Finish the program
# It accomplish the requested operaton of each option:

from time import sleep
n1 = int(input('First Value: '))
n2 = int(input('Second Value: '))
option = 0
while option != 5:
    print('''        
    [1] Addition
    [2] Multiplication
    [3] Greater Number
    [4] New Numbers
    [5] Finish the Program''')
    option = int(input('>>>>>>> What is your option? '))
    if option == 1:
        sum = n1 + n2
        print(f'The sum between {n1} + {n2} is {sum} ')
    elif option == 2:
        times = n1 * n2
        print(f'The result of {n1} x {n2} is {times}')
    elif option == 3:
        if n1 > n2:
            greater = n1
        else:
            greater = n2
        print(f'Between {n1} and {n2} the greater number is {greater}')
    elif option == 4:
        print('Give me new numbers: ')
        n1 = int(input('First Value: '))
        n2 = int(input('Second Value:'))
    elif option == 5:
        print('Finishing ...')
    else:
        print('Invalid Option. Try Again!')
    print('=-=' * 10)
    sleep(2)
print('End of Program! Bye!')
