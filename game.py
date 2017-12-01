# In this version of the game we add some personalization to the game with name input and guess count

import os	#import os class to allow for clearing of terminal screen
import random

os.system('clear')

print("Welcome to the number guessing game!\n")
name = input("What is your name? ")
num = random.randint(0, int(input("Please input the max number for this game: ")))
count = 0

print("Good luck, " + name + "!\n")

while True:
	guess = int(input("Your guess? "))
	count += 1

	if(guess > num):
		print("Your guess of " + str(guess) + " is too high\n")
	elif(guess < num):
		print("Your guess of " + str(guess) + " is too low\n")
	else:
		break

print("Congratulations, " + name + ", you are correct! It took you " + str(count) + " guesses.\n")