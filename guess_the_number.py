import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = input(f'Guess a number between 1 and {x}: ')
        if guess < random_number:
            print('Sorry! Guess again. Guess is lower than the number.')
        elif guess > random_number:
            print('Sorry! Guess again. Guess is higher than the number.')
    print(f'Viola! You have guesses the number! It was {random_number}.')

guess(100)