import random

secret_num = random.randint(1, 30)
print(secret_num)

while True:
    user_num = int(input('Enter a number: '))
    # print(type(user_num))
    if user_num > secret_num:
        print('Your number is too high')
    elif user_num < secret_num:
        print('Your number is too low')
    else:
        print('Hey You Won!!')
        break
