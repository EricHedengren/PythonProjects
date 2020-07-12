word = input('Enter a word: ')

revealed = ''
for letter in word:
    if letter == ' ':
        revealed += ' '
    elif letter == "'":
        revealed += "'"
    else:
        revealed += '#'

lives = int(input('Number of lives: '))

guesses = []
while True:
    print('Previous guesses:',guesses)
    print(revealed)
    guess = input('Guess a letter or the whole thing: ')
    if guess in guesses:
        print('You already guessed that')
        continue
    elif guess == '':
        print('Actually guess something')
        continue
    elif len(guess) > 1:
        if len(guess) != len(word):
            print('Incorrect word length')
            continue
        elif guess == word:
            print('You won!\nYou won!\nYou guessed it!')
            break
        else:
            print('Incorrect word')
            lives -= 1
            print(lives,'lives left')

    elif guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                revealed = revealed[:i] + letter + revealed[i+1:]
        print('Right on')
    else:
        lives -= 1
        print(guess,"isn't in the word.",lives,'lives left.')
    if revealed == word:
        print('You won!\nYou won!\nWith',lives,'lives left.')
        break
    elif lives == 0:
        print('You ran out of lives. The word was','"'+word+'".')
        break
    guesses.append(guess)