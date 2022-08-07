#! python3
# This is a computer age guessing game
import random

chance = 5

for i in range(1, 50):
    guess = random.randint(1, 50)
    print('Is your age ' + str(guess) +'?:')
    Age_answer = input().lower()
    while Age_answer != 'y' and Age_answer != 'n':
        print('Please enter "y" for "yes" and "n" for "no".')
        Age_answer = input().lower()
        continue
    if Age_answer == 'y':
        print('Computer is the winner!')
        break
    else:
        chance = chance - 1
        if chance > 1:
            print(str(chance) + ' guesses left')
        elif chance == 0:
            print('Computer has lost this one!')
            break
        else:
            print(str(chance) +' guess left')

