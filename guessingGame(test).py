# This is a number guessing game.
import random  # needed for generating a random number
import os
import csv

os.chdir(r'C:\Users\ddimo\Local Documents\Python\Local College')
name = []
score = []
playerInfo = []


def greetUser(i):  # Gets user name and prints greeting.
    print('Please enter your name.')
    name.append(input())
    print(f'Hello, {name[i]}')



def gameRound(number, i):  # Main generates random number and passes to gameRound where it loops until the user guesses
    # Correctly. The function then returns the number of guesses to main and stores them in a list
    print('I am thinking of a number between 1 and 10.')
    guess = -1  # Initializes the condition for the while loop
    guessesTaken = 0
    while guess != number:
        guess = int(input('Take a guess.'))

        guessesTaken += 1

        if guess < number:
            print('Your guess is too low')
        elif guess > number:
            print('Your guess is too high')
        else:
            score.append(guessesTaken)
            break  # This condition is the correct guess!

    print(f'Congratulations, {name[i]}! you guessed the number in {score[i]} tries!')


    return guessesTaken


def cleanUp():

    playerInfo = [[name], [score]]

    with open('scores.csv','w', newline='') as gameData:
        writer = csv.writer(gameData)
        writer.writerows(playerInfo)




def main():
    keepGoing = 'yes'
    i = 0
    while keepGoing == 'yes' or keepGoing == 'Yes':
        number = random.randint(1, 10)
        greetUser(i)
        gameRound(number, i)
        i += 1  # Counter value
        keepGoing = input('Should I start another game? ')

        if keepGoing != 'yes' or keepGoing != 'Yes':
            cleanUp()


main()
