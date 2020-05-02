import sys

word = input("Enter a word: ") # Word can't have repeat letters 
word.lower()
lives = int(input("How many lives: "))
wordList = []
for i in word:
    wordList.append(i)

printer = []
for i in wordList:
    printer.append("X")

x = input("Guess a letter: ")
x.lower()

for i in range(lives):
    if x in wordList and "X" in printer:
        lives += 1
        printer[wordList.index(x)] = x
        if "X" not in printer:
            f = ''
            for i in printer:
                f += i
            print(f)
            sys.exit("You won")
    print(printer)
    x = input("Guess a letter: ")
    x.lower()

sys.exit("You ran out of lives")