word = input('Enter a word: ')
word = word.lower()

revealed = ''
exception_chars = ["'", '.', '?', ' ', ',']
for letter in word:
    if letter in exception_chars:
        revealed += letter
    else:
        revealed += '□'

hint = input('Enter a hint: ')

print('\n'*75)

lives = int(input('Number of lives: '))

the_phrase = 'The phrase was "'+word+'".'
line = '-'*75
guesses = []
while True:
    print(revealed,'\nPrevious guesses:',guesses)
    guess = input('Guess a letter or the whole thing: ')
    guess = guess.lower()
    print(line)
    if guess in guesses:
        print('You already guessed that')
        continue
    elif guess == '':
        print('Actually guess something')
        continue
    elif len(guess) > 1:
        if len(guess) != len(word) and guess != 'hint':
            print('Incorrect word length')
            continue
        elif guess == word:
            print('You won!\nYou guessed the whole thing!\n'+the_phrase)
            break
        elif guess == 'hint':
            print('The hint is','"'+hint+'".')
            continue
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
        print('You won!\nWith',lives,'lives left. '+the_phrase)
        break
    elif lives == 0:
        print('You ran out of lives. '+the_phrase)
        break
    guesses.append(guess)
