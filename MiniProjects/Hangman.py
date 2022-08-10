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
    word = list(getpass(prompt=f'To play, please enter a word (word will not be displayed):').lower())
    for l in word:
        while not l.isalpha():
            word = list(getpass(prompt=f'Only enter letters, please enter a word (word will not be displayed):').lower())
    hangman = ['_' for letter in word]
    print(hangman)
    wordCopy = word.copy()
    guessCounter = 6
    for n in range(10):
        letter = input(f'Please guess a letter:').lower()
        while len(letter) > 1 or not letter.isalpha():
            letter = input(f'Please enter 1 letter:').lower()
        if letter in wordCopy:
            while letter in wordCopy:
                i = wordCopy.index(letter)
                hangman[i] = letter
                wordCopy[i] = ' '
            if hangman == word:
                print(hangman)
                print(f"You win! The word is {''.join(word)}")
                break
            else:
                print(hangman)
                continue
        print(f'Incorrect')
        guessCounter -= 1
        if guessCounter == 1:
            print(f'You have {guessCounter} guess left')
        elif guessCounter == 0:
            print(f"You lose! The word was {''.join(word)}")
            break
        else:
            print(f'You have {guessCounter} guesses left')
else:
    exit()


