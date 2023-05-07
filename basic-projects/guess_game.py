import random

print('I am thinking of a number between 1 and 20.')


ran = random.randint(1,20)
tries = 6
counter = 1
while True:
    print('Care to take a guess.......')
    num = int(input('Enter Your Number: '))
    if num < ran:
        print('your guess is too low')
    elif num > ran:
        print('Your is too high')
    else:
        print('Good job! You guessed my number in ' + str(counter) + ' guesses!')
        break
    if counter == tries:
        print('Nope. The number I was thinking of was ' + str(ran))
        break

    counter += 1