#! python3
from getpass import getpass

playAgain = True

while playAgain == True:
    play = input(f'Do you want to play? (Y/N):').lower()
    while play != 'y' and play != 'n':
        play = input(f'Do you want to play? Only enter (Y/N):').lower()
    if play == 'y':
        playAgain = True
    elif play == 'n':
        exit()
    print(f'Welcome to Hangman!')
    word = getpass(prompt=f'To play, please enter a word (word will not be displayed):').lower()
    while not word.isalpha():
        word = getpass(prompt=f'Only enter letters, please enter a word (word will not be displayed):').lower()
    hangman = ['_' for letter in word]
    print(hangman)
    wordCopy = '' + word
    guessCounter = 6
    for n in range(10):
        letter = input(f'Please guess a letter:').lower()
        while len(letter) > 1 or not letter.isalpha():
            letter = input(f'Please enter 1 letter:').lower()
        if letter in word:
            while letter in word:
                i = word.index(letter)
                hangman.pop(i)
                hangman.insert(i, letter)
                word = word.replace(letter, ' ', 1)
            if ''.join(hangman) == wordCopy:
                print(hangman)
                print(f'You win! The word is {wordCopy}')
                break
            else:
                print(hangman)
                continue
        print(f'Incorrect')
        guessCounter -= 1
        if guessCounter == 1:
            print(f'You have {guessCounter} guess left')
        elif guessCounter == 0:
            print(f'You lose! The word was {wordCopy}')
            break
        else:
            print(f'You have {guessCounter} guesses left')
else:
    exit()


