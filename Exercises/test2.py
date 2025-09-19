import random

number = random.randint(1, 100)
max = 100
min = 1
guess = (min + max) // 2
numberOfGuesses = 0

while guess != number:
    numberOfGuesses += 1

    if guess < number:
        min = guess + 1
    elif guess > number:
        max = guess - 1
    else:
        print("Houston, we have a problem. Please enter a number between 1 and 100.")
    
    guess = (min + max) // 2

print(f'The computer guessed the number {number} correctly and it only took {numberOfGuesses} tries!')