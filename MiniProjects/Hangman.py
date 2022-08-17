#! python3
from getpass import getpass

play_again = True

while play_again:

    print(f'Welcome to Hangman!')
    word = list(getpass(prompt=f'To play, please enter a word (word will not be displayed): ').lower())

    for l in word:
        while not l.isalpha():
            word = list(
                getpass(prompt=f'Only enter letters, please enter a word (word will not be displayed): ').lower())
    hangman = ['_' for letter in word]

    print(hangman)

    word_copy = word[:]

    guess_counter = 6

    for n in range(10):
        letter = input(f'Please guess a letter: ').lower()
        while len(letter) > 1 or not letter.isalpha():
            letter = input(f'Please enter 1 letter: ').lower()

        if letter in word_copy:
            while letter in word_copy:
                i = word_copy.index(letter)
                hangman[i] = letter
                word_copy[i] = ' '
            if hangman == word:
                print(hangman)
                print(f"You win! The word is {''.join(word)}")
                break
            else:
                print(hangman)
                continue
        print(f'Incorrect')
        guess_counter -= 1

        if guess_counter == 1:
            print(f'You have {guess_counter} guess left')
        elif guess_counter == 0:
            print(f"You lose! The word was {''.join(word)}")
            break
        else:
            print(f'You have {guess_counter} guesses left')

    play = input(f'Do you want to play again? (Y/N): ').lower()
    while play != 'y' and play != 'n':
        play = input(f'Do you want to play? Only enter (Y/N): ').lower()
    if play == 'y':
        continue
    elif play == 'n':
        play_again = False


