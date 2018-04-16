import random

input("Lets play guess my number. Press 'Enter' to continue.")

low_int = int(input('Enter your low number: '))
high_int = int(input('Enter your hight number: '))

hidden_int = random.randint(low_int, high_int)

guess_int = int(input('Your guess: '))
guess_count = 1

while guess_int != hidden_int:

    guess_int = int(input('Wrong try again: '))
    guess_count += 1
    
print('You are right! It only took ', guess_count, 'tries!')
