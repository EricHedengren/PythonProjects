import random

def winner(a,b):
    if a == "rock" and b == "scissors":
        return "You win"
    elif a == "paper" and b == "rock":
        return "You win"
    elif a == "scissors" and b == "paper":
        return "You win" 
    elif a == b:
        return "Tie"
    else:
        return "You lose"

random_squence = ["rock", "paper", "scissors"]
y = random_squence[random.randint(0,2)]
x = input("Rock, paper, scissors: ")
x.lower()
print(winner(x,y))
print("I picked", y)