import random

x = int(input("Enter minimum value: "))
y = int(input("Enter maximum value: "))

number = random.randint(x,y)

print("Guess a number between " + str(x) + " and " + str(y) + ": ", end='')
guess = int(input())
guesses = 1

while guess != number:
    guesses += 1
    if guess > y or guess < x:
        print("Guess is out of range.\nGuess again: ",end='')
    elif guess > number:
        print("Lower: ",end='')
    elif guess < number:
        print("Higher: ",end='')
    guess = int(input())

print("You won! It took",guesses,"guesses.")