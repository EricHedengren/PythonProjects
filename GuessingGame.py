import random

x = int(input("Enter minimum value: "))
y = int(input("Enter maximum value: "))

number = random.randint(x,y)

print("Guess a number between " + str(x) + " and " + str(y) + ": ", end='')
guess = int(input())

while guess != number:
    if guess > y or guess < x:
        guess = int(input("Guess is out of range "))
    elif guess > number:
        guess = int(input("Guess is too high: "))
    elif guess < number:
        guess = int(input("Guess is too low: "))

print("You won!")