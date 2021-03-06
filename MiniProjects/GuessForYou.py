from random import randint

def higher_lower(guess):
    if guess > number:
        return('Too High')
    elif guess < number:
        return('Too Low')
    elif guess == number:
        return('You Won')

def run_guesser(min2, max2):
    feedback = ''
    count = 0
    while feedback != 'You Won':
        count += 1
        guess = int(((max2-min2)/2)+min2)
        feedback = higher_lower(guess)
        if feedback == 'Too High':
            max2 = guess
        elif feedback == 'Too Low':
            min2 = guess
    return count

min1 = 1
max1 = 10

num_guess = []

for i in range(1000):
    number = randint(min1, max1)
    num_guess.append(run_guesser(min1, max1+1))

print(sum(num_guess)/len(num_guess))