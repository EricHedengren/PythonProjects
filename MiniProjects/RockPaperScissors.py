import random

def winner(a,b):
    if a != 'rock' and a != 'paper' and a != 'scissors':
        return 'Invalid choice: '+a
    elif a == b:
        return "Tie"
    elif a == "rock" and b == "scissors":
        return w
    elif a == "paper" and b == "rock":
        return w
    elif a == "scissors" and b == "paper":
        return w
    elif a == "":
        return "Nothing was entered"
    else:
        return l

def decode(a):
    if a == 'r':
        return 'rock'
    elif a == 'p':
        return 'paper'
    elif a == 's':
        return 'scissors'
    else:
        return a

random_squence = ["rock", "paper", "scissors"]

w = "You win"
l = "You lose"
wins = 0
losses = 0
x = input("Rock, paper, scissors: ")

while x != 'quit':
    x = decode(x.lower())
    y = random_squence[random.randint(0,2)]
    print("I picked", y)
    r = winner(x,y)
    print(r)
    if r == l:
        losses += 1
    elif r == w:
        wins += 1
        print(str(wins)+':'+str(losses))
    x = input("Rock, paper, scissors: ")

print('Stopped')