#! python3

import time
import datetime

# Create class that acts as a countdown
def countdown(h, m, s):

    # Calculate the total number of seconds
    totalSeconds = h * 3600 + m * 60 + s

    # While loop that checks if totalSeconds reaches zero
    # If not zero, decrement total time by one second
    while totalSeconds > 0:

        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=totalSeconds)

        # Prints the time left on the timer
        print(timer, end = '\r')

        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        totalSeconds -= 1

    print('Bzzzzt! The countdown is at zero seconds!')

# Inputs for hours, minutes, seconds on the timer
h = input('Enter the time in hours: ')
m = input('Enter the time in minutes: ')
s = input('Enter the time in seconds: ')
countdown(int(h), int(m), int(s))


